#!/usr/bin/python3
import os
import binascii
import random
import mpmath
from getkey import getkey,keys
mpmath.mp.dps=1000

#方法１
# ∞＝１００００とした場合のSの近似値
# S=Σk=1,10000 (1/2^k)
#
s=0
for i in range(10000):
 s=s+1/mpmath.power(2,i)
print("方法１:",end='')
print(2**(s-1))

print("Hit any key")
key=getkey()

# 10000回ゲームを繰り返した場合の平均の算出
s2=0
N=10000
l=[]
f=open("/dev/random",'rb') # /dev/randomを開く
random32bitdata=f.read(4) # ４バイト読み出し
randomhex=binascii.hexlify(random32bitdata) #１６進の文字列に変換
randomint=int(randomhex,16) # 整数に変換
random.seed(randomint) # ランダムシードを初期化

# ｎ回ゲームをした場合の結果のリストを作る
for i in range(N):
 k=0
 while(True):
   k=k+1
   coin=random.randrange(2)
   if coin==0:
     break
 l+=[float(mpmath.power(2,k-1))]

# 平均を取る
s=0
for i in range(len(l)):
 s+=l[i]
a=s/N
print("シミュレーション")
print(l)
print("平均: ",end='')
print(a)
