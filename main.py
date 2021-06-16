# What is in DNA
Nucleotides = ["A", "C", "G", "T"]

# check the structure of DNA strand
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
         return False
    return tmpseq

# to count the nucleotides in a DNA sequence
def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict(nuc) +=1
    return tmpFreqDict

rndDNAStr="GGCCAATTT"

print(validateSeq(rndDNAStr))
print(countNucFrequency(rndDNAStr))
