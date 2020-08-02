#Read data from the file (FASTA formatted file)
def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round(((seq.count('C') + seq.count('G'))/len(seq) * 100), 6)

FASTAFile = readFile("")
FASTADict = {}
FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

print(FASTADict)

RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

print(RESULTDict)

MaxGCKey = max(RESULTDict, key=RESULTDict.get)

print(f'{MaxGCKey}\n{RESULTDict[MaxGCKey]}')