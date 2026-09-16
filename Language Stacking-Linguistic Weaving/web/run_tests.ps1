# 学习库基础施设一键验收（Windows 主机）
# 用法: powershell -ExecutionPolicy Bypass -File "Language Stacking-Linguistic Weaving/web/run_tests.ps1"
$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$env:PYTHONIOENCODING = "utf-8"

$candidates = @(
    "$env:USERPROFILE\miniconda3\envs\hy_py312\python.exe",
    (conda env list 2>$null | Select-String "hy_py312" | ForEach-Object {
        ($_.Line -split '\s+') | Where-Object { $_ -and $_ -notmatch '^#' } | Select-Object -Last 1
    } | Where-Object { $_ } | Select-Object -First 1)
) | Where-Object { $_ }
$py = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $py) { Write-Error "找不到 hy_py312 python，请先 conda activate hy_py312"; exit 1 }

Push-Location $repo
try {
    Write-Host "[1/4] 知识源校验 + 站点构建 + sqlite 索引"
    & $py "Language Stacking-Linguistic Weaving/web/build_learning.py" --validate --db --check
    if ($LASTEXITCODE -ne 0) { throw "build/validate 失败 (exit $LASTEXITCODE)" }

    Write-Host "[2/4] neo4j 阶段二 cypher 导出"
    & $py "Language Stacking-Linguistic Weaving/web/export_neo4j.py"
    if ($LASTEXITCODE -ne 0) { throw "export_neo4j 失败 (exit $LASTEXITCODE)" }

    Write-Host "[3/4] pytest 测试套件"
    & $py -m pytest "Language Stacking-Linguistic Weaving/web/tests" -q
    if ($LASTEXITCODE -ne 0) { throw "pytest 失败 (exit $LASTEXITCODE)" }

    Write-Host "[4/4] 全部通过"
} finally {
    Pop-Location
}