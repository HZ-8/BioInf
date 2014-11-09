def ProteinTranslation(Pattern, GenCode):
    '''Taking an RNA patern string, and genetic code, return a peptide'''
    Peptide = ''
    
    for i in range(0, len(Pattern) - 2, 3):
        codon = Pattern[i: i + 3]
        amino_acid = GenCode[codon]
        if amino_acid == '':
            return Peptide
        Peptide = Peptide + amino_acid

    return Peptide