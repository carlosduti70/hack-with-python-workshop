import hashlib


def generarHash(h):
    digest = h.hexdigest()
    return digest


def hash_file(algorithm, file_path):
    h = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h


x = 0
while x < 1:
    print("Elige el numero de algoritmo:")
    print("1. SHA256")
    print("2. SHA512")
    print("3. MD5")
    print("4. Acabar el programa")

    nAlgoritmo = int(input())

    if nAlgoritmo != 4:
        print("Introduce el nombre del archivo:")
        archivo = input()

        if nAlgoritmo == 1:
            algoritmo = "sha256"
        elif nAlgoritmo == 2:
            algoritmo = "sha512"
        elif nAlgoritmo == 3:
            algoritmo = "md5"

        h = hash_file(algoritmo, archivo)
        hash1 = generarHash(h)
        print()
        print(hash1)
        print()
        x = 0

        with open('Hashes.txt', 'a') as file:
            file.write(f"> Nombre del archivo: {archivo}\n")
            file.write(f"Hash creado con {algoritmo}: {hash1}\n")

    else:
        x = 1
print("FIN")