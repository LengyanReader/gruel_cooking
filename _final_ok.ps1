$ErrorActionPreference = 'SilentlyContinue'
$r = 'C:\DA_Practice\cookbooks\gruel_cooking'
$proj = 'C:\DA_Practice\cookbooks\gruel_cooking\Language Stacking-Linguistic Weaving'
$web = 'C:\DA_Practice\cookbooks\gruel_cooking\Language Stacking-Linguistic Weaving\web'

Write-Output '=== 0) git toplevel ==='
git -C $r rev-parse --show-toplevel

Write-Output ''
Write-Output '=== 1) pytest (hy_py312 含 markdown+pytest) ==='
Push-Location -LiteralPath $web
conda run -n hy_py312 python -m pytest tests -q
Write-Output ("pytest_exit=" + $LASTEXITCODE)
Pop-Location

Write-Output ''
Write-Output '=== 2) staged name-status ==='
git -C $r diff --cached --name-status

Write-Output ''
Write-Output '=== 3) junk still staged? ==='
$j = git -C $r diff --cached --name-only | Select-String -Pattern '\.bak$|_tmp_classes|extract_classes|gruel_cooking\.py$'
if ($j) { $j } else { Write-Output 'clean' }

Write-Output ''
Write-Output '=== 4) secrets in staged (name-status already excludes content; do cached patch scan) ==='
$hits = git -C $r show --cached 2>$null | Select-String -Pattern 'BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9]{16}'
if ($hits) { $hits } else { Write-Output 'clean (0 hits)' }

Write-Output ''
Write-Output '=== 5) .bak untracked in docs? ==='
git -C $r status --short --untracked-files=all | Select-String -Pattern '\.bak|_tmp_classes|extract_classes'
