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
 
 
def compute(locations, stars, n):
   #debug(locations, stars)
   if stars<2: return 0
   place = locations[0]+1
   j = 1
   stars-=1
   ret, total_dist = 0, 0
   
   for i in range(place-1, n):
      if stars==0: break
      distance = locations[j] - place - total_dist
      ret += (distance*stars)
      #debug(distance, stars, ret, n)
      place+=1
      stars-=1
      j+=1
      total_dist+=distance
      
   return ret

 
for _ in range(int(input())):
   n = int(Input())
   string = Input()[:-1]
   if n==1:
      print(0)
      continue
      
   reverse, foward, stars = [], [], 0
   
   for i in range(n):
      if string[i]=='*': 
         foward.append(i)
         reverse.append(n-1-i)
         stars+=1
   reverse = sorted(reverse)   
   debug('forward', foward)
   debug('reverse', reverse[::-1])
   
   temp = stars//2
   
   if stars%2:
      f_loc = foward[temp:]
      r_loc = reverse[temp:]
      number = temp+1
      f_size = n-temp
      
      fow = compute(f_loc, number, n)
      rev = compute(r_loc, number, n)
      print(fow+rev)
     
    
   else:
      ans = 10**18
      for t in range(2):
         f_loc = foward[temp-t:]
         r_loc = reverse[temp-1+t:]
         number = temp
         f_size = n-temp
         r_size = n - f_size
         
         fow = compute(f_loc, number+t, n)
         rev = compute(r_loc, number+1-t, n)
         
         ans = min(fow+rev, ans)
         
      print(ans)
   

   
   
 
   
   
   
