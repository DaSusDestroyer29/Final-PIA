param(
    [string]$FolderPath
)

# Solicitar al usuario que la introduzca si no se proporciona
if (-not $FolderPath) {
    $FolderPath = Read-Host "Por favor, introduzca la ruta de la carpeta que desea listar"
}

# Verificar si la carpeta existe
if (-Not (Test-Path -Path $FolderPath -PathType Container)) {
    Write-Host "La carpeta especificada no existe. Por favor, verifique la ruta." -ForegroundColor Red
    return
}

# Obtener los archivos de la carpeta especificada, incluidos los ocultos
$files = Get-ChildItem -Path $FolderPath -File -Force

# Listar archivos
if ($files) {
    $files | ForEach-Object {
        if ($_.Attributes -match "Hidden") {
            Write-Host "[Oculto] $($_.FullName)" -ForegroundColor Yellow
        } else {
            Write-Host "$($_.FullName)" -ForegroundColor Green
        }
    }
} else {
    Write-Host "No se encontraron archivos en la carpeta especificada." -ForegroundColor Yellow
}
