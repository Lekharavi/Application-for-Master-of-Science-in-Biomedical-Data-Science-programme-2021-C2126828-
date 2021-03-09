# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:06:09 2021

@author: ravichandrapl
"""

def findPath(arr,x,y,Sum,path):
    global m,n,required_sum
    if x==m-1 and y==n-1:
        if Sum+arr[x][y]==required_sum:
            return path
        else:
            return 0
    if Sum>required_sum:
        return 0
    if x<m-1:
        ans=findPath(arr,x+1,y,Sum+arr[x][y],path+"R")
        if ans!=0:
            return ans
    if y<n-1:
        ans=findPath(arr,x,y+1,Sum+arr[x][y],path+"D")
        if ans!=0:
            return ans
    return 0
arr=[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
Sum=0
required_sum=110
m,n=9,9
x,y=0,0
path=""
ans=findPath(arr,x,y,Sum,path)
if ans!=0:
    print(ans)
else:
    print('Not Possible')