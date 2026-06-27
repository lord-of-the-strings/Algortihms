# Algorithms
Step-by-step visualization of important algorithms for visual learners

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
