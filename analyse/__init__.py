from .kasiski import Hasakey
from decrypt import decrypt
def attack(text_in: bytes, out_file_path: str):
    h = Hasakey(text_in)
    key_length = h.get_key_length()
    text_subarrays = [[] for i in range(key_length)]
    for i in range(0,len(text_in) -1 ,key_length):
        for j in range(key_length):
            text_subarrays[j].append(text_in[i + j])
   # in the subarrays find the most frequent int
    most_frequent = []
    for subarray in text_subarrays:
        most_frequent.append(max(set(subarray), key = subarray.count))
    e = 101
    key = ''.join(chr(m ^ e) for m in most_frequent)
    decrypt(text_in, out_file_path, key)
    