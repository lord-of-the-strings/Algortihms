# Algorithms
Step-by-step visualization of important algorithms for visual learners.

**NOTE**: Some animation steps were done using AI tools althought the process of curating and implementing the algorithms themselves was done independently by the author. The author's motive is to learn the algorithms by visualisation and not learn how to animate things in python.

## 1. Kadane's Algorithm
Kadane's Algorithm typically finds the [maximum subarray sum](https://cses.fi/problemset/task/1643). It finds wide applications in various fields like business analysis and detecting the time window in which the CPU was most overloaded. 
A typical implementation in python looks like:
```python
best=0
sum=0
for k in range(n):
  sum=max(array[k],sum+array[k])
  best=max(best,sum)
print(best)
```
To run the visualization, clone this repo and execute it in python - ensure you have matplotlib and numpy installed.
```bash
git clone https://github.com/lord-of-the-strings/Algorithms
cd Algorithms
python Kadane.py
```

## 2. Merge Sort
Merge Sort is an O(nlogn) sorting algorithm written by John von Newumann in 1945. It sorts an array by recursively sorting its halves and merging them. A typical implementation in python looks like:
```python
arr=[1,3,6,2,8,2,5,9]
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    arr_left=arr[:mid]
    arr_right=arr[mid:]
    sorted_left=merge_sort(arr_left)
    sorted_right=merge_sort(arr_right)
    return merge(sorted_left,sorted_right)
def merge(l,r):
    arr=[]
    i=0
    j=0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            arr.append(l[i])
            i+=1
        else:
            arr.append(r[j])
            j+=1
    arr.extend(l[i:])
    arr.extend(r[j:])
    return arr
print(merge_sort(arr))
```
To run the visualization, clone this repo and execute merge.py in python - ensure that you have matplotlib and networkx installed.
```bash
git clone https://github.com/lord-of-the-strings/Algorithms
cd Algorithms #Make sure you do not have a similar path or provide a custom path to git clone
python merge.py #Close the window to stop; you may have to send SIGTERM twice if you do that
```
