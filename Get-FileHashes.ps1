param(
    [string]$FolderPath
)
#Verificar si la carpte existe
if (-Not (Test-Path -Path $FolderPath -PathType Container)) {
    Write-Output "Carpeta No existe"
    exit
}

#Obtener informacion de archivos
Get-ChildItem -Path $FolderPath -File | ForEach-Object {
    $filepath=$_.FullName
    $hash=(Get-FileHash -Path $filepath -Algorithm SHA256).Hash
    [PSCustomObject]@{
        FilePath=$filepath
        Hash=$hash
    }
} | ConvertTo-Json -Compress