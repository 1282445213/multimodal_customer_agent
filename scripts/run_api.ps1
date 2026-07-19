$ErrorActionPreference = "Stop"

$CodeRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$SourceRoot = Join-Path $CodeRoot "src"
$separator = [IO.Path]::PathSeparator
if ($env:PYTHONPATH) {
    $env:PYTHONPATH = "$SourceRoot$separator$env:PYTHONPATH"
} else {
    $env:PYTHONPATH = $SourceRoot
}

Set-Location $CodeRoot
python -m customer_agent
