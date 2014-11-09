def ReverseComplementPattern(Pattern):
    '''This proceduer returns a complementary sting in reverse order for the
    given string sequence'''
    gene_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse = ''
    for letter in Pattern:
        reverse = gene_dict[letter] + reverse
    return reverse
    