s,k,h = map(int,input().split())

if s + k + h >= 100 :
    print("OK")
else :
    if k < s and k < h :print("Korea")
    elif s < k and s < h : print("Soongsil")
    elif h < s and h < k : print("Hanyang")