# t = int(input())

# list = [0] * 26


# for i in range(t) :
#     name = input()
#     last_name = name[0]
#     list[ord(last_name)-97] += 1


# if max(list) < 5 :
#     print('PREDAJA')
# else : 
#     result = ''
#     for i in range(len(list)) :
#         if list[i] > 4 : 
#             result += chr(i + 97)
#     print(result)


# 다른 사람 코드가 훨씬 깔끔한 것 같아 정리 및 습득 

arr = [input()[0] for _ in range(int(input()))]
f = 1
for i in range(97, 123):
    if arr.count(chr(i)) >= 5:
        f = 0
        print(chr(i), end='')

if f: print('PREDAJA')

# f 가 false일 경우에는 "PREDAJA"를 출력하고 아닐 경우에는 for문 안에서 print(chr(i), end='')를 통해서 더욱 간결한 코드로 구현하셨다. 
# 또한 for 문의 range 시작과 끝을 소문자 알파벳의 아스키 코드 번호에 한해서 돌게 해서 굳이 97을 빼고 더할 수고를 덜어주는 코드다. 


