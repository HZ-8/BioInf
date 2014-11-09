def GeneTranscribe(Text):
    rna = ''
    for letter in Text:
        if letter == 'T':
            rna = rna + 'U'
        else:
            rna = rna + letter
    return rna