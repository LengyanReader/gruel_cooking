$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = "utf-8"
$out = "C:\Users\data\AppData\Local\Temp\opencode\pytest_final_utf8.txt"
$findPy = Get-ChildItem "C:\Users\data\miniconda3\envs" -Directory | Where-Object { $_.Name -like "*hy_py*" } | ForEach-Object {
    $p = Join-Path $_.FullName "python.exe"
    if (Test-Path -LiteralPath $p) { $p }
} | Select-Object -First 1
if (-not $findPy) { "NO_PYTHON" | Out-File -LiteralPath $out -Encoding utf8; exit 1 }
$pyPath = $findPy
"USING_PY=$pyPath" | Out-File -LiteralPath $out -Encoding utf8
$testDir = "C:\DA_Practice\cookbooks\gruel_cooking\Language Stacking-Linguistic Weaving\web\tests"
$repo = "C:\DA_Practice\cookbooks\gruel_cooking"
& $pyPath -m pytest $repo --rootdir $testDir -c "$testDir\pytest.ini" $testDir -p no:cacheprovider 2>&1 | Out-File -FilePath $out -Append -Encoding utf8
"PYTEST_EXIT=$LASTEXITCODE" | Out-File -LiteralPath $out -Append -Encoding utf8
