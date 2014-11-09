def GeneProteins(RNA, GenCode):
    '''Taking whole gene RNA, return all peptides separated with stop codons'''
    Peptides = []
    peptide = ''
    
    for i in range(0, len(RNA) - 2, 3):
        codon = RNA[i: i + 3]
        amino_acid = GenCode[codon]
        if amino_acid == '':
            Peptides.append(peptide)
            peptide = ''
        else:
            peptide = peptide + amino_acid
    
    if peptide <> '':
        Peptides.append(peptide)
    return Peptides