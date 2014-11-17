def GeneTranscribe(Text):
    '''For gene Text, return its RNA'''
    rna = ''
    for letter in Text:
        if letter == 'T':
            rna = rna + 'U'
        else:
            rna = rna + letter
    return rna