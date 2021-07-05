"""
  Author: Enivar
  Date:  
"""
 
from sys import exit, stderr, stdout, stdin
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, Counter
from heapq import nlargest, nsmallest, merge
from math import ceil
from ctypes import c_longlong as ll
from ctypes import c_float,c_int,c_int8, c_int16, c_int32, c_int64
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
 
 
for _ in range(int(input())):
   n = int(Input())
   a = [int(x) for x in Input().split()]
   reference = a[0]
   d = {}
   for i in range(n):
      try: d[reference-a[i]]+=1
      except: d[reference-a[i]] = 1
      reference+=1
      
   ans = 0
   for key in d:
      value = d[key]
      if value > 1:ans+=((value-1)*value)//2
      
   print(ans)
   
   
