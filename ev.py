#!/usr/bin/python3
import os
import binascii
import truerand

N=100
# N回ゲームを繰り返した場合の平均の算出
l=0
r=0

# ｎ回シミュレーションをした場合の結果のリストを作る

for i in range(N):
 k=0
 while(True):
   k=k+1
   if truerand.randomint(2,1):
     break
 print(i,chr(13),end='',flush=True)
 r+=k
 l+=2**(k-1)

# 平均を取る
a=l/N
b=r/N

print("シミュレーション回数：",N)
print("コインを投げる平均回数: ",b)
print("μ(%d)=%f"%(N,2**(b-1)))
print("平均利得額: ",a)
