'''
E와 F가 독립 사건이면
P(E,F) = P(E)P(F)

E conditional on F
P(E|F) = P(E,F)/P(F)
P(E,F) = P(E|F)P(F)

E와 F가 독립 사건이라면,
P(E|F) = P(F)

1. 두 아이는 각각 남자아이이거나, 여자아이일 수 있다.
2. 두 번째 아이의 성별은 첫 번째 아이의 성별과 무관하다
no_girls = 1/4
one_girl, one_boy = 1/2
two_girls = 1/4

두 모두 여자아이 = (B)
첫째만 여자아이 = (G)
P(B|G) = P(B,G)/P(G) = P(B)/P(G) = 1/2
이벤트 B, G는  B이다.
 두 명 모두 여자아이이면, 첫째는 무조건 여자아이!


모두 여자아이  (B) = 1/4 
최소한 한명은 여자아이  (A) = 1-1/4 = 3/4
P(B|A) = P(B,A)/P(A) = P(B)/P(A) = 1/3
'''
import random
def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl+=1
    if older == "girl" and younger == "girl":
        both_girls+=1
    if older == "girl" or younger == "girl":
        either_girl +=1
print("P(both | older):", both_girls /older_girl)  
print("P(both | either):", both_girls / either_girl)      





