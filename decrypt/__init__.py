from parsing import str_to_bytes
def decrypt(in_text:bytes, out_file_path:str, key: str):
    print(f'Decrypting {in_text} with key {key} to {out_file_path}')
    key_bytes = str_to_bytes(key)
    key_bytes_padding = key_bytes * (len(in_text) // len(key_bytes)) + key_bytes[:len(in_text) % len(key_bytes)]
    out_bytes = bytes([a ^ b for a, b in zip(in_text, key_bytes_padding)])
    with open(out_file_path, "wb") as f:
        f.write(out_bytes)