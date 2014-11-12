import Expand as exp, GetNumPeptideMass as gm, NumCyclopeptideScore as csc, \
NumTrim as nt

def LeaderboardCycloPeptideSequencing(Spectrum, N, dict_18):
    '''With a given experimental spectrum, find any winning peptide that has
    closest match with spectrum; N is maximal allowed mismatches;
    mass_dictionary is 20-elem dict'''
    
    Leaderboard = [0]
    LeaderPeptide = [0]
    pmass = max(Spectrum)
    spec_len = 1
    
    while (len(Leaderboard) > 0) and (spec_len < len(Spectrum)):
        Leaderboard = exp.Expand(Leaderboard, dict_18)
        spec_len = len(Leaderboard[0]) * (len(Leaderboard[0]) - 1) + 1

        for Peptide in Leaderboard:
            if gm.GetNumPeptideMass(Peptide) == pmass:
                pept_score = csc.NumCyclopeptideScore(Peptide, Spectrum)
                lead_score = csc.NumCyclopeptideScore(LeaderPeptide, Spectrum)
                if pept_score > lead_score:
                    LeaderPeptide = Peptide + []
                    Leaderboard.remove(Peptide)
            elif gm.GetNumPeptideMass(Peptide) > pmass:
                Leaderboard.remove(Peptide)
            
        Leaderboard = nt.NumTrim(Leaderboard, Spectrum, N)
        
 
    return LeaderPeptide