def to_rna(dna_strand):
    rna = [nuc for nuc in dna_strand.replace("A", "U").replace("T", "A")]
    for i in range(len(rna)):
        if (rna[i] == 'G'):
            rna[i] = 'C'
        elif (rna[i] == 'C'):
            rna[i] = 'G'
    return ''.join(rna)
