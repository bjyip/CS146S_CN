$ErrorActionPreference = 'Stop'
$folder = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\Fall2025_cn'))
$app = New-Object -ComObject PowerPoint.Application
try {
  foreach ($file in Get-ChildItem -LiteralPath $folder -Filter '*.pptx') {
    $deck = $app.Presentations.Open($file.FullName, -1, 0, 0)
    try {
      $deck.Export((Join-Path $PSScriptRoot ($file.BaseName + '.preview')), 'PNG', 1280, 720)
      Write-Output ("OPENED {0}: {1} slides" -f $file.Name, $deck.Slides.Count)
    } finally {
      $deck.Close()
      [void][Runtime.InteropServices.Marshal]::ReleaseComObject($deck)
    }
  }
} finally {
  $app.Quit()
  [void][Runtime.InteropServices.Marshal]::ReleaseComObject($app)
}
