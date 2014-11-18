def AminoAcidMasses(fname = 'integer_mass_table.txt'):
    ''' Takes a file with masses of amino acids and returns a disctionary with
    amino acids as keys and apropriate masses as values'''
    
    aa_masses = {}
    
    f = open(fname, 'r')
    for line in f:
        if line == '\n' or line == '':
            continue

        mass_pair = line.split()
        key = mass_pair[0]
        value = mass_pair[1]
        aa_masses[key] = int(value)
  
    f.close()
    return aa_masses