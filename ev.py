#!/usr/bin/python3
import os
import binascii
import random
from getkey import getkey,keys

#方法１
# ∞＝１００００とした場合のSの近似値
# S=Σk=1,10000 (1/2^k)
#
s=0
for i in range(10000):
 s=s+1/2**i
print("方法１:",2**(s-1))

print("Hit any key")
key=getkey()

# 10000回ゲームを繰り返した場合の平均の算出
s2=0
N=10000
l=[]
r=[]
f=open("/dev/random",'rb') # /dev/randomを開く
random32bitdata=f.read(4) # ４バイト読み出し
randomhex=binascii.hexlify(random32bitdata) #１６進の文字列に変換
randomint=int(randomhex,16) # 整数に変換
random.seed(randomint) # ランダムシードを初期化

# ｎ回シミュレーションをした場合の結果のリストを作る
for i in range(N):
 k=0
 while(True):
   k=k+1
   coin=random.randrange(2)
   if coin==0:
     break
 r+=[k]
 l+=[2**(k-1)]

# 平均を取る
s=0
t=0
for i in range(len(l)):
 s+=l[i]
 t+=r[i]
a=s/N
b=t/N

print("シミュレーション")
print("回数：",r)
print("利得額：",l)
print("コインを投げる平均回数: ",b)
print("μ(%d)=%f"%(N,2**(b-1)))
print("平均利得額: ",a)
