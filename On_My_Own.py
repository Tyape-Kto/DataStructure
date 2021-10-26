### this searches if it has your number or not but other is just filled with bugs. dang it
i = 0
def finder(num, arr):
  globals()['i'] += 1
  if num == arr[len(arr)//2]:
    return "Found !"
  elif len(arr) == 1 and num != arr[0]:
    return "Not Found !"
  else:
    middle = len(arr) // 2
    index = middle
    if num < arr[middle]:
      index = middle - middle // 2
      print("at", index)
      return finder(num, arr[:middle])
    else:
      index = middle + middle
      print("at", index)
      return finder(num, arr[middle:])
l = [i for i in range(1000000)]
print(finder(5000,l))
print(i, 'iterations')
