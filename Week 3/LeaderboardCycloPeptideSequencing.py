import Expand as exp, NumCyclopeptideScore as csc, NumTrim as nt

def LeaderboardCycloPeptideSequencing(Spectrum, N, AminoMassesList):
    '''With a given experimental spectrum, find any winning peptide that has
    closest match with spectrum; N is maximal allowed mismatches between
    spectrums'''
    
    Leaderboard = [0]
    LeaderPeptide = [0]
    pmass = max(Spectrum)
    lead_score = csc.NumCyclopeptideScore(LeaderPeptide, Spectrum)
    
    while (len(Leaderboard) > 0):
        Leaderboard = exp.Expand(Leaderboard, AminoMassesList)
        work_board = Leaderboard + []
        
        for Peptide in Leaderboard:
            sump = sum(Peptide)

            if sump == pmass:
                pept_score = csc.NumCyclopeptideScore(Peptide, Spectrum)
                if pept_score > lead_score:
                    LeaderPeptide = Peptide + []
                    lead_score = pept_score

                work_board.remove(Peptide)
            else:
                if sump > pmass:
                    work_board.remove(Peptide)
       
        Leaderboard = nt.NumTrim(work_board, Spectrum, N)

    return LeaderPeptide