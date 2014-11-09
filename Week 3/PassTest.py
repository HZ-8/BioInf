str1 = [1,2,1,3, 4]
str2 = [1,5]
score = 0
for i in range(len(str1)):
    if str1[i] in str2:
        score +=1
    
print score