def LCS(s1, s2):
    a = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    s1 = ' ' + s1
    s2 = ' ' + s2
    s = ''
    
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                a[i][j] = 1 + a[i-1][j-1]
                s += s1[i]
            else:
                a[i][j] = max(a[i-1][j], a[i][j-1])

    print(f'The LCS between the two strings are: {s} \nThe number of similar elements are: {a[-1][-1]}')
        
str1 = 'abcdef'
str2 = 'ace'

print(f'The first string is: {str1} \nThe second string is: {str2}')
print('')
LCS(str1, str2)