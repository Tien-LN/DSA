# HASHSETS

s = set()
print(s)

# add item into set - O(1)

s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

# lookup if item in set - O(1)

if 3 in s:
    print(True)
else:
    print(False)
    
# remove from set - O(1)

s.remove(2)
print(s)

# set contruction - O(S) - s is the length of the string,..

string = 'aaaaaaaaaaaabbbbbbbbbbbbbccccccccccddddd'
sett = set(string)
sett

# loop over item in set - O(n)

for x in s:
    print(x)

for i in sett:
    print(i)
    
# ------------------------------------------------------- #

# HASHMAPS - DICTIONARIES

d = {'Lam' : 1, 'Nhat' : 2, 'Tien' : 3}
print(d)

# add key:val in dictionary - O(1)

d['hello'] = 4
print(d) 

# check for presence of key in dictionary - O(1)

if 'Tien' not in d:
    print(True)
else:
    print(False)

# check the value corresponding to a key in dictionary - O(1)

print(d['Nhat'])

# loop over the key:val pairs of dictionary - O(n)

for key, val in d.items():
    print(f'key {key} : val {val}')
    
# DefaultDict

from collections import defaultdict

df1 = defaultdict(int) # you can put anything you want like list,...
df1[4]                 # default int is 0

df2 = defaultdict(list)
df2[2] 

df1
df2 

# counter ( NOT recommend using this in interview)

from collections import Counter
counter = Counter(string)
print(counter)