$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$py = 'C:\Users\data\miniconda3\envs\hy_py312\python.exe'
$env:LH_PORT = if ($env:LH_PORT) { $env:LH_PORT } else { '18080' }
$port = $env:LH_PORT

$existing = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "port ${port} already in use (PID $($existing[0].OwningProcess)); skipping launch"
    exit 0
}

$cmd = "cmd.exe /c set PYTHONIOENCODING=utf-8&& set LH_PORT=$port&& `"$py`" -m app.main"
$r = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{
    CommandLine = $cmd
    CurrentDirectory = $root
}
if ($r.ReturnValue -eq 0) {
    Write-Host "server launched on http://127.0.0.1:$port  (PID $($r.ProcessId))"
} else {
    Write-Host "launch failed, WMI return $($r.ReturnValue)"
    exit 1
}