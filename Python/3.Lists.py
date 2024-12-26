''' List : is a collection of mutable python objects
----------------------------
In-built functions:
------------------------------
Length
Concatenation
Repetion
Membership
Iteration
	
-------------------------------
Other Built-In functions:
-------------------------------
append
extend
pop
count
min
max
sort
replace
split
insert
del
join
reverse
cmp
list(seq)
enumerate
find

----------------------------------------'''
-----------------------------------------------
#     REPRESENTATION AND BUILT-IN FUNCTIONS
----------------------------------------------

l1=list()

l1=[]

l1=[1,2,3,4,5,6,'python']

type(l1)

l1=[1,2,'a','b',2.555,'python',6]

l1[0]    # capturing the values based on indexing

l1[1]

l1.index('python')  # will give index value of given object

l1.index(6)

-----------------------------

# 1. Length

l1=[1,2,5,8,7,4,9,'a','z']

len(l1)


-----------------------------------------

#2. Concatenation

l1=[99,74,'python']

a=5

l1 + a  # will throw error concatenation possible between two lists


l1 +l2  # will work

-----------------------------------------

# 3. Repetion

l3=[1,2]

l3*2

a= 'python'

a*2

--------------------------------------

#4. Member ship

l1=[1,2,5,8,7,4,9,'a','z']

4 in l1

'a' in l1

-----------------------------------------

# 5. Iteration

l1=[1,2,3,4,5]

for i in l1:
     print i


#5.1 Eg.
     
for i in l1:
     print i*2

# 5.2 Eg.

for i in l1:
     print l1.index(i), i

# 5.3 Eg. Enumerate

for i in enumerate(l1):
     print i


---------------------------------------------
#         OTHER BUILT-IN FUNCTION
---------------------------------------------
'''
append - will append only one value into the lists
extend - will help to add more python objects into the list
'''

l1=[1,2,3,4,5,'a','b']

l2=[88,55,66]

a = 125

b = 'Course'

l1.append(100)
l1.append(15)
l1.append('python')
l1.append(a)
l1.append(l2)

l1.extend([55,74])
l1.extend(l2)
l1.extend([a,b])

'''
pop - will remove the last element from the list
count - will get the no. of occurrences of given python objects
min - will get minimum value from list
max - will get maximum value from list
del - will delete the complete list
sort - sorting will sort the objects based on increasing order
insert - will insert the value on mentioned index
remove - remove the mentioned object from list
cmp - compare l1 and l2. both matches return '0', l1 difference return '-1',l2 difference return '1'.
'''

l1.pop() 

l1.pop(0) # Index wise deletion 

l1.count(4)

min(l1)

max(l1)

a='apple'
a.replace('p','#')
a.replace('p','#',2)
#List not having the replace attribute

del l1

del l1[2]

del l1[len(l1)-2]


l1.sort()

l1.insert(2,'q')

l1.insert(4,'j')

l1.reverse()

l1.remove(4)

----------------------------------------------------
# SPLIT & LIST SEQUENCE & JOIN
-------------------------------------------------
#Exp : 1

a='python'

list(a)   

'-'.join(a)  # spliting the string by '-'

b='High level language'

c=b.split(' ')   # converting to list

' '.join(c)     # converting back list to string
------------------------------------

# Exp : 2

sentence = "Python is an interpreter lanuguage"

sentence.split(' ')  # will seperate as list

sentence.split(' ',0) # will seperate as list with single python object
sentence.split(' ',4) # will seperate as list with four python object

sentence.split(' ',5)[1]  # seperating as 5 py objects and picking up 1st element
sentence.split(' ',5)[3]  # seperating as 5 py objects and picking up 3rd element
sentence.split(' ',5)[1:]  # seperating as 5 py objects and slicing up from 1st element


-----------------------------------------
#           NESTED LISTS
------------------------------------------

l1=[1,2,3,4,5,7,8,'abc']

l2 = [10,20,30]

l1.append([100,90,80])

l1.append(l2)

# output : [1, 2, 3, 4, 5, 7, 8, 'abc', [100, 90, 80], [10, 20, 30]]

for i in enumerate(l1):
     print i

l1[8].append(555)  # appending the value into nested list (i.e[100,90,80]) of l1
l1[9].extend([5,85,'a'])

----------------------------------------------------------------------
#                             find and rfind
----------------------------------------------------------------------
'''
find : will start the index from to till the end and if it met the 'str' which we're
issuing in the mid, it'll print that index value.
rfind : it will start from reverse order and The rfind() method returns the highest index of the substring (if found).
if not found, it returns -1.
'''

a= 'Python is an interpreter language and it is an elite language for best applications'

a.find('is') # not mentioning any starting or ending index values, will begin from initial.

a.find('is',0,30) # mentioning the starting and ending index values

a.find('is',30,0) # will not work. reversing isn't possible

a.rfind('is') # finding the highest index of substring (from reverse search will happen)


---------------------------------------------------------------------
# List slicing
--------------------------------------------------------------------
a='Mathematics'

a[0]
a[5]
a[-1]
a[-3]
a[0:2]

a[1:5]
a[0:]
a[:11]

a[::-1]    # Reversing the string

a[-1:-4]   # Reversing is not possible in slicing(will print empty list)

a[-1:3]   # Reversing is not possible in slicing(will print empty list)

a[3:-3]  # This will be possible because this action is happening towards the positive way

a[-3:-2]  # This will be possible because this action is happening towards the positive way

a[:-4]

a[-1:]

a[:]

a[::]   # will print complete string

a[:len(a)]

a[len(a)-2:len(a)]

a[a.index(min(a)):len(a)]

# Interval

l1=[1,2,4,5,8,9,8,5]

l1[0:6:1]

l1[0:5:2]

l1[0:5:-1]

l1[5:0:-1]


---------------------------------------------------------------------------
# CALL BY VALUE AND CALL BY REFERENCE
--------------------------------------------------------------------------

a=b=c= 100

b=20 # changing the b value

c = 5 # changing the c value too

# if you check 'a' value, it'll remain with 100. so this is eg. for call by value.

# HERE,

a=b=c=[1,4,7,9,4,5]

b.append(100) # appending a value into the b list

# if you check 'a' and 'c', all the values would be updated with the value of 100. This is eg. for call by reference.

--------------------------------------------------------------------------------------------

# SORTING ALGORITHM

from operator import itemgetter
l1=[1,2,3,4,5]
l1=[(1,0),(10,4),(5,7),(2,10)]
print sorted(l1, key=itemgetter(1),reverse=True)

---------------------------------------------

# SORTING EXAMPLE CODE

for i in range(len(l1)):
	for j in range(i+1, len(l1)):
		if l1[i]>l1[j]:
			new = l1[j]
			l1[j] = l1[i]
			l1[i] = new

--------------------------------------------------














