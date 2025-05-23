# obtener_ips.ps1
$connections = Get-NetTCPConnection | Select-Object -ExpandProperty RemoteAddress
$uniqueIPs = $connections | Where-Object { $_ -match "\d+\.\d+\.\d+\.\d+" } | Sort-Object -Unique
$uniqueIPs

# Opcional: Guardar la lista en un archivo de texto
$uniqueIPs | Out-File -FilePath "ConexionesIPs.txt"

Write-Host "El listado de IPs también ha sido guardado en 'ConexionesIPs.txt'"
