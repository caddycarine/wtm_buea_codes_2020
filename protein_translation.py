def proteins(strand):
    codonProteins = {
        "AUG" : "Methionine",
        "UUU" : "Phenylalanine",
        "UUC" : "Phenylalanine",
        "UUA" : "Leucine",
        "UUG" : "Leucine",
        "UCU" : "Serine",
        "UCC" : "Serine",
        "UCA" : "Serine",
        "UCG" : "Serine",
        "UAU" : "Tyrosine",
        "UAC" : "Tyrosine",
        "UGU" : "Cysteine",
        "UGC" : "Cysteine",
        "UGG" : "Tryptophan",
        "UAA" : "STOP",
        "UAG" : "STOP",
        "UGA" : "STOP",
    }
    protein = []
    for i in range(0, len(strand), 3):
        acid = codonProteins[strand[i:i+3]]
        if acid == 'STOP':
            break
        else:
            protein.append(acid)
    return protein
