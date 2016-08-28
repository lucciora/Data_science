import random
#print(random.seed(1000))
b = random.randint(60,100)
a= 0
count=0
while a!=b:
    a = random.randint(60,100)
    print(a,b)
    if a==b:
        print("matched")
    count+=1
print(count)


# 시드를 설정하면, 나왔던 숫자를 다시 사용할 수 있음