#importing Ploting modules
import matplotlib
import matplotlib.pyplot as plt
#importing BioPython
import Bio
from Bio.Seq import Seq

dna1=Seq("ATGCAAGGACGATACGATTAGAC")

dna2=Seq("AAATGGCCCCCCCCCGCTTCGCCCCCCCCCCTCGGCGCAAATAGCCCAGAGGACATTAG")

gc1=dna1.count('G')+dna1.count('C')

gc2=dna2.count('G')+dna2.count('C')

gcfreq= {'Seq1':gc1, 'Seq2':gc2} 

print (gcfreq)

plt.bar(gcfreq.keys(), gcfreq.values())
#it will show the GC plots in GTK3 window
plt.show()
