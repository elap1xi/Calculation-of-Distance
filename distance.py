class loc:
    a1 = 0,
    a2 = 0,
    b1 = 0,
    b2 = 0,
r = 6378.135
d = 111.31945588668853276112184419674
def x(a1, b1):
    x = a1 - b1
def y(a2, b2):
    y = a2 - b2
def err():
    print("형식에 맞게 입력해주세요")
while(True):
    a = input("첫번째 위치의 경도와 위도를 입력해 주세요 (형식: ddd.mmmmmm/dd.mmmmmm) : ")
    if(len(a)==20):
        try:
            k1 = a.split("/")
            a1 = float(k1[0])
            a2 = float(k1[1])
            break
        except:
            err()
    else:
        err()
while(True):
    b = input("두번째 위치의 경도와 위도를 입력해 주세요 (형식: ddd.mmmmmm/dd.mmmmmm) : ")
    if(len(a)==20):
        try:
            k2 = b.split("/")
            b1 = float(k2[0])
            b2 = float(k2[1])
            break
        except:
            err()
    else:
        err()
# print(a1,a2,b1,b2)

