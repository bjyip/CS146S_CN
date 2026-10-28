const fs = require('fs')
const path = require('path')
const vm = require('vm')

const root = __dirname
const files = fs.readdirSync(root).filter(file => file.endsWith('.md'))
const errors = []
let links = 0
let blocks = 0

for (const file of files) {
  const source = fs.readFileSync(path.join(root, file), 'utf8')
  if (/[^\S\r\n]+$/m.test(source)) {
    errors.push(`${file}: trailing whitespace`)
  }
  const fences = source.match(/^```/gm) || []
  if (fences.length % 2) errors.push(`${file}: unclosed code fence`)

  for (const match of source.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)) {
    const target = match[1]
    if (/^(https?:|mailto:|#)/.test(target)) continue
    links++
    const resolved = path.resolve(
      root,
      decodeURIComponent(target.split('#')[0])
    )
    if (!fs.existsSync(resolved)) errors.push(`${file}: missing ${target}`)
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
