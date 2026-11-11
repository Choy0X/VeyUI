# Thin wrapper: installs veyUI for your coding agents. Pass any install.py option.
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$py = Get-Command py -ErrorAction SilentlyContinue
if ($py) { & py -3 (Join-Path $here 'install.py') @args; exit $LASTEXITCODE }
$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) { & python (Join-Path $here 'install.py') @args; exit $LASTEXITCODE }
Write-Error 'Python 3.10+ is required. Install it, or run: npx skills add Choy0X/VeyUI'
exit 1
