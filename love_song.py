"""
  Author: Enivar
  Date:  
"""
 
from sys import exit, stderr, stdout, stdin
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, Counter
from heapq import nlargest, nsmallest, merge
from math import ceil
import heapq
import io, atexit, sys
 
buffer = io.BytesIO()
stdout = buffer
 
copy = lambda array: [x for x in array]
vector = lambda lim, fill: [fill for _ in range(lim)] 
inList = lambda : [int(x) for x in input().split()]
Input = lambda : stdin.readline()
 
#@atexit.register
#def write():
#   sys.__stdout__.write(buffer.getvalue())
 
def debug(*args):
   for i in args: 
      stderr.write(str(i)+' ')
   stderr.write('\n')
 
def Print(*args):
   for i in args: 
      stdout.write(str(i)+' ')
   stdout.write('\n')
 
class Solve:
   def __init__(self):
      self.i = 0
 
   def inp(self, x):
      return x
 
a = 97
 
if __name__=='__main__':
   n, q = map(int, Input().split())
   s = Input()
   s = s[:-1]
   d = [0]
   for k in range(n):
      d.append(ord(s[k])-a+1)
      if k>0: d[k+1] = d[k]+d[k+1]
   #debug(d)
   for i in range(q):
      l, r = map(int, Input().split())
      ans = d[r]-d[l-1]
      print(ans)
   

   
  
