a=int(input())
print([['01'[a%4==0],'0'][a%100==0],'1'][a%400==0])