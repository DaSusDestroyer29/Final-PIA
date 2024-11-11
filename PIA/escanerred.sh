#!/bin/bash
 
#Nombre de la red
get_network_name() {
    ssid=$(iwgetid -r)
    echo "Nombre de la red (SSID): $ssid"
}
#PAquetes
get_consumed_packets() {
    echo "Paquetes consumidos por la interfaz de red:"
    ifconfig | grep -A 7 'flags' | grep 'RX packets\|TX packets'
}
#IP
view_ip_address() {
    echo "Direccion IP:"
    ip addr show | grep 'inet ' | grep -v '127.0.0.1'
}
#Equipos en red
view_connected_devices() {
    echo "Equipos conectados a la red local:"
    arp -a
}
#Reporte .txt
create_report() {
    {
        echo "=== Reporte de Escaneo de Red ==="
        echo "Nombre de la red (SSID): $(iwgetid -r)"
        echo ""
        echo "Paquetes consumidos por la interfaz de red:"
        ifconfig | grep -A 7 'flags' | grep 'RX packets\|TX packets'
        echo ""
        echo "Dirección IP:"
        ip addr show | grep 'inet ' | grep -v '127.0.0.1'
        echo ""
        echo "Equipos conectados a la red local:"
        arp -a
    } > escaner_de_red.txt
    echo "Reporte generado: escaner_de_red.txt"
}
#menu
display_menu() {
    echo "Seleccione una opcion:"
    echo "1) Ver nombre de la red (SSID)"
    echo "2) Ver paquetes consumidos"
    echo "3) Ver direccion IP"
    echo "4) Ver equipos conectados a la red"
    echo "5) Generar reporte .txt"
    echo "6) Salir"
}
#ciclo
option=0
while [ $option -ne 6 ]; do
    display_menu
    read -p "Ingrese su opcion: " option
    case $option in
        1)
            get_network_name
            ;;
        2)
            get_consumed_packets
            ;;
        3)
            view_ip_address
            ;;
        4)
            view_connected_devices
            ;;
        5)
            create_report
            ;;
        6)
            echo "Saliendo..."
            ;;
        *)
            echo "Opcion no válida. Inténtelo de nuevo."
            ;;
    esac
    echo ""
done
