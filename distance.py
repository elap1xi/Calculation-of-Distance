import math as m
class loc:
    a0 = []
    a00 = []
    b0 = []
    b00 = []
r = 6378.135
d = 111.31945588668853276112184419674
def err():
    print("형식에 맞게 입력해주세요")
def calc(dis_d1, dis_m1, dis_s1, dis_d11, dis_m11, dis_s11, cd_a11, cd_b11, d):
    cok = m.cos((cd_a11 + cd_b11)/2) * d
    calc_1 = dis_d1 * cok
    # print("calc_1: ",calc_1)
    calc_2 = dis_m1 * (cok/60)
    # print("calc_2: ",calc_2)
    calc_3 = dis_s1 * (cok/3600)
    # print("calc_3: ",calc_3)
    calc_01 = (calc_1 + calc_2 + calc_3)**2
    # print("calc_01: ",calc_01)
    calc_4 = dis_d11 * d
    # print("calc_4: ",calc_4)
    calc_5 = dis_m11 * (d/60)
    # print("calc_5: ",calc_5)
    calc_6 = dis_s11 * (d/3600)
    # print("calc_6: ",calc_6)
    calc_02 = (calc_4 + calc_5 + calc_6)**2
    # print("calc_02: ",calc_02)
    calc = round(m.sqrt(calc_01+calc_02),5)
    calc_m = round(1000 * calc,5)
    print("Distance of two points : ",calc,"km (",calc_m,"m )")
while(True):
    a = input("첫번째 위치의 경도와 위도를 입력해 주세요 (형식: ddd.mmmmmm/dd.mmmmmm) : ")
    if(len(a)==20):
        try:
            k1 = a.split("/")
            a1 = k1[0]
            a2 = k1[1]
            loc.a0 = list(a1)
            loc.a00 = list(a2)
            if(loc.a0[3]=="."):
                if(loc.a00[2]=="."):
                    break
                else:
                    err()
            else:
                err()
        except:
            err()
    else:
        err()
while(True):
    b = input("두번째 위치의 경도와 위도를 입력해 주세요 (형식: ddd.mmmmmm/dd.mmmmmm) : ")
    if(len(a)==20):
        try:
            k2 = b.split("/")
            b1 = k2[0]
            b2 = k2[1]
            loc.b0 = list(b1)
            loc.b00 = list(b2)
            if(loc.b0[3]=="."):
                if(loc.b00[2]=="."):
                    break
                else:
                    err()
            else:
                err()
        except:
            err()
    else:
        err()
cd_a1 = int("".join(loc.a0[0:3]))
cka1 = list(str(int("".join(loc.a0[4:10])) * 60 * 1/1000000))
cm_a1 = int("".join(cka1[0:2]))
cs_a1 = float("".join(list(str(float("".join(cka1[3:8])) * 60 * 1/100000))[0:5]))
# print(cd_a1,"\n",cm_a1,"\n",cs_a1)
cd_a11 = int("".join(loc.a00[0:2]))
cka11 = list(str(int("".join(loc.a00[3:9])) * 60 * 1/1000000))
cm_a11 = int("".join(cka11[0:2]))
cs_a11 = float("".join(list(str(float("".join(cka11[3:8])) * 60 * 1/100000))[0:5]))
# print(cd_a11,"\n",cm_a11,"\n",cs_a11)
cd_b1 = int("".join(loc.b0[0:3]))
ckb1 = list(str(int("".join(loc.b0[4:10])) * 60 * 1/1000000))
cm_b1 = int("".join(ckb1[0:2]))
cs_b1 = float("".join(list(str(float("".join(ckb1[3:8])) * 60 * 1/100000))[0:5]))
# print(cd_b1,"\n",cm_b1,"\n",cs_b1)
cd_b11 = int("".join(loc.b00[0:2]))
ckb11 = list(str(int("".join(loc.b00[3:9])) * 60 * 1/1000000))
cm_b11 = int("".join(ckb11[0:2]))
cs_b11 = float("".join(list(str(float("".join(ckb11[3:8])) * 60 * 1/100000))[0:5]))
# print(cd_b11,"\n",cm_b11,"\n",cs_b11)
dis_d1 = cd_a1 - cd_b1
dis_m1 = cm_a1 - cm_b1
dis_s1 = cs_a1 - cs_b1
dis_d11 = cd_a11 - cd_b11
dis_m11 = cm_a11 - cm_b11
dis_s11 = cs_a11 - cs_b11
calc(dis_d1, dis_m1, dis_s1, dis_d11, dis_m11, dis_s11, cd_a11, cd_b11, d)
