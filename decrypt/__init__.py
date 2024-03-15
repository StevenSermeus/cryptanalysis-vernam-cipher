from parsing import str_to_bytes

def decrypt(in_text:bytes, out_file_path:str, key: str):
    key_pad = key * (len(in_text) // len(key)) + key[:len(in_text) % len(key)]
    decrypted_text = ''.join(chr(c ^ k) for c, k in zip(in_text, str_to_bytes(key_pad)))
    with open(out_file_path, "w") as f:
        f.write(decrypted_text)
        