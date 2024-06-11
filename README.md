
In Python, data types are the classification of data items. Python has various data types that are used to define the operations possible on them and the structure in which the data can be stored. Here are some examples of different data types in Python:

### 1. **Numeric Types**
   - **Integer**: Whole numbers, positive or negative, without decimals.
     ```python
     a = 10
     b = -20
     ```
   - **Float**: Numbers, positive or negative, containing one or more decimals.
     ```python
     c = 10.5
     d = -20.3
     ```
   - **Complex**: Numbers written with a "j" as the imaginary part.
     ```python
     e = 2 + 3j
     f = -5j
     ```

### 2. **Sequence Types**
   - **String**: A sequence of characters.
     ```python
     g = "Hello, World!"
     h = 'Python is fun'
     ```
   - **List**: An ordered collection of items, which can be of different types.
     ```python
     i = [1, 2, 3, 4]
     j = ["apple", "banana", "cherry"]
     k = [1, "apple", 3.5]
     ```
   - **Tuple**: An ordered collection of items, which can be of different types, and is immutable.
     ```python
     l = (1, 2, 3, 4)
     m = ("apple", "banana", "cherry")
     n = (1, "apple", 3.5)
     ```

### 3. **Mapping Type**
   - **Dictionary**: A collection of key-value pairs.
     ```python
     o = {"name": "John", "age": 30}
     p = {1: "one", 2: "two", 3: "three"}
     ```

### 4. **Set Types**
   - **Set**: An unordered collection of unique items.
     ```python
     q = {1, 2, 3, 4}
     r = {"apple", "banana", "cherry"}
     ```
   - **Frozen Set**: An immutable version of a set.
     ```python
     s = frozenset({1, 2, 3, 4})
     t = frozenset({"apple", "banana", "cherry"})
     ```

### 5. **Boolean Type**
   - **Boolean**: Represents one of two values: `True` or `False`.
     ```python
     u = True
     v = False
     ```

### 6. **Binary Types**
   - **Bytes**: Immutable sequences of bytes.
     ```python
     w = b"Hello"
     ```
   - **Byte Array**: Mutable sequences of bytes.
     ```python
     x = bytearray(5)
     ```
   - **Memory View**: A memory view object exposes the buffer interface to Python objects, allowing code to access the internal data of an object that supports the buffer protocol without copying.
     ```python
     y = memoryview(bytes(5))
     ```

### Examples in Use:
Here's a small Python script demonstrating the use of different data types:

```python
# Numeric Types
integer_num = 42
float_num = 3.14159
complex_num = 1 + 2j

# Sequence Types
string_data = "Hello, Python!"
list_data = [1, 2, "three", 4.0]
tuple_data = (1, 2, 3)

# Mapping Type
dict_data = {"key1": "value1", "key2": "value2"}

# Set Types
set_data = {1, 2, 3, 4}
frozenset_data = frozenset([1, 2, 3, 4])

# Boolean Type
bool_data = True

# Binary Types
bytes_data = b"Hello"
bytearray_data = bytearray(b"Hello")
memoryview_data = memoryview(bytearray(b"Hello"))

print(f"Integer: {integer_num}")
print(f"Float: {float_num}")
print(f"Complex: {complex_num}")

print(f"String: {string_data}")
print(f"List: {list_data}")
print(f"Tuple: {tuple_data}")

print(f"Dictionary: {dict_data}")

print(f"Set: {set_data}")
print(f"Frozenset: {frozenset_data}")

print(f"Boolean: {bool_data}")

print(f"Bytes: {bytes_data}")
print(f"Bytearray: {bytearray_data}")
print(f"Memoryview: {memoryview_data}")
```

These examples cover the basic and commonly used data types in Python, helping you understand the variety of data structures available for your programming needs.