#/usr/bin/python3.9
"""
# size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

# size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

# size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
"""


def print_rangoli(size):

    # your code goes here

    width = size * 4 - 3
    print(width)
    string_ = ''
    for i in range(1, size+1):
    	for j in range(0, i):
    		string_ += chr(96+size-j)
    		if len(string_) < width:
    			string_ += '-'

    	for k in range(i-1, 0, -1):
    		string_ += chr(97+size-k)
    		if len(string_) < width:
    			string_ += '-'

    	print(string_.center(width, '-'))
    	string_ = ''

    for i in range(size-1, 0, -1):
    	string_ = ''
    	for j in range(0,i):
    		string_ += chr(96+size-j)
    		if len(string_) < width:
    			string_ += '-'

    	for k in range(i-1, 0, -1):
    		string_ += chr(97+size-k)
    		if len(string_) < width:
    			string_ += '-'

    		
    	print(string_.center(width, '-'))

if __name__ == "__main__":
	print_rangoli(5)
