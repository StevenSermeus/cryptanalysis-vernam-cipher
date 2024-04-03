from functools import reduce
from math import gcd
import decrypt
import time
def attack(file_in_path : str, out_file_path: str, most_frequent_letter: str = "e", ngram_size: int = 3, depth: int = 3):
    start = time.time()
    file_in = open(file_in_path, "rb")
    data = file_in.read(depth * 1024)
    file_in.close()
    ngram_positions = {}
    ngram_count = {}

    for i in range(len(data) - ngram_size):
        ngram = data[i:i+ngram_size]

        if str(ngram) in ngram_count:
            ngram_count[str(ngram)] += 1
            ngram_positions[str(ngram)].append(i)
        else:
            ngram_count[str(ngram)] = 1
            ngram_positions[str(ngram)] = [i]

    most_frequent_ngram = max(ngram_count, key=ngram_count.get)
    ngram_distance = []
    for i in range(len(ngram_positions[most_frequent_ngram]) - 1):
        ngram_distance.append(ngram_positions[most_frequent_ngram][i+1] - ngram_positions[most_frequent_ngram][i])

    sub_arrays_distance = []
    for i in range(len(ngram_distance) - 10):
        sub_array = ngram_distance[i:i+10]
        sub_arrays_distance.append(sub_array)
    
    arrays_gcd = []

    for sub_array in sub_arrays_distance:
        arrays_gcd.append(reduce(gcd, sub_array))

    key_length = max(set(arrays_gcd), key=arrays_gcd.count)

    text_subarrays = [[] for i in range(key_length)]


    for i in range(0,len(data) -key_length ,key_length):
        for j in range(key_length):
            text_subarrays[j].append(data[i + j])
    most_frequent = []

    for subarray in text_subarrays:
        most_frequent.append(max(set(subarray), key = subarray.count))
    key = ''.join(chr(m ^ ord(most_frequent_letter)) for m in most_frequent)

    print("Key: ", key)
    time_taken_ms = ((time.time() - start) / 1000)
    print("Time taken: ", time_taken_ms, "ms")
    text = open(file_in_path, "rb").read()
    start_decrypt = time.time()
    decrypt.decrypt(text, out_file_path, key)
    
