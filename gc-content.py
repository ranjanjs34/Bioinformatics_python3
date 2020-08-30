#!/usr/bin/python3"
import Bio
from Bio.Seq import Seq



dna1=Seq("ATGACGACCAGTGACGATGACGTTTGACCAGAT")
dna2=Seq("GGGACCAGACCAGATGACCAGATGACAGATGACAGACAGAT")






#Method 1: manual calculation of the gc percentage
gc_dna= dna1.count('G')+dna1.count('C')
dna1_len=len(dna1)
gc_per=(gc_dna/dna1_len)*100
print("The GC-Content in percentage :", gc_per, "%")






#Method 2: calculation of the ngc percentage using function
def gc_content(x):
	gc_dna= x.count('G')+x.count('C')
	dna_len=len(x)
	gc_per=(gc_dna/dna_len)*100
	return gc_per
print("The GC percentage using Self-Defined function:", gc_content(dna1),"%")






#Method 3: calculation of GC percentage using Bio python module
from Bio.SeqUtils import GC
gc=GC(dna1)
print("GC % in Bio Python:", gc,"%")






#Suppose we want the GC percent in rounded form 
#Method 1
print("GC % in Bio Python but in rounded form:", format(gc,".2n"), "%")
#Method 2
print("GC % in Bio Python but in rounded form:", round(gc), "%")





#Suppose you want this GC percentage in two decimal places and there are  various methods to do that 
#Method 1
print("The GC percentage using Self-Defined function upt two decimal places:", format(gc_content(dna1),".2f"),"%")
#Method  2
print("GC % in Bio Python but in upto two decima places:", round(gc, 2), "%")