# Python Labs (Ngoprek): Data Types

## Prerequisite
- 1 cpu and 2GB RAM
- Ubuntu OS
- Internet connection

## Instructions

In this episode we will discuss about the fundamental concepts in Python programming: data types. Whether you're new to programming or looking to solidify your understanding, grasping the different data types in Python is crucial. Data types define the kind of data that can be stored and manipulated within a program. From numbers to text, from collections to custom objects, Python offers a rich variety of data types to cater to diverse programming needs. In this session, we'll explore the most commonly used data types in Python, understand their characteristics, and see how to use them effectively through practical examples. So, let's dive in and unravel the building blocks of data that power your Python programs!

### Integer
```python
# Integer: Whole numbers without a decimal point
x = 10
y = -5
print(f"x: {x}, y: {y}")
print(f"Type of x: {type(x)}, Type of y: {type(y)}")
```
**Explanation:** Integers in Python represent whole numbers without a decimal point. Here, `x` is assigned the value 10, and `y` is assigned -5. The `type()` function confirms that both are of type `int`.

### Float
```python
# Float: Numbers with a decimal point
a = 3.14
b = -2.71
print(f"a: {a}, b: {b}")
print(f"Type of a: {type(a)}, Type of b: {type(b)}")
```
**Explanation:** Floats represent numbers that have a decimal point. In this example, `a` is 3.14 and `b` is -2.71. The `type()` function shows that both variables are of type `float`.

### String
```python
# String: Sequence of characters enclosed in quotes
str1 = "Hello"
str2 = 'World'
str3 = """This is a 
multi-line string"""
print(f"str1: {str1}, str2: {str2}")
print(f"str3: {str3}")
print(f"Type of str1: {type(str1)}, Type of str2: {type(str2)}, Type of str3: {type(str3)}")
```
**Explanation:** Strings in Python are sequences of characters enclosed in quotes (single, double, or triple). `str1` and `str2` are single-line strings, while `str3` is a multi-line string. The `type()` function confirms that all are of type `str`.

### List
```python
# List: Ordered collection of elements, can be of mixed types
my_list = [1, 2, 3.5, "Python", True]
print(f"List: {my_list}")
print(f"First element: {my_list[0]}, Last element: {my_list[-1]}")
print(f"Type of my_list: {type(my_list)}")
```
**Explanation:** Lists are ordered collections of elements that can be of mixed types. `my_list` contains integers, a float, a string, and a boolean. Lists are mutable, meaning their elements can be changed. The `type()` function confirms that `my_list` is of type `list`.

### Tuple
```python
# Tuple: Ordered collection of elements, immutable
my_tuple = (10, 20, 30, "tuple")
print(f"Tuple: {my_tuple}")
print(f"First element: {my_tuple[0]}, Last element: {my_tuple[-1]}")
print(f"Type of my_tuple: {type(my_tuple)}")
```
**Explanation:** Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation. `my_tuple` contains integers and a string. The `type()` function confirms that `my_tuple` is of type `tuple`.

### Dictionary
```python
# Dictionary: Key-value pairs, unordered
my_dict = {"name": "Alice", "age": 25, "is_student": True}
print(f"Dictionary: {my_dict}")
print(f"Name: {my_dict['name']}, Age: {my_dict['age']}")
print(f"Type of my_dict: {type(my_dict)}")
```
**Explanation:** Dictionaries are collections of key-value pairs. They are unordered, meaning the items do not have a defined order. `my_dict` contains keys like "name", "age", and "is_student" with their respective values. The `type()` function confirms that `my_dict` is of type `dict`.

### Set
```python
# Set: Unordered collection of unique elements
my_set = {1, 2, 3, 3, 4}
print(f"Set: {my_set}")
print(f"Type of my_set: {type(my_set)}")
```
**Explanation:** Sets are unordered collections of unique elements. `my_set` contains the elements 1, 2, 3, and 4. The duplicate value 3 is automatically removed. The `type()` function confirms that `my_set` is of type `set`.

### Boolean
```python
# Boolean: Represents True or False
is_valid = True
has_error = False
print(f"is_valid: {is_valid}, has_error: {has_error}")
print(f"Type of is_valid: {type(is_valid)}, Type of has_error: {type(has_error)}")
```
**Explanation:** Booleans represent truth values: `True` or `False`. `is_valid` is assigned `True`, and `has_error` is assigned `False`. The `type()` function confirms that both are of type `bool`.

### NoneType
```python
# NoneType: Represents the absence of a value
nothing = None
print(f"Nothing: {nothing}")
print(f"Type of nothing: {type(nothing)}")
```
**Explanation:** `NoneType` represents the absence of a value. `nothing` is assigned `None`, which is used to signify that there is no value assigned. The `type()` function confirms that `nothing` is of type `NoneType`.

These examples illustrate the variety of data types available in Python and how they can be used in practice. Each example includes the creation of a variable of the given type, some operations or accesses to demonstrate its use, and a check of the variable's type.

### Complex Number
```python
# Complex: Complex numbers with real and imaginary parts
complex_num = 2 + 3j
print(f"Complex number: {complex_num}")
print(f"Real part: {complex_num.real}, Imaginary part: {complex_num.imag}")
print(f"Type of complex_num: {type(complex_num)}")
```
**Explanation:** Complex numbers have a real and an imaginary part. `complex_num` is assigned the value `2 + 3j`, where 2 is the real part and 3j is the imaginary part. The `type()` function confirms that `complex_num` is of type `complex`.

