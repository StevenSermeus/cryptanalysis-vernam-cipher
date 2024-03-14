def str_to_bytes(s:str) -> bytes:
    return s.encode('ascii')

def bytes_to_str(b:bytes) -> str:
    return b.decode('ascii')

def bytes_to_bin(b:bytes) -> str:
    binary_int = int.from_bytes(b, "big")
    return bin(binary_int)