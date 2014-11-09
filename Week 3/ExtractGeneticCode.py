def ExtractGeneticCode(fname = 'RNA_codon_table_1.txt'):
    ''' Takes a file with genetic code and returns a disctionary of codons as
    keys and apropriate amino acids as key values'''
    
    gen_code = {}
    
    f = open(fname, 'r')
    for line in f:
        code_pair = line.split()
        key = code_pair[0]
        if len(code_pair) == 2:
            value = code_pair[1]
        else:
            value = ''
        gen_code[key] = value
  
    f.close()
    return gen_code