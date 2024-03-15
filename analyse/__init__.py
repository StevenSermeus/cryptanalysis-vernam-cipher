from .kasiski import Hasakey
from decrypt import decrypt
def attack(text_in: bytes, out_file_path: str, most_frequent_letter: str = "e", ngram_size: int = 3, depht: int = 3):
    h = Hasakey(text_in, ngram_size=ngram_size)
    key_length = h.get_key_length(depht=depht)
    print(f"Key length: {key_length}")
    text_subarrays = [[] for i in range(key_length)]
    for i in range(0,len(text_in) -1 ,key_length):
        for j in range(key_length):
            text_subarrays[j].append(text_in[i + j])
    most_frequent = []
    for subarray in text_subarrays:
        most_frequent.append(max(set(subarray), key = subarray.count))
    key = ''.join(chr(m ^ ord(most_frequent_letter)) for m in most_frequent)
    print(f"Key: {key}")
    decrypt(text_in, out_file_path, key)
    print(f"Decrypted text saved to {out_file_path}")
    