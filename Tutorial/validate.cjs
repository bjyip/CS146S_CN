const fs = require('fs')
const path = require('path')
const vm = require('vm')

const root = __dirname
const files = []
const directories = [root]
while (directories.length) {
  const directory = directories.pop()
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const location = path.join(directory, entry.name)
    if (entry.isDirectory()) directories.push(location)
    else if (entry.isFile() && entry.name.endsWith('.md')) {
      files.push(path.relative(root, location))
    }
  }
}
files.sort()
const errors = []
let links = 0
let blocks = 0

for (const file of files) {
  const location = path.join(root, file)
  const source = fs.readFileSync(location, 'utf8')
  if (/[^\S\r\n]+$/m.test(source)) {
    errors.push(`${file}: trailing whitespace`)
  }
  const fences = source.match(/^```/gm) || []
  if (fences.length % 2) errors.push(`${file}: unclosed code fence`)

  for (const match of source.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)) {
    const target = match[1]
    if (/^(https?:|mailto:|#)/.test(target)) continue
    links++
    try {
      const resolved = path.resolve(
        path.dirname(location),
        decodeURIComponent(target.split('#')[0])
      )
      if (!fs.existsSync(resolved)) errors.push(`${file}: missing ${target}`)
    } catch (error) {
      errors.push(`${file}: invalid link ${target}: ${error.message}`)
    }
  }

  const codePattern = /^```([^\r\n]*)\r?\n([\s\S]*?)^```/gm
  for (const match of source.matchAll(codePattern)) {
    blocks++
    try {
      if (match[1] === 'json') JSON.parse(match[2])
      if (['javascript', 'js'].includes(match[1])) {
        new vm.Script(match[2])
      }
    } catch (error) {
      errors.push(`${file}: invalid ${match[1]} block: ${error.message}`)
    }
  }
}

const readme = fs.readFileSync(path.join(root, '..', 'README.md'), 'utf8')
if (!readme.includes('(Tutorial/README.md)')) {
  errors.push('Root README: missing tutorial entry')
}

if (errors.length) {
  console.error(errors.join('\n'))
  process.exitCode = 1
} else {
  console.log(
    `Validated ${files.length} documents, ${links} links, ${blocks} code blocks`
  )
}
