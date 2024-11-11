function Get-SystemResources {
    param(
        [switch]$MostrarDetalles = $false
    )

    #RAM
    function Get-MemoryUsage {
        $memoria = Get-WmiObject Win32_OperatingSystem
        $memoriaTotal = [math]::Round($memoria.TotalVisibleMemorySize / 1MB, 2)
        $memoriaLibre = [math]::Round($memoria.FreePhysicalMemory / 1MB, 2)
        $memoriaUsada = [math]::Round($memoriaTotal - $memoriaLibre, 2)

        Write-Host "Memoria Total: $memoriaTotal MB"
        Write-Host "Memoria Libre: $memoriaLibre MB"
        Write-Host "Memoria Usada: $memoriaUsada MB"
    }

    #Disco Duro
    function Get-DiskUsage {
        $discos = Get-WmiObject Win32_LogicalDisk -Filter "DriveType=3" 
        foreach ($disco in $discos) {
            $espacioTotal = [math]::Round($disco.Size / 1GB, 2)
            $espacioLibre = [math]::Round($disco.FreeSpace / 1GB, 2)
            $espacioUsado = [math]::Round($espacioTotal - $espacioLibre, 2)
            
            Write-Host "Disco $($disco.DeviceID):"
            Write-Host "  Espacio Total: $espacioTotal GB"
            Write-Host "  Espacio Libre: $espacioLibre GB"
            Write-Host "  Espacio Usado: $espacioUsado GB"
        }
    }

    #CPU
    function Get-CPUUsage {
        $procesadores = Get-WmiObject Win32_Processor
        foreach ($procesador in $procesadores) {
            Write-Host "Procesador: $($procesador.Name)"
            Write-Host "  Carga Actual: $($procesador.LoadPercentage)%"
        }
    }

    #Red
    function Get-NetworkUsage {
        $interfaces = Get-WmiObject Win32_PerfFormattedData_Tcpip_NetworkInterface
        foreach ($interface in $interfaces) {
            $enviados = [math]::Round($interface.BytesSentPersec / 1KB, 2)
            $recibidos = [math]::Round($interface.BytesReceivedPersec / 1KB, 2)

            Write-Host "Interfaz de Red: $($interface.Name)"
            Write-Host "  Enviados: $enviados KB/s"
            Write-Host "  Recibidos: $recibidos KB/s"
        }
    }

    # Mostrar la información básica de los recursos del sistema
    Write-Host "--- Monitoreo de Recursos del Sistema ---"
    Get-MemoryUsage
    Get-DiskUsage
    Get-CPUUsage
    Get-NetworkUsage

    # Si se especifica el switch -MostrarDetalles, mostrar información adicional de procesos
    if ($MostrarDetalles) {
        Write-Host "n--- Detalles adicionales de los recursos del sistema ---"

        Write-Host "nMemoria Detallada (procesos que más consumen memoria):"
        Get-Process | Sort-Object WS -Descending | Select-Object -First 10 | Format-Table Name, @{Name="Memoria Usada (MB)"; Expression={[math]::Round($_.WorkingSet / 1MB, 2)}} -AutoSize
        
        Write-Host "nUso del CPU por proceso (procesos que más usan CPU):"
        Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 | Format-Table Name, @{Name="Uso CPU (s)"; Expression={[math]::Round($_.CPU, 2)}} -AutoSize
    }
}

# Ejecutar el monitoreo básico
Get-SystemResources