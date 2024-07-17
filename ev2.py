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
N=10000
l=[]
r=[]
f=open("/dev/random",'rb') # /dev/randomを開く

# ｎ回シミュレーションをした場合の結果のリストを作る
for i in range(N):
 k=0
 while(True):
   k=k+1
   n=f.read(1)
   r1=binascii.hexlify(n)
   r2=int(r1,16)
   if r2%2: break
 r+=[k]
 l+=[2**(k-1)]

# 平均を取る
a=sum(l)/N
b=sum(r)/N

print("シミュレーション")
print("回数：",r)
print("利得額：",l)
print("コインを投げる平均回数: ",b)
print("μ(%d)=%f"%(N,2**(b-1)))
print("平均利得額: ",a)
