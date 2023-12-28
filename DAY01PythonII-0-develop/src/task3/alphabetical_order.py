dct = {}
with open('materials/task3/names.txt', 'r') as file:
    lst = [line.strip().split()[0] for line in file.readlines()]
    
lst.sort()
for name in lst:
    dct[name] = dct.setdefault(name, 0) + 1
#print(lst)

with open('src/task3/sorted_names.txt', 'w') as file:
    for k, v in dct.items():
        print(f"{k}–{v}", end='\n', file=file)
