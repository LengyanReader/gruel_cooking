$root = 'C:\DA_Practice\cookbooks\gruel_cooking'
$wd   = 'C:\DA_Practice\cookbooks\gruel_cooking\Language Stacking-Linguistic Weaving\web'

$py = $null
try {
    $py = conda run -n hy_py312 which python 2>$null | Select-Object -Last 1
} catch { }
if (-not $py -or -not (Test-Path -LiteralPath $py)) { $py = 'C:\DA_Practice\cookbooks\gruel_cooking\...' }
Write-Output "conda_python=$py"

Write-Output ''
Write-Output '=== pytest (web dir, hy_py312) ==='
Push-Location -LiteralPath $wd
try {
    & conda run -n hy_py312 python -m pytest tests -q 2>&1
    Write-Output "pytest_exit=$LASTEXITCODE"
} finally {
    Pop-Location
}

Write-Output ''
Write-Output '=== git status --short (repo root) ==='
git -C $root status --short --untracked-files=all

Write-Output ''
Write-Output '=== staged files (diff --cached --name-only) ==='
git -C $root diff --cached --name-only

Write-Output ''
Write-Output '=== junk staged? scan report ==='
$junk = git -C $root diff --cached --name-only | Select-String -Pattern '\.bak$|_tmp_class|extract_class|index\.html\.bak|_pycache_'
if ($junk) { Write-Output 'JUNK STAGED:'; $junk | ForEach-Object { $_.Line } } else { Write-Output 'clean' }
