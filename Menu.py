#Modulos
import platform #Modulo para filtrar So
import subprocess #Modulo para ejecutar powershell
import json
from encriptar import generate_key, generate_iv,encrypt_file #Encriptar
from generador import generar_contrasena #Generador
from AbuseIPDB import buscar_datos #Data Abuse
import os 
from sh import buscar_shodan #Shodan
from DecBin import decimal_binario, texto_binario #Binario
from datetime import datetime #Fehca 
import platform #SO
def detectar_so():
    sistema=platform.system()
    if sistema=="Windows":
        return "El sistema operativo es Windows"
    elif sistema=="Linux":
        return "El sistema operativo es Linux"
    elif sistema=="Darwin":
        return "El sistema operativo es macOs"
    else:
        return "Desconocido"

def limpiar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')
#Menu
while True:
    print("=====MENU=====")
    print("1)API SHODAN") #Yo
    print("2)API-DATA ABUSE")#Uriel 
    print("3)Generador de contraseñas") #Yo
    print("4)Encriptar Archivo") #Yo
    print("5)Codificador de binario") #Angel
    print("6)SALIR")
    print("7)Limpiar pantalla")
    print("8)Menu Powershell")
    print("9)Menu Bash")
    opcion=int(input("Ingresa una opcion:\n"))
    if opcion == 1:
        print("SHODAN")
        api_key=input("Ingresa tu api key aqui: \n")
        xd=buscar_shodan(api_key)

    elif opcion == 2:
        print("Data Abuse")
        api_key=input("INgresa la apikey de data abuse aqui:\n")
        ip_address=input("Ingresa la direccion ip:\n")
        buscar_datos(api_key,ip_address)
        
    elif opcion == 3:
        print("Generar contraseñas")
        contrasena_generada= generar_contrasena()
        print(f"La contraseña generada es: {contrasena_generada}")

    elif opcion == 4:
        print("Encriptar archivos")
        file_path = input("Ingresa la ruta del archivo que deseas encriptar:\n")
        key = generate_key()  
        iv = generate_iv()
        encrypt_file(file_path, key, iv)
        with open("clave.key", "wb") as key_file:
            key_file.write(key)
        print("Clave guardada en clave.key")

    elif opcion == 5:
        print("Codificador de binario")
        entrada=input("Ingresa el texto a convertir (Nuemros/texto):\n")
        if entrada.lstrip('-').isdigit():
            numero_decimal=int(entrada)
            binario=decimal_binario(numero_decimal)
            print(f"El numero {numero_decimal} en binario es: {binario}")
        else:
            binario=texto_binario(entrada)
            print(f"El texto '{entrada}' en binario es: {binario}")

    elif opcion == 6:
        exit()
    elif opcion == 7:
        limpiar_pantalla()
    elif opcion == 8:
        while True:
            print("Ejecutando powershell")
            print("Menu Powershell")
            print("1)Recursos")
            print("2)Escaneo sistema con windows defender")
            print("3)Hashes de archivos")
            print("4)Archivos ocultos")
            print("5)Menu principal")
            powerinput=int(input("Ingresa una opcion aqui: \n"))

            if powerinput == 1:#ASA
                print("Recursos")
                generar_reporte=input("Generar reporte s/n:\n").strip().lower() #Reporte s/n 
                try:
                    if generar_reporte == "s":
                        with open("recursos.txt", "w") as f:
                            fecha_actual=datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Importar fecha
                            f.write(f"Reporte de recursos - Fecha: {fecha_actual}\n") #Agregar fecha al reporte
                            f.write("="*40+"\n\n") #Lineas de separacion
                            result=subprocess.run([
                                "powershell", "-ExecutionPolicy", "Bypass", "-command",
                                "Import-Module ./Recursos.psm1; Get-SystemResources"
                            ], shell=True, stdout=f)
                        print("Reporte generado y llamado: Recursos.txt")
                    else:
                        result=subprocess.run([
                                "powershell", "-ExecutionPolicy", "Bypass", "-command",
                                "Import-Module ./Recursos.psm1; Get-SystemResources"
                            ], shell=True)
                    if result.returncode !=0: #Verificar errores
                        print("Error al ejecutar powershell: ",result.stderr)
                except FileNotFoundError:
                    print("Archivo no encontrado")
                except Exception as e:
                    print("Error {e}")
#Para usar la funcion 2 se debe ejcutar como admin y se debe tener la defensa de windows y no otro antivirus

            elif powerinput == 2: #Angel Esau
                print("Escaneo de sistema con windows defender")
                generar_reporte=input("Generar reporte s/n:\n").strip().lower() #Reporte s/n 
                if generar_reporte == "s":
                    with open("defender.txt", "w") as f:
                        fecha_actual=datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Importar fecha
                        f.write(f"Reporte de escaneo con Windows Defender")
                        f.write(f"Fecha de ejecucion {fecha_actual}\n")
                        f.write("="*40+"\n\n") #Lineas de separacion
                        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-command", "Invoke-WindowsDefenderScan"], shell=True, stdout=f)
                    print("Reporte generado y llamado defender.txt")
                else:
                    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-command", "Invoke-WindowsDefenderScan"], shell=True)

            elif powerinput == 3:#ASA
                print("Hashes")
                def obtener_hashes(carpeta):
                    comando=[
                        "powershell",
                        "-ExecutionPolicy", "Bypass",
                        "-File",r"C:\Users\angel\OneDrive\Desktop\Le facultad\3 Semestre\Programacion\Python\PIA3E\Get-FileHashes.ps1",
                        "-FolderPath", carpeta
                    ]
                    try:
                        resultado=subprocess.run(comando, capture_output=True, text=True, check=True)
                        print("Resultado powershell:",resultado.stdout)
                        hashes=json.loads(resultado.stdout)
                        if isinstance(hashes, dict):
                            hashes=[hashes]
                        return hashes
                    except subprocess.CalledProcessError as e:
                        print("Error al ejecutar powershell:",e.stderr)
                        return None
                        
                def guardar_reporte(hashes):
                    fecha_actual=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    nombre_reporte="Reporte_Hashes.txt"
                    with open(nombre_reporte, "w") as reporte:
                        reporte.write(f"Fecha y hora: {fecha_actual}\n")
                        reporte.write("Hashes de archivos\n\n")
                        for archivo in hashes:
                            reporte.write(f"Archivo: {archivo['FilePath']}, Hash: {archivo['Hash']}\n")
                    print(f"Reporte generado y llamado {nombre_reporte}")
                carpeta=input("Ingresa la ruta de la carpeta a monitorear:\n")
                hashes=obtener_hashes(carpeta)
                if hashes is not None:
                    generar_reporte=input("Desea generar un reporte txt?s/n:\n").strip().lower()
                    if generar_reporte=="s":
                        guardar_reporte(hashes)
                    else:
                        for archivo in hashes:
                            print(f"Archivo: {archivo['FilePath']}, Hash: {archivo['Hash']}")

            elif powerinput == 4:#Uriel
                print("Archivos ocultos") 
                def generar_reporte(contenido):
                    fecha_actual = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                    nombre_reporte = f"ReporteArchivosOcultos.txt"
                    try:
                        with open(nombre_reporte, "w") as reporte:
                            reporte.write(f"Fecha y hora: {fecha_actual}\n")
                            reporte.write("Reporte de resultados:\n\n")
                            reporte.write(contenido) 
                        print(f"Reporte generado exitosamente y guardado como {nombre_reporte}")
                    except Exception as e:
                        print(f"Error al generar reporte {e}")
                
                def ejecutar_ps1(folder_path=None):
                    #Directorio powrshell
                    ps_path=r"c:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
                    command=[
                        ps_path,
                        "-ExecutionPolicy", "Bypass",
                        "-File", r"C:\Users\angel\OneDrive\Desktop\Le facultad\3 Semestre\Programacion\Python\PIA3E\GetHiddenFiles.ps1",
                        folder_path]
                    try:
                        result=subprocess.run(command, shell=True, capture_output=True, text=True)
                        if result.returncode !=0:
                            print("Error al ejecutar powershell: {result.stderr}")
                            return result.stderr
                        else:
                            print(result.stderr)
                            return result.stdout
                    except Exception as e:
                        print(f"Ocurrió un error al intentar ejecutar el script: {e}")
                        return str(e)  
                folder_path = input("Ingresa la ruta de la carpeta a monitorear:\n")
                resultado = ejecutar_ps1(folder_path)
                if resultado is not None:
                    generar_reportes_resultado = input("¿Quieres generar un reporte con los resultados? (si/no): ").strip().lower()
                    if generar_reportes_resultado == "si":
                        generar_reporte(resultado)

            elif powerinput == 5:
                print("Saliendo...")
                break
            else:
                print("Ingresa una opcion valida")
    elif opcion == 9:
        print("MENU BASH")
        print(detectar_so())
        print("Bash no es ejecutable desde Windows; Intentar desde bash")
    else:
        print("Ingresa una opcion valida!!")