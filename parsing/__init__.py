def str_to_bytes(s:str) -> bytes:
    return s.encode('utf-8')

def bytes_to_str(b:bytes) -> str:
    return b.decode('utf-8')
