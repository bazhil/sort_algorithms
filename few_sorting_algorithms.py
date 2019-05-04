data = [10, 3, 6, 1, 9, 4, 7, 2, 8, 5]
print('data: ', data)

#change sort
def insertion(data):
  for i in range(len(data)):
    j = i - 1
    key = data[i]
    while data[j] > key and j >= 0:
      data[j + 1] = data[j]
      j -= 1
    data[j + 1] = key
  return data

print('first sort: ', insertion(data))

#another change sort
def insertion_sort(data):
  for i in range(len(data)):
    tmp = data[i]
    j = i - 1
    while j >=0 and tmp < data[j]:
      data[j + 1], data[j] = data[j], data[j + 1]
      j -= 1
  return data

print('another sort: ', insertion_sort(data))

#shell sort
def shell(data):
  inc = len(data) // 2
  while inc:
    for i, el in enumerate(data):
      while i >=1 and data[i - inc] > el:
        data[i] = data[i - inc]
        i -= inc
      data[i] = el
    inc = 1 if inc == 2 else int(inc * 5.0 / 11)
  return data

print('shell sort: ', shell(data))

#stooge sort
def stooge_sort(data, i=0, j=None):
  if j is None:
    j = len(data) - 1
  if data[j] < data[i]:
    data[i], data[j] = data[j], data[i]
  if j - i > 1:
    t = (j - i + 1) // 3
    stooge_sort(data, i, j - t)
    stooge_sort(data, i + t, j)
    stooge_sort(data, i, j - t)
  return data

def stooge(data):
  return stooge_sort(data, 0, len(data) - 1)

print('stooge sort: ', stooge(data))

#stupid sort
def stupid_sort(data):
  i, size = 1, len(data)
  while i < size:
    if data[i - 1] > data[i]:
      data[i - 1], data[i] = data[i], data[i - 1]
      i = 1
    else:
      i += 1
  return data

print('stupid sort: ', stupid_sort(data))

#gnome sort
def gnome(data):
  i, size = 1, len(data)
  while i < size:
    if data[i - 1] <= data[i]:
      i += 1
    else:
      data[i - 1], data[i] = data[i], data[i - 1]
      if i > 1:
        i -= 1
  return data

print('gnome sort: ', gnome(data))

#optimized gnome sort
def opt_gnome(data):
  i, j, size = 1, 2, len(data)
  while i < size:
    if data[i - 1] <= data[i]:
      i, j = j, j + 1
    else:
      data[i - 1], data[i] = data[i], data[i - 1]
      i -= 1
      if i == 0:
        i, j = j, j + 1
  return data

print('optimized gnome sort: ', opt_gnome(data))

#bubble sort
def bubble_sort(data):
  changed = True
  while changed:
    changed = False
    for i in range(len(data) - 1):
      if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]
        changed = True
  return data

print('bubble sort: ', bubble_sort(data))

#odd-ever sort
def odd_even_sort(data):
  n = len(data)
  is_sorted = 0
  while is_sorted == 0:
    is_sorted = 1
    temp = 0
    for i in range(1, n - 1, 2):
      if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]
        is_sorted = 0
    for i in range(0, n - 1, 2):
      if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]
        is_sorted = 0
  return data

print('odd-even sort: ', odd_even_sort(data))

#comb sort
def comb_sort(data):
  gap = len(data)
  swaps = True
  while gap > 1 or swaps:
    gap = max(1, int(gap / 1.25))
    swaps = False
    for i in range(len(data) - gap):
      j = 1 + gap
      if data[i] > data[j]:
        data[i], data[j] = data[j], data[i]
        swaps = True
  return data

print('comb sort: ', comb_sort(data))

#Quick sort
def quick_sort(data):
  less = []
  pivot_list = []
  more = []
  if len(data) <= 1:
    return data
  else:
    pivot = data[0]
    for i in data:
      if i < pivot:
        less.append(i)
      elif i > pivot:
        more.append(i)
      else:
        pivot_list.append(i)
    less = quick_sort(less)
    more = quick_sort(more)
    return less + pivot_list + more

print('quick sort: ', quick_sort(data))