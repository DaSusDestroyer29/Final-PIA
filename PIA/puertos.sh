#!/bin/bash
local_ip=$(hostname -I | awk '{print $1}')
# Función para escanear puertos
scan_port() {
    local ip="$1"
    local port="$2"
    local report_file="$3"
    if nc -zv -w 1 "$ip" "$port" 2>&1 | grep succeeded; then
        result="Exito"
    else
        result="Fallido"
    fi
    echo "Puerto $port: $result"   
    # Generar reporte
    if [[ -n "$report_file" ]]; then
        echo "Puerto $port: $result" >> "$report_file"
    fi
}
# Bucle
while true; do
    read -p "Introduce la direccion IP a escanear (presiona Enter para usar la IP local [$local_ip]): " ip
    ip=${ip:-$local_ip}
    # Contador
    port_count=0
    report_file="reporte.txt"
    # Escribir el reporte
    {
        echo "Reporte del escaneo:"
        echo "Dirección IP: $ip"
        echo "Fecha y hora: $(date)"
        echo ""
    } > "$report_file"
    while [[ $port_count -lt 3 ]]; do
        read -p "Introduce el puerto a escanear (o 'fin' para terminar): " port
        if [[ "$port" == "fin" ]]; then
            break
        fi
        # Escaneo de un puerto
        scan_port "$ip" "$port" "$report_file"
        ((port_count++))
    done
    #reporte
    read -p "¿Quieres crear un reporte del escaneo? (s/n): " create_report
    if [[ "$create_report" =~ ^[sS]$ ]]; then
        echo "Reporte guardado en $report_file"
    else
        rm -f "$report_file"
        echo "No se genero el reporte."
    fi
    #repetir el script
    read -p "¿Quieres repetir el escaneo? (s/n): " repeat
    if [[ ! "$repeat" =~ ^[sS]$ ]]; then
        echo "Saliendo..."
        break
    fi
done
