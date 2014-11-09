import PeptidePositions, GeneTranscribe, ReverseComplementPattern as rev,\
 GeneProteins as gp

def PeptideEncoding(Text, Peptide, GeneticCode):
    '''Given gene string Text, find all its substings which encode for 
    Peptide - complements as well'''
    code_strings = []
    
    rna = GeneTranscribe.GeneTranscribe(Text)
    for i in range(3):
        frame = rna[i:]
        proteins = gp.GeneProteins(frame, GeneticCode)
        
        pos_in_text = i
        for protein in proteins:
            positions = PeptidePositions.PeptidePositions(protein, Peptide)
            for pos in positions:
                start_pos = pos_in_text + pos * 3
                code_str = Text[start_pos: start_pos + len(Peptide) * 3]
                code_strings.append(code_str)
            pos_in_text = pos_in_text + len(protein)*3 + 3
    
    compl = rev.ReverseComplementPattern(Text)
    rna = GeneTranscribe.GeneTranscribe(compl)
    for i in range(3):
        frame = rna[i:]
        proteins = gp.GeneProteins(frame, GeneticCode)
       
        pos_in_text = i
        for protein in proteins:
            positions = PeptidePositions.PeptidePositions(protein, Peptide)
            for pos in positions:
                start_pos = pos_in_text + pos * 3
                text_pos = len(Text) - start_pos - len(Peptide) * 3
                code_str = Text[text_pos : text_pos + len(Peptide) * 3]
                code_strings.append(code_str)
            pos_in_text = pos_in_text + len(protein)*3 + 3
    return code_strings