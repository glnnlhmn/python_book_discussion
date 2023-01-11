# python data types - very basic examples

# Integer
x = 1
print(type(x))  # <class 'int'>

# Float
x = 3.14
print(type(x))  # <class 'float'>

# String
x = 'Hello, World!'
print(type(x))  # <class 'str'>

# Boolean
x = True
print(type(x))  # <class 'bool'>

# List
x = [1, 2, 3]
print(type(x))  # <class 'list'>

# Tuple
x = (1, 2, 3)
print(type(x))  # <class 'tuple'>

# Set
x = {1, 2, 3}
print(type(x))  # <class 'set'>

# Dictionary
x = {'a': 1, 'b': 2, 'c': 3}
print(type(x))  # <class 'dict'>

# Complex number
x = 3 + 4j
print(type(x))  # <class 'complex'>

# Byte
x = b'Hello'
print(type(x))  # <class 'bytes'>

# Bytearray
x = bytearray(b'Hello')
print(type(x))  # <class 'bytearray'>

# Range
x = range(5)
print(type(x))  # <class 'range'>
# Frozen set
x = frozenset({1, 2, 3})
print(type(x))  # <class 'frozenset'>

# None
x = None
print(type(x))  # <class 'NoneType'>


# Function
def foo():
    pass


x = foo
print(type(x))  # <class 'function'>


# Class
class Foo:
    pass


x = Foo()
print(type(x))  # <class '__main__.Foo'>

# Module
import math

x = math
print(type(x))  # <class 'module'>


# Generator
def foo():
    for i in range(5):
        yield i


x = foo()
print(type(x))  # <class 'generator'>

# Type
x = int
print(type(x))  # <class 'type'>

# MemoryView
x = memoryview(b'Hello')
print(type(x))  # <class 'memoryview'>

# Enumerate
fruits = ['apple', 'banana', 'mango']
x = enumerate(fruits)
print(type(x))  # <class 'enumerate'>

# Zip
fruits = ['apple', 'banana', 'mango']
colors = ['red', 'yellow', 'green']
x = zip(fruits, colors)
print(type(x))  # <class 'zip'>


# Property
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


x = C()
print(type(x.x))  # <class 'property'>


# Callable
def foo():
    pass


x = callable(foo)
print(type(x))  # <class 'bool'>

# Reversed
x = reversed('hello')
print(type(x))  # <class 'reversed'>

# Slice
x = slice(1, 5)
print(type(x))  # <class 'slice'>

# collections.deque
import collections

x = collections.deque()
print(type(x))  # <class 'collections.deque'>

# struct.Struct
import struct

x = struct.Struct('i')
print(type(x))  # <class 'struct.Struct'>

# array.array
import array

x = array.array('i', [1, 2, 3])
print(type(x))  # <class 'array.array'>

# heapq.heap
import heapq

x = []
heapq.heappush(x, 3)
heapq.heappush(x, 2)
heapq.heappush(x, 1)
print(type(x))  # <class 'list'>

x = memoryview(b'Hello')
print(type(x))  # <class 'memoryview'>

x = callable(foo)
print(type(x))  # <class 'bool'>

x = reversed('hello')
print(type(x))  # <class 'reversed'>

x = slice(1, 5)
print(type(x))  # <class 'slice'>

x = frozenset({1, 2, 3})
print(type(x))  # <class 'frozenset'>
