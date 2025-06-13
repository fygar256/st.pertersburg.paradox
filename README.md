---
title: A consideration of the St. Petersburg Paradox using python3
tags: Python3 Terminal Mathematics
author: fygar256
slide: false
---
The St. Petersburg Paradox

In a game where you flip a coin and continue until it lands on heads, if the number of flips is N, you will receive a prize of 2^(N-1) yen. If you calculate the expected value, it diverges to infinity.

W=Σk=1,∞(1/2^k・2^(k-1))=∞

This is counterintuitive, so it is called the St. Petersburg Paradox.

First, find the expected number of coin flips S,

and then calculate the expected prize amount μ (Method 1). …①

S=Σk=1,∞ (1/2^k)=2

Since S=2, μ=2^(S-1)=2

Therefore, the answer is 2.

This is a semantically valid inference, but mathematically incorrect, because the number of coin tosses in one game can be infinite.

In general, f(g(x))=g(f(x)) does not hold for the expected value.

William Feller also calculated this by sampling, and the correct answer is that the expected value is infinite.

If the number of games is finite, the expected value converges to a much smaller value.

Daniel Bernoulli presented this paradox and found a solution in the form of utility by taking the logarithm of the prize money, but saying that the value of money decreases as the prize money increases introduces human subjectivity, so it is not an objective answer.

Below is a program to calculate the average value when Method 1 and the simulation are repeated n times.

Here, n=10000.

```ev0.py
#!/usr/bin/python3
import os
import binascii
import random
from getkey import getkey,keys

#Method 1
# Approximate value of S when ∞=10000
# S=Σk=1,10000 (1/2^k)
#
s=0
for i in range(10000):
s=s+1/2**i
print("Method 1:",2**(s-1))

print("Hit any key")
key=getkey()

# Calculate the average when the game is repeated 10000 times
N=10000
l=[]
r=[]
f=open("/dev/random",'rb') # Open /dev/random

# Create a list of results when simulating n times
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

# Take the average
a=sum(l)/N
b=sum(r)/N

print("Simulation")
print("Number of times:",r)
print("Payoff:",l)
print("Average number of coin tosses: ",b)
print("μ(%d)=%f"%(N,2**(b-1)))
print("Average payoff: ",a)
```

Results of program execution

```
$ ev.py
Method 1:2.0
Press any key
Simulation
Number of times: [3, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 3, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 4, 3, 1, 3, 4, 5, 3, 1, 3, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 2, 1, 1, 3, 1, 1, 3, 4, 1, 1, 5, 5, 4, 1, 1, 2, 5, 1, 1, 1, 1, 2, 1, 2, 1, 2, 3, 2, 3, 2, 2, 1, 2, 1, 2, 1, 2, 3, 1, 1, 1, 3, 1, 10,, omitted because it's long, 8, 1, 7, 1, 1, 1]
Profit: [4.0, 1.0, 2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 4.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 2.0, 2.0, 8.0, 4.0, 1.0, 4.0, 8.0, 16.0, 16.0, 8.0, 1.0, 1.0, 1.0, 1.0, 2.0, 16.0, 16.0, 8.0, 1.0, 1.0, 1.0, 2.0, 16.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 4.0, 2.0, 4.0, 2.0, 2.0, 1.0, 2.0, 1.0, 1.0, 2.0, 4.0, 1.0, 1.0, 1.0, 4.0, 1.0, 512.0, long, omitted, 128.0, 1.0, 64.0, 1.0, 1.0, 1.0]
Average number of coin tosses: 1.9905
μ(10000)=1.974132271
Average payoff: 6.5987
$
```

When 10000 simulations are performed, the average number of coin tosses is 1.9905, so
μ(10000 simulations)＝2^(1.9905-1)≒1.974132271

This is a big difference from the average payoff of 6.5987.

Average of r: (r[0]+r[1]+r[2]+r[3]+r[4]+...+r[9999])/10000=1.9905

Average of r is expressed as (r1+r2+r2+...+rn)/n.

If the number of r is always 2, then (∑(i=1,n){2^(2-1)})n=(∑(i=1,n){2})n=2.

Average of l is la=(l[0]+l[1]+l[2]+...+l[9999])/10000=6.5987 //Simulation
=(∑(i=1,n){l[i]})/n=(∑(i=1,n){2^(r[i]-1)})/n.

In the limit, if l=μ and r=S in ①, then l=2^(r-1).

Solution by computer simulation

The solution obtained by simulating the game 1 billion times is as follows.

Program

```ev.py
#!/usr/bin/python3
import os
import binascii
import random
from getkey import getkey,keys

N=1000000000
# Calculate the average over N repetitions of the game
l=0
r=0
f=open("/dev/random",'rb') # Open /dev/random

# Create a list of results over n simulations

for i in range(N):
k=0
while(True):
k=k+1
n=f.read(1)
r1=binascii.hexlify(n) # Convert to hex string
r2=int(r1,16) # Convert to integer
if r2%2:
break
print(i,chr(13),end='',flush=True)
r+=k
l+=2**(k-1)
f.close() # Close /dev/random

# Take the average
a=l/N
b=r/N

print("Number of simulations:",N)
print("Average number of coin tosses: ",b)
print("Average payoff: ",a)
```

Execution results

```
Number of simulations: 1000000000
Average number of coin tosses: 2.000005233
Average payoff: 19.908359876
```

Therefore, the "realistic" expected value is at most 20 yen. It is better not to gamble on this.

We are waiting for the appearance of Ezekiel Bernoulli, who solves this problem by renormalizing the expected value with a new theory of mathematics.

Another reason for this problem is that information disappears after calculation.

If the simulation ends after N times, the average reward H(N) is a function of N including probabilistic unknowns.

In the end, if you go infinitely, lim N→∞ H(N)＝∞.
