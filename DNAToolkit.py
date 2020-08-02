# import collections
from structures import *
from collections import Counter

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C":0, "G":0, "T":0}
    for nuc in seq:
        tmpFreqDict[nuc]+=1
    return tmpFreqDict
    # return dict(collections.Counter(seq))

#transcription: process where DNA is transcribed
def transcription(seq):
    """DNA -> RNA Transription Replacing Thymine with Uracil"""
    return seq.replace("T", "U")

def reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine. Reversing newly generated string"""
    # return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

    #Pythonic approach A little bit faster solution
    mapping = str.maketrans('ATCG', 'TAGC') #no dictionary work
    return seq.translate(mapping)[::-1]

def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G'))/ len(seq) * 100)

def gc_content_subsec(seq, k=20):
    """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(
            round((subseq.count('C') + subseq.count('G')) / len(subseq) * 100))
    return res

def translate_seq(seq, init_pos=0):
    """Translation a DNA sequence into an aminoacid sequence"""
    return [DNA_Codons[seq[pos:pos+3]] for pos in range(init_pos, len(seq) -2, 3)]

def codon_usage(seq, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i+3]] == aminoacid:
            tmpList.append(seq[i:i+3])
    # if self.seq_type == "DNA":
    #     for i in range(0, len(self.seq) - 2, 3):
    #         if DNA_Codons[self.seq[i:i + 3]] == aminoacid:
    #             tmpList.append(self.seq[i:i + 3])
    #
    # elif self.seq_type == "RNA":
    #     for i in range(0, len(self.seq) - 2, 3):
    #         if RNA_Codons[self.seq[i:i + 3]] == aminoacid:
    #             tmpList.append(self.seq[i:i + 3])

    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict

def gen_reading_frames(seq):
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_complement(seq), 0))
    frames.append(translate_seq(reverse_complement(seq), 1))
    frames.append(translate_seq(reverse_complement(seq), 2))
    return frames
