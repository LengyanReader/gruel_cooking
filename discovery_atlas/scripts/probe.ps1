# Discovery Atlas · reachability probe
# Usage:  pwsh -NoProfile -File scripts/probe.ps1 -Urls @('https://a.org/','https://b.fr/') [-Out out.txt]
# Method: HEAD first; on any failure retry GET (HEAD gives false ERR on some hosts,
# measured 2026-10-27 with gutenberg/ganjoor). 403/429 => bot-gated, NOT dead.
param(
  [Parameter(Mandatory = $true)][string[]]$Urls,
  [string]$Out = 'probe_result.txt'
)
$rows = @()
foreach ($u in $Urls) {
  $st = ''
  try { $r = Invoke-WebRequest -Uri $u -Method Head -TimeoutSec 9 -UseBasicParsing -ErrorAction Stop; $st = 'OK ' + $r.StatusCode }
  catch {
    if ($_.Exception.Response) { $st = 'FAIL ' + [int]$_.Exception.Response.StatusCode } else { $st = 'FAIL ERR' }
    try { $r2 = Invoke-WebRequest -Uri $u -Method Get -TimeoutSec 12 -UseBasicParsing -ErrorAction Stop; $st = 'OK-GET ' + $r2.StatusCode }
    catch { if ($_.Exception.Response) { $st += ' / GET ' + [int]$_.Exception.Response.StatusCode } else { $st += ' / GET ERR' } }
  }
  $rows += ($st + ' ' + $u)
}
$rows | Set-Content -Path $Out -Encoding UTF8
Write-Host "probed: $($rows.Count) -> $Out"
