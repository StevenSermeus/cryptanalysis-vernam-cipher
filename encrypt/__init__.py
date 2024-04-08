from .sanitize import sanitize
from parsing import str_to_bytes, bytes_to_bin
import os
def encrypt(in_text:str, out_file_path:str, key: str):
    in_text = sanitize(in_text)
    key_pad = key * (len(in_text) // len(key)) + key[:len(in_text) % len(key)]
    cyphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(in_text, key_pad))
    if os.path.dirname(out_file_path):
        os.makedirs(os.path.dirname(out_file_path), exist_ok=True)
    with open(out_file_path, "w") as f:
        f.write(cyphertext)
