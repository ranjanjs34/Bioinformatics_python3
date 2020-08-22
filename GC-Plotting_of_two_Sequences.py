import matplotlib
import matplotlib.pyplot as plt
import Bio
from Bio.Seq import Seq
from collections import Counter
dna=Seq('ATGCATGACAG')
freq=Counter(dna)
print (freq)
plt.bar(freq.keys(), freq.values())
plt.show()
