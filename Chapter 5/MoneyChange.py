def DPChange(money, Coins):
    '''With a set of Coins, find minimal amount of coins to change the money'''
    MinNumCoins = {0: 0}
    
    for m in range(1, money+1):
        MinNumCoins[m] = money + 1
        for i in range(len(Coins)):
            if m >= Coins[i]:
                if MinNumCoins[m - Coins[i]] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - Coins[i]] + 1
    return MinNumCoins[money]
    
def DPChangeEconomy(money, Coins):
    '''With a set of Coins, find minimal amount of coins to change the money.
    While iterating, do not save changes array longer than largest coin value'''
    maxCoin = max(Coins)
    MinNumCoins = {0: 0}
    
    for m in range(1, money+1):
        MinNumCoins[m] = money + 1
        for i in range(len(Coins)):
            if m >= Coins[i]:
                if MinNumCoins[m - Coins[i]] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - Coins[i]] + 1
        if len (MinNumCoins) > maxCoin:
            keys = MinNumCoins.keys()
            keys.sort()
            MinNumCoins.pop(keys[0])
    return MinNumCoins[money]   

def DPChangeCoins(money, Coins):
    '''With a set of Coins, find a minimal SET of coins to change the money.
    While iterating, do not save changes array longer than largest coin value'''
    maxCoin = max(Coins)
    MinSetCoins = {0: []}
    for m in range(1, money+1):
        MinSetCoins[m] = [0] * (m+1)
            
        for i in range(len(Coins)):
            if m >= Coins[i]:
                if len(MinSetCoins[m - Coins[i]]) + 1 < len(MinSetCoins[m]):
                    MinSetCoins[m] = MinSetCoins[m - Coins[i]] + [Coins[i]]
        if len (MinSetCoins) > maxCoin:
            keys = MinSetCoins.keys()
            keys.sort()
            MinSetCoins.pop(keys[0])
    return MinSetCoins[money]   