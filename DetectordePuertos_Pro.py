import socket
from concurrent.futures import ThreadPoolExecutor

ip = input("Ingresa la dirección IP: ")

def escanear_puerto(puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((ip, puerto))
        
        if resultado == 0:
            print(f"Puerto abierto: {puerto}")
        
        sock.close()
    except:
        pass

# Número de hilos (puedes ajustar esto)
hilos = 100

print(f"\nEscaneando {ip}...\n")

with ThreadPoolExecutor(max_workers=hilos) as executor:
    executor.map(escanear_puerto, range(1, 65536))

print("\nEscaneo terminado.")