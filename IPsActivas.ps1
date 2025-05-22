# Obtener todas las conexiones de red activas
$connections = Get-NetTCPConnection | Select-Object -ExpandProperty RemoteAddress

# Filtrar para eliminar valores vacíos y evitar repetir IPs
$uniqueIPs = $connections | Where-Object { $_ -match "\d+\.\d+\.\d+\.\d+" } | Sort-Object -Unique

# Imprimir la lista de IPs establecidas
Write-Host "Lista de IPs conectadas al equipo:" $uniqueIPs 

# Opcional: Guardar la lista en un archivo de texto
$uniqueIPs | Out-File -FilePath "ConexionesIPs.txt"

Write-Host "El listado de IPs también ha sido guardado en 'ConexionesIPs.txt'"