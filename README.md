ST.Petersburg paradox

If you keep tossing coins until you get a face and the number of tosses is N,

In a game where you get 2^(N-1) yen, if you calculate the expected value,diverges to infinity.

W=Σk=1,∞(1/2^k/2^(k-1))=∞

This is called the St. Petersburg paradox because it goes against intuition.

Once we find the expected value S of the number of coin tosses, then, let us take the method (Method 1) to calculate the expected value of the prize money (also called “μ”). ...①)

S=Σk=1,∞ (1/2^k)=2

Since S=2, μ=2^(S-1)=2

Hence, the answer is 2.

which is incorrect. (Common mistake)

In general, since f(g(x))=g(f(x)) does not hold in the expected value,

Once the expected value of the number of coin tosses is obtained, the expected value of the prize money (or something similar) is then obtained,

Then, it is incorrect to calculate the expected value of the prize (or something similar).

However, I don't understand what is incorrect with this.

Semantically correct, but mathematically incorrect.

The amount of money you get per game is 2^n, so here is the point of error.

William Feller also calculated this by sampling, and the correct answer is an expected value of infinity.

If the number of games is limited to a finite number, then the expected value converges to a far smaller value.

It is not clear if renormalization of infinity is possible.

Daniel Bernoulli presented this paradox and sought the solution of utility by taking the logarithm of the prize money, but it is not an objective answer because the larger the prize money, the smaller the value of a penny, because of human subjectivity.

Method 1 and a program to find the average value when the simulation is repeated n times are included.

Here we assume n=10000

```
#! /usr/bin/python3
import os
import binascii
import random
from getkey import getkey,keys

#Method 1
# Approximate value of S when ∞ = 10000
# S=Σk=1,10000 (1/2^k)
# method 1 # approximate value of S when ∞=10000
s=0
for i in range(10000):.
 s=s+1/2**i
print(“Method 1:”,2**(s-1))

print(“Hit any key”)
key=getkey()

# Calculate the average of 10000 game repetitions
N=10000
l=[]
r=[]
f=open(“/dev/random”,'rb') # Open /dev/random

# Make a list of results for n simulations
for i in range(N): for i in range(N): for i in range(N)
 k=0
 while(True): k
   k=k+1
   n=f.read(1)
   r1=binascii.hexlify(n)
   r2=int(r1,16)
   if r2%2: break
 r+=[k]
 l+=[2**(k-1)]

# Take the average
a=sum(l)/N
b=sum(r)/N

print(“Simulation”)
print(“Number of times:”,r)
print(“Amount of gain:”,l)
print("Average number of coin tosses: ”,b)
print(“μ(%d)=%f”%(N,2**(b-1)))
print("Average amount of gain: ”,a)
```

Result of program execution

```
$ ev.py
Method 1:2.0
Hit any key
Simulation
 5, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 2, 3, 3, 2, 2, 1, 2, 1, 1, 2, 3, 1, 1, 1, 1, 3, 1, 10, ,long so abbreviated,8, 1, 7, 1, 1, 1]
  16.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 2.0, 2.0, 4.0, 2.0, 4.0, 4.0, 2.0, 1.0, 1.0, 1.0, 2.0, 1.0, 4.0, 4.0, 4.0, 1.0, 1.0, 4.0, 1.0, 512.0, omitted because long , 128.0, 1.0, 64. 0, 1.0, 1.0, 1.0, 1.0]
Average number of coin tosses: 1.9905
μ(10000)=1.974132271
Average gain: 6.5987
$ 
```

Here, when the simulation is run 10000 times,

Since the average number of coin tosses is 1.9905,

μ (in 10000 simulations) = 2^(1.9905-1) ≈ 1.974132271 with,

This is a large difference from the average gain of 6.5987.

Average of r: (r[0]+r[1]+r[2]+r[3]+r[4]+... +r[9999])/10000=1.9905

The average of r is (r1+r2+r2+... +rn)/n.

If the number of times r is all 2, then (∑(i=1,n){2^(2-1)})n=(∑(i=1,n){2})n=2.

The average of l, la=(l[0]+l[1]+l[2]+... +l[9999])/10000=6.5987 = (∑(i=1,n){l[i]})/n=(∑(i=1,n){2^(r[i]-1)})/n.

In the limit, in (1), if l=μ and r=S, then l=2^(r-1).

Solution by computer simulation

The solutions obtained by simulating the game one billion times are shown here.

The program

```
ev.py
#! /usr/bin/python3
import os
import binascii
import random
from getkey import getkey,keys

N=1000000000
# Calculate the average of N game iterations
l=0
r=0

f=open(“/dev/random”,'rb') # Open /dev/random

# Make a list of results for n simulations

for i in range(N): for i in range(N): for i in range(N)
 k=0
 while(True): k
   k=k+1
   n=f.read(1)
   r1=binascii.hexlify(n) # convert to hexadecimal string
   r2=int(r1,16) # convert to integer
   if r2%2: break
     break
 print(i,chr(13),end='',flush=True)
 r+=k
 l+=2**(k-1)

f.close() # close /dev/random

# Take the average
a=l/N
b=r/N

print("Number of simulations: ”,N)
print("Average number of coin tosses: ”,b)
print("Average amount of gain: ”,a)
```

Execution Result

```
Number of simulations: 1000000000
Average number of coin tosses: 2.000005233
Average gain: 19.908359876
```
love.
Translated with DeepL.com (free version)
