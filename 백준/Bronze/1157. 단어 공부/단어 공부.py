
s = input()

upper_s = s.upper()

dp = [0] * 26

for i in upper_s : 
    dp[ord(i) - 65] += 1
max_dp = max(dp)

if dp.count(max_dp) >= 2 :
    print('?')
else :
    print(chr(dp.index(max_dp) + 65))
