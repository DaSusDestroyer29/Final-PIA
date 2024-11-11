def decimal_binario(decimal):
    if decimal >=0:
        return bin(decimal)[2:]
    else:
        return '-' +bin(decimal)[3:]
def texto_binario(texto):
    binario=''.join(format(ord(c), '08b') for c in texto)
    return binario
