from functools import reduce
from math import gcd
from parsing import bytes_to_str, bytes_to_bin
class Hasakey:

  def __init__(self, text: bytes):
    self.text = text
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

    
  def get_key_length(self):
    self._ngram_frequency()
    self._ngram_distances()
    self._ngram_gcd()
    return self.key_length
  def _ngram_separation(self, size=2):
    ngram = {}
    for i in range(len(self.text) - size + 1):
      sequence = self.text[i:i + size]
      if sequence in ngram:
        ngram[sequence].append(i)
      else:
        ngram[sequence] = [i]
    self.ngrams_positions = ngram

  def _ngram_frequency(self, size=2):
    self._ngram_separation(size=size)
    frequencies = {}
    for k, v in self.ngrams_positions.items():
      frequencies[k] = len(v)
    self.ngrams_frequencies = frequencies
    #print top10 in ascii bytes to ascii
    top3 = sorted(self.ngrams_frequencies.items(), key=lambda x: x[1], reverse=True)[:2]
    #get top3 positions from ngrams_positions
    top3_positions = {}
    for k, v in top3:
      top3_positions[k] = self.ngrams_positions[k]
    self.top3 = top3_positions  

  def _ngram_distances(self):
    distances = {}
    for k, v in self.top3.items():
      distances[k] = [v[i+1] - v[i] for i in range(len(v)-1)]
    self.top3_distances = distances

  def _ngram_gcd(self):
    #merge the 3 top distances list into one list
    distances = []
    for k, v in self.top3_distances.items():
      distances += v
    #remove all 1s
    distances = [d for d in distances if d != 1]
    #divide distances list into list of 10 elements
    distances = [distances[i:i+10] for i in range(0, len(distances), 10)]
    #get the gcd of each list
    distances_gcd = []
    for i in range(len(distances)):
      distances_gcd.append(reduce(gcd, distances[i]))
    if all(d == 1 for d in distances_gcd):
      self.key_length = 1
    else:
      #remove 1 from the list
      distances_gcd = [d for d in distances_gcd if d != 1]
      self.key_length = max(set(distances_gcd), key = distances_gcd.count)
    