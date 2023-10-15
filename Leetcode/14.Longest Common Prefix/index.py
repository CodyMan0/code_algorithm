
def longestCommonPrefix(strs2) :
    res = ""

    for i in range(len(strs2[0])) :
        for s in strs2 :
            if i == len(s) or s[i] != strs2[0][i] :
                return res
        res += strs2[0][i]

    return res

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]

print(longestCommonPrefix(strs2))