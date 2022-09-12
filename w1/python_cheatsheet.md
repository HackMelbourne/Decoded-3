<h1 align="center">Xin Yu's COMP10001 Python Notes</h1>

> You don't need to know everything in this document to create the Discord Bot - just skim through the document to
> remmind yourself of Python's Syntax

---
<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

- [Printing & Inputting](#printing--inputting)
- [Commenting](#commenting)
- [Operators (Highest to Lowest precedence)](#operators-highest-to-lowest-precedence)
- [Conditionals](#conditionals)
- [While Loop](#while-loop)
    - [For loop](#for-loop)
- [Functions](#functions)
- [Files](#files)
- [`csv` Library](#csv-library)
- [Iterators](#iterators)
    - [Iterators VS Sequences](#iterators-vs-sequences)
- [`itertools` Library](#itertools-library)
- [Unpacking](#unpacking)
- [Data Types](#data-types)
    - [Integer](#integer)
    - [String](#string)
    - [Float](#float)
    - [Boolean](#boolean)
    - [List](#list)
    - [Tuple](#tuple)
    - [Dictionary](#dictionary)
        - [Default Dictionaries](#default-dictionaries)
        - [Unpacking Dictionaries:](#unpacking-dictionaries)
    - [Set](#set)
- [Errors](#errors)
- [Statements and Expressions](#statements-and-expressions)
- [Extra](#extra)
    - [`pillow` Library](#pillow-library)
    - [Data Science](#data-science)
        - [`matplotlib` LIbrary](#matplotlib-library)

</details>

---

## Printing & Inputting

- `print(object)` displays object to user
- `input(str)` displays str to user and asks user for input

## Commenting

- `# hello` single line comment
- `'''hello'''` or `"""hello"""` docstring/multi-line comment

---

## Operators (Highest to Lowest precedence)

- Arithmetic Operators
    - `()` brackets
    - `**` exponent
    - `%` modulus/remainder
    - `//` floor/integer division
    - `/` division
    - `*` multiplication
    - `-` subtraction (also a unary operator; make number negative)
    - `+` addition (also a unary operator; make number positive)
- Comparison Operators
    - `==` equal to
    - `!=` not equal to
    - `<` less than
    - `>` greater than
    - `<=` less than or equal to
    - `>=` more than or equal to
    - `in`
- Boolean Operators
    - `not`
    - `and`
    - `or`

---

## Conditionals

```python
if <condition1>:
  <statements/operations to be executed if condition1 is True>
elif <condition2>:
  <statements/operations to be executed if condition2 is True>
...
elif <conditionx>:
  <statements/operations to be executed if conditionx is True>
else:
  <statements/operations to be executed if all conditions are False>
```

---

## While Loop

```python
while <condition>:
  <statements/operations to be executed while condition is True>
```

- `break` immediately exists while loop
- `continue` jumps back to start of loop

### For loop

```python
# with range()
for i in range(<int>):
  <statements/operations to be executed if i is less than <int>>

# iterate over sequence (str/list/tuple)
for i in <sequence>:
  # i will become the char/ele
```

---

## Functions

```python
CONSTANT = 0 # declare constants before all functions
def <function-name>(<parameters>):
  <function-body>
```

---

## Files

- `fp = open(filename, mode)` opens file
    - `r` read (default)
    - `w` write
    - `a` append
- `fp = open(new-filename, 'w'/'a')` creates new file to write or append to
- `fp.read()` return entire contents of file as a single string
- `fp.readline()` returns a single line of text as a string
- `fp.readlines()` return entire contents of file as list of strings (one per line)
- `fp.write(str)` write str to fp, appending it to whatever is currently there
- `fp.writelines(str_list)` writes each string in str_list as separate lines to the file
- `fp.close()` closes file *important: must always be done once finished using file
- `with open(filename) as name: ` opens file as name; file can only be accessed within the code block; file is closed
  automatically on exiting code block

## `csv` Library

- CSV: Comma-Separated Values - represents tabular data
- `import csv` imports csv module
- `fp = open('filename.csv', mode)` opens csv file
- `reader = csv.reader(fp)` returns a csv reader object
    - can be iterated through
- `reader.next(fp)` return the next parsed line from fp as a list
- `csv.DictReader(open("filename.csv", mode))` returns list of dictionaries for each row
- `csv.writer()` returns a csv writer object
- `.writerows(2d-data)` expects a two-dimensional data representation as input, and writes that data to the file in CSV
  format
- `writerow(list)` writes a single CSV row

```python
import csv
csvdata = csv.reader(open('filename.csv'))

# iterate through rows
for row in csvdata:
  print(row)
#['header', 'row']
#['value', 'value']
#['value', 'value']

with open('filename.csv') as fp:
  my_reader = reader(fp)
  print(list(my_reader))
#[['header', 'row'], ['value', 'value'], ['value', 'value']...]

# DictReader
csvdata = csv.DictReader(open('filename.csv'))
for row in csvdata:
  print(row)
#OrderedDict([('header', 'row'), ('value', ' value'), ('value', ' value')])
```

---

## Iterators

- `iterator = iter(str/list/tuple/set/dict)` initialize iterator
- `next(iterator)` returns next char/elem/key
- **there is no way to more backward**

### Iterators VS Sequences

||Iterators|Sequences|
|:--:|:--:|:--:|
|Random Access|No random access|Has random acces<br>(you can access any element in the sequence, as many times as you
like)|
|Position Tracking|Remembers where you are up to|No position tracking within the sequence|
|`len()`|cannot use|can use|
|Finity|Can be Infinite|Must be finite|
|Transverse|Can only transverse once, forwards|can transverse it many times|

## `itertools` Library

- `from itertools import permutations, combinations, product ...`
- `permutations(str/tuple/list/set/dict, r)` returns r-length tuples of permutations
- `combinations(str/tuple/list/set/dict, r)` returns r-length tuples of combinations
- `product(p, q, r, ...)` returns tuples of combination of p, q, r...; length of tuples = number of arguments
- `cycle(str/tuple/list/set/dict)` returns an infinite iterators that cycles through char/elem/keys
- `groupby(str/tuple/list/set/dict, key(lambda criteria))` returns an iterator which generates 2-tuples: (group,
  elements-of-group)

## Unpacking

```python
# unpacking tuple
p0, p1 = (1, 2)

# unpacking dictionary
d = {}
for key, value in d:
  print(value, key)

# unpacking permutations
from itertools import permutations
for p0, p1 in permutations ("ABC", 2):
    print(p0, p1)
```

---

## Data Types

### Integer

- `int(value)` convert value to **integer** (whole number)

### String

- `str(value)` convert value to **string** (chunk of text)
    - `str + str` string concatenation
    - `str * int` string replication
    - `str[index]` string indexing
    - `str[start-index:end-index:step]` string slicing (does not include end-index btw)
    - `str.upper()` make all uppercase
    - `str.lower()` make all lowercase
    - `str.strip(str)`
    - `str.split(str)` return a list of string-delimited substrings in string
    - f-strings
        - `f'string {variable/operation/etc.}'`
        - `f'{val : filling align window .precision format-code}'` format specifier
            - eg: `f'A float: {4.35:0<5.5f}'`
            -
          |Part|Explanation|
          |:--:|:--:|
          |`:`|Specifies value from format specifier|
          |`filling` (char)|fills extra space with filling (default=spaces)|
          |`<` left<br>`^` middle<br>`>` right<br>`,` thousand-separatign commas|aligns formatted text to the
          left/middle/right (default=right)|
          |`window` (int)|sets formatted windoe to be int characters long(default=length of fomatted value)|
          |`.precision` (int)|formats the number to int decimal places // indicates number of characters in string|
          |`f` float<br>`s` string<br>`g` 'optimal' float<br>`d` integer<br>`c` Unicode character|(default=auto)|

### Float

- `float(value)` convert value to **float** (real number)

### Boolean

- `bool(value)` convert value to **boolean** (truth value)

### List

- `list(value)` convert value to **list**
    - mutable
    - sequence of values
    - values can be different types
    - `list(range(start, end, step))` returns a list from start to end (end not included)
    - `list[index]` index can be positive (start from 0) or negative (start from -1)
    - `list[start-index: end-index: step-size]` returns elements from start-index to end-index (end-index not included)
    - `list.append(item)` append/add item to a list
    - `list.remove(item)` remove first instance of item from list
    - `list.pop(index)` remove item of index
    - `mylist.insert(index, item)` insert item in specific index in list - other items are moved backward

### Tuple

- `tuple(value)` convert *iterable* value (list, tuple, string) to **tuple**
    - immutable
    - sequence of values
    - values can be different types

### Dictionary

- `d = {}` or `d = dict()` initilize dictionary
- `dict(value)` convert to **dictionary**
- collection of key and associated values
- keys must be unique
- values can be of different types
- Methods/Operations
    - `d[key]` access value associated to key - returns `KeyError` if key doesn't exist
    - `d.get(key)` returns value associated with key - returns `None` if key doesn't exist
    - `key in d` test for presence of key
    - `d.pop(key, no-key-value)` deletes the key-value pair and returns the value or returns no-key-value if key does
      not exist (default=None)
    - `del d[key]` deletes key-value pair
    - `d.copy()` makes a shallow copy of dictionary
    - `d.clear()` deletes all key-value pairs from the dictionary
- Iterables
    - `d.keys()` returns iterable collection of keys
    - `d.values()` returns iterable collection of values
    - `d.items()` returns iterable collection of 2-tuples (key, value)
    - `list(d)` same as `list(d.keys())`

#### Default Dictionaries

- `from collections import defaultdict (*as dd)` import default dictionary, *optional
- `d = defaultdictd(value-data-type)`
- Why better than dictionary?
    - Default dictionaries are useful because, when queried with a key which is not yet in the dictionary, rather than
      raising a `KeyError`, the default dictionary adds it as a new entry, with its value set to a default value.

#### Unpacking Dictionaries:

```python
my_dict = {'first': 1, 'second': 2, 'third': 3}
for key, value in my_dict.items():
    print(key, value)
# first 1
# second 2
# third 3
```

### Set

- stores unique data (removes duplicates)
- elements must be immutable type
- *unordered* collection
- `set(value)` convert to set // initialize a set
- `set.pop()` remove and retrieve a random element
- `set.remove(ele)` removes specific element
- `set1.intersect(set2)` or `set1 & set2` returns new set containing common elements between sets
- `set1.union(set2)` or `set1 | set2` returns new set containing all unique elements from both sets
- `set1.difference(set2)` or `set1 - set2` returns new set containing difference between sets
- `set.copy()`
- `set.clear()`
- `set.issubset`


- `len(str/list/tuple/set/dict)` used to find number of characters in a string or elements in a list/tuple/set or number
  of key-value pairs in a dict
- `sorted(str/list/tuple/set, reverse = True/False)` returns list of sorted characters/elements
    - `sorted(str/list/tuple/set, key=lambda x: x[])`
    - `sorted(str/list/tuple/set, key=lambda x: (x[], x[]))`
- `list.sort(list)` sorts (mutates) the list
- `type(object)` find out type of object
- `chr(int)` convert integer to corresponding Unicode character
- `ord(char)` convert Unicode character to Unicode code
- `substring/elem in string/list/tuple/set` check if substring is in a string or if an element is in a list/tuple/set
- `id(object)` returns id of object

---

## Errors

- `SyntaxError`
    - detected before you run
  ``` python
  >>> a +
    File "<stdin>", line 1
      a +
        ^
  SyntaxError: invalid syntax
  >>> if:
    File "<stdin>", line 1
      if:
        ^
  SyntaxError: invalid syntax
  >>> [1:2]
    File "<stdin>", line 1
      [1:2]
        ^
  SyntaxError: invalid syntax
  >>> unless True:
    File "<stdin>", line 1
      unless True:
            ^
  SyntaxError: invalid syntax
  >>> if 1 = 2:
    File "<stdin>", line 1
      if 1 = 2:
          ^
  SyntaxError: invalid syntax
  >>>     a = 1
    File "<stdin>", line 1
      a = 1
  IndentationError: unexpected indent
  ```
- `Runtime Error`
    - detected while running
  ```python
  >>> a = b
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'b' is not defined

  >>> [][1]
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  IndexError: list index out of range

  >>> int("zero")
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: invalid literal for int() with base 10: 'zero'
  
  >>> int([])
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
  
  >>> {}['a']
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  KeyError: 'a'
  ```
- `Logic Error` the intended output is not the same as actual output
    - detected after running
- `TypeError`
- `IndexError`
- `StopIteration` exception that is raised when the iterator runs out of objects to iterate over

---

## Statements and Expressions

- Expression: some code which generates an object
- Simple Expression: contains 1 operator
- Complex Expression: has more parts than a simple expression
- Logical Expression: evaluates to bool
- Statement: any valid line of Python code

|Code|Exp.|Simple Exp.|Complex Exp.|Logical Exp.|Statement|
|--|--|--|--|--|--|
|`1+2`|✅|✅|||✅|
|`var=1+2`|||||✅|
|`-(2)`|✅|✅|||✅|
|`True or False`|✅|✅||✅|✅|
|`1<3 or 3!=3`|✅||✅|✅|✅|
|`def my_func():`|||||✅|

---

## Extra

### `pillow` Library

- `import PIL.Image as pim` make pillowtools available in your program
- `image = pim.open(filename)` opens filename and returns an object of Image datatype
- `image = pim.new(mode, size, bg_colour)` creates new blank image and returns an object of Image datatype
  |field|details|
  |:--:|:--:|
  |mode|`"1"` black and white images<br>`"L"` greyscale images<br>`"RGB"` colour images|
  |size|2-tuple`(width, height)`|
  |bg_colour|`0` black // `1` white<br>`int_between_0-255(inclusive)` 0 for black, 255 for white<br>`(R, G, B)` between
  0-255(inclusive)|
- `image.mode` returns the image's mode
- `image.size` returns image's size (2-tuple)
- `image.getpixel(address)` address is 2-tuple
- `image.putpixel(address, colour)`
- `image.save(filename)`
- Effects and transformations

### Data Science

- big data problems
- 4 broad steps
    1. data wrangling
    2. data visualisation
    3. data analysis
    4. empirical evaluation

#### `matplotlib` LIbrary

- `import matplotlib.pyplot as plt`

- `ax = plt.axes()` generate aces to draw on
- `ax.bar(locations, heights, width)` draw bar chart within an axes` object
    - `locations` (list) the locations of the lower left corners of the bars
    - `heights` (list) their respective heights
    - `width` (list) width of the bars
- `ax.set_title(str)` set title
- `ax.set_ylabel(str)` set y label
- `ax.set_xlabel(str)` set x label (opt)
- `ax.set_xticks(list)` set position of labls on x axis
- `ax.set_xticklabels(labels_list)` set the labels to the contents of labels_list
- `plt.show()`
- save plot:
  ```
  # at the top
  import matplotlib
  matplotlib.use('Svg')
  from pylab import *

  # ...
  # your program
  # ...

  # directly after plotting
  savefig('thing1.svg')
  ```