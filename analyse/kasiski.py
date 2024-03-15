from functools import reduce
from math import gcd
from parsing import bytes_to_str, bytes_to_bin
class Hasakey:

  def __init__(self, text: bytes, ngram_size=2):
    self.text = text
    self.ngram_size = ngram_size
    print("""
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠤⠀⠒⠒⠂⠐⠒⢢⡦⠆⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠋⢰⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⢑⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠈⠂⠀⠀⠀⠀⠀⠀⠀⢀⠀⡺⠁⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⡠⠲⠛⠈⠙⠹⠳⡆⠂⠀⠀⠂⢒⡩⠓⠈⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⢰⠁⢀⡀⢀⣤⣄⡀⢈⡗⠒⠬⠙⠧⠴⠋⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⣣⣡⡭⠉⠀⡸⡇⡀⠀⣱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⣿⠣⠌⠁⠈⠄⠌⣷⠠⠅⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠙⢢⡤⡂⡠⠤⣰⡁⡓⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⡔⢓⢄⢖⢙⡿⢀⡾⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⢰⡫⢑⢥⠖⢣⠗⠁⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠰⣤⣮⣥⠤⣼⣷⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠿⠷⢿⠟⠷⣝⢏⣽⡶⠶⠶⠶⠶⠶⠶⠶⢶⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⢸⠑⢠⠣⠦⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢾⢽⢶⣟⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢾⢼⢺⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠘⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)

    
  def get_key_length(self, depht=3):
    ngrams = self._ngram_separation()
    ngrams_frequencies = self._ngram_frequency(ngrams_positions=ngrams)
    depht_ngrams = self._get_most_frequent_ngrams(ngrams_frequencies,ngrams,depht)
    ngrams_distances = self._ngram_distances(depht_ngrams)
    return self._ngram_gcd(ngrams_distances=ngrams_distances)
    return self.key_length
  
  def _get_most_frequent_ngrams(self, ngrams_frequencies, ngrams,depht=3):
    ngrams_frequencies = sorted(ngrams_frequencies.items(), key=lambda x: x[1], reverse=True)
    ngrams_frequencies = ngrams_frequencies[:depht]
    ngrams = {k: v for k, v in ngrams.items() if k in [n[0] for n in ngrams_frequencies]}
    return ngrams


  def _ngram_separation(self):
    ngrams = {}
    for i in range(len(self.text) - self.ngram_size + 1):
      sequence = self.text[i:i + self.ngram_size]
      if sequence in ngrams:
        ngrams[sequence].append(i)
      else:
        ngrams[sequence] = [i]
    return ngrams

  def _ngram_frequency(self, ngrams_positions):
    frequencies = {}
    for k, v in ngrams_positions.items():
      frequencies[k] = len(v)
    return frequencies

  def _ngram_distances(self, ngrams_positions):
    distances = {}
    for k, v in ngrams_positions.items():
      distances[k] = [v[i+1] - v[i] for i in range(len(v)-1)]
    return distances

  def _ngram_gcd(self, ngrams_distances):
    #merge the 3 top distances list into one list
    distances = []
    for k, v in ngrams_distances.items():
      distances += v
    distances = [d for d in distances if d != 1]
    distances = [distances[i:i+10] for i in range(0, len(distances), 10)]
    distances_gcd = []
    for i in range(len(distances)):
      distances_gcd.append(reduce(gcd, distances[i]))
    if all(d == 1 for d in distances_gcd):
      return 1
    else:
      distances_gcd = [d for d in distances_gcd if d != 1]
      return max(set(distances_gcd), key = distances_gcd.count)
    