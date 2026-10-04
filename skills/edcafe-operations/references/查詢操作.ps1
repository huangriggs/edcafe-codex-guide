param([string]$關鍵字 = '')
$ErrorActionPreference = 'Stop'
$索引路徑 = Join-Path $PSScriptRoot '操作資料.json'
$索引資料 = Get-Content -LiteralPath $索引路徑 -Raw -Encoding UTF8 | ConvertFrom-Json
$結果 = @($索引資料.operations | Where-Object {
    [string]::IsNullOrWhiteSpace($關鍵字) -or
    (($_.id, $_.title, $_.keywords, $_.route, $_.status) -join ' ').IndexOf($關鍵字, [StringComparison]::OrdinalIgnoreCase) -ge 0
})
if ($結果.Count -eq 0) { Write-Output '沒有符合的操作；請改用較短的關鍵字。'; exit 0 }
$結果 | Select-Object @{Name='操作';Expression={$_.title}}, @{Name='路徑';Expression={$_.route}}, @{Name='驗證';Expression={$_.status}} | Format-Table -Wrap -AutoSize
