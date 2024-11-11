function Invoke-WindowsDefenderScan {
    <#
    .SYNOPSIS
    Realiza un análisisde amenazas detectadas.

    .DESCRIPTION
    La función `Invoke-WindowsDefenderScan` inicia un análisis rápido del sistema utilizando Windows Defender y, una vez finalizado, obtiene los resultados de posibles amenazas detectadas. 
    También puede usarse para obtener solo los resultados de un análisis anterior si se especifica el parámetro `-ScanResultsOnly`.

    .PARAMETER ScanResultsOnly
    Si se proporciona este parámetro, la función no ejecuta un análisis, solo obtiene y muestra los resultados de un análisis anterior.

    .EXAMPLE
    Invoke-WindowsDefenderScan
    Esto ejecuta un análisis rápido de Windows Defender y muestra los resultados de las amenazas detectadas.

    .EXAMPLE
    Invoke-WindowsDefenderScan -ScanResultsOnly
    Esto muestra únicamente los resultados del último análisis de Windows Defender, sin realizar un nuevo análisis.

    .NOTES
    Esta función requiere que el script sea ejecutado con privilegios de administrador.
    #>

    param (
        [switch]$ScanResultsOnly
    )

    # Verificar permisos de administrador
    If (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
        Write-Host "Ejecuta el script como administrador"
        return
    }

    # Función interna para realizar un análisis rápido
    function Run-DefenderScan {
        Write-Host "Iniciando análisis rápido con Windows Defender..."
        Start-MpScan -ScanType QuickScan
        Write-Host "Análisis completado."
    }

    # Función interna para obtener los últimos resultados del análisis
    function Get-DefenderScanResults {
        Write-Host "Obteniendo resultados del análisis..."
        $scanResults = Get-MpThreatDetection
        if ($scanResults) {
            Write-Host "Se encontraron vulnerabilidades:"
            $scanResults | Format-Table ThreatName, Action, Resources -AutoSize
        } else {
            Write-Host "No se encontraron vulnerabilidades."
        }
    }

    # Si se especifica el parámetro -ScanResultsOnly, solo se obtienen los resultados
    if ($ScanResultsOnly) {
        Get-DefenderScanResults
    } else {
        # Ejecutar el análisis
        Run-DefenderScan
        # Obtener los resultados después del análisis
        Get-DefenderScanResults
    }
}
