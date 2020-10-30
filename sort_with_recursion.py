#This is a program to sort with recursion in python.


def sort_fun(arr):
  l=len(arr)
  if l==0:
    return
  temp=arr.pop()
  sort_fun(arr)
  insert(arr,temp)
def insert(arr,temp):
  if(len(arr)==0 or arr[len(arr)-1]<=temp):
    arr.append(temp)
    return
  val=arr[len(arr)-1]
  arr.pop()
  insert(arr,temp)
  arr.append(val)
  
arr=list(map(int,input().split()))
sort_fun(arr)
