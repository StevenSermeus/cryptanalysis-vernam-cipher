from .sanitize import sanitize
from parsing import str_to_bytes
def encrypt(in_text:str, out_file_path:str, key: str):
    text_sanitized = sanitize(in_text)
    print(f'Encrypting {text_sanitized} with key {key} to {out_file_path}')
    in_bytes = str_to_bytes(text_sanitized)
    key_bytes =str_to_bytes(key)
    key_bytes_padding = key_bytes * (len(in_bytes) // len(key_bytes)) + key_bytes[:len(in_bytes) % len(key_bytes)]
    out_bytes = bytes([a ^ b for a, b in zip(in_bytes, key_bytes_padding)])
    with open(out_file_path, "wb") as f:
        f.write(out_bytes)
