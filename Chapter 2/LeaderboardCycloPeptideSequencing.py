import Expand as exp, CyclopeptideScore as cs, Trim

def LeaderboardCycloPeptideSequencing(Spectrum, N, AminoMassesList):
    '''With a given experimental spectrum, find any winning peptide that has
    closest match with spectrum; N is maximal allowed mismatches between
    spectrums'''
    
    Leaderboard = [0]
    LeaderPeptide = [0]
    pmass = max(Spectrum)
    lead_score = cs.NumCyclopeptideScore(LeaderPeptide, Spectrum)
    
    while (len(Leaderboard) > 0):
        Leaderboard = exp.Expand(Leaderboard, AminoMassesList)
        work_board = Leaderboard + []
        
        for Peptide in Leaderboard:
            sump = sum(Peptide)

            if sump == pmass:
                pept_score = cs.NumCyclopeptideScore(Peptide, Spectrum)
                if pept_score > lead_score:
                    LeaderPeptide = Peptide + []
                    lead_score = pept_score

                work_board.remove(Peptide)
            else:
                if sump > pmass:
                    work_board.remove(Peptide)
       
        Leaderboard = Trim.NumTrim(work_board, Spectrum, N)

    return LeaderPeptide