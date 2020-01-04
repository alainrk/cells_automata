from random import gauss
arr = [0 for i in range(0, 11)]
for c in range(1000000000):
  i = round(min(10, max(0, gauss(5, 1))))
  arr[i] += 1
  # print(arr)

m = min(arr)
print(m, arr)
arr = list(map(lambda x: x-m, arr))
print(arr)