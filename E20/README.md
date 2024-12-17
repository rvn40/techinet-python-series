# Python Labs (Ngoprek): Variables

Understanding how to declare and assign variables is crucial because they form the backbone of your code, allowing you to store and manipulate data efficiently. Think of variables as containers that hold values, which you can use and modify as your program runs. So, let's jump in and explore the ins and outs of working with variables in Python, with plenty of examples to illustrate each concept!

### Introduction

---

#### 1. **Introduction to Variables in Python**
   - **Definition of a Variable**
     - Example: `x = 10`
   - **Purpose of Variables**
     - Storing data, making code reusable and readable, etc.

#### 2. **Variable Declaration**
   - **Implicit Declaration**
     - Example: `name = "John"`
   - **Dynamic Typing**
     - Example: `age = 25`, `age = "Twenty Five"`

#### 3. **Variable Assignment**
   - **Basic Assignment**
     - Example: `pi = 3.14`
   - **Multiple Assignment**
     - Example: `a, b, c = 1, 2, 3`
   - **Swapping Variables**
     - Example: `a, b = b, a`

#### 4. **Types of Variables**
   - **Global Variables**
     - Example: 
       ```python
       global_var = "I am global"
       def example_function():
           print(global_var)
       ```
   - **Local Variables**
     - Example: 
       ```python
       def example_function():
           local_var = "I am local"
           print(local_var)
       ```
   - **Nonlocal Variables**
     - Example: 
       ```python
       def outer_function():
           outer_var = "outer"
           def inner_function():
               nonlocal outer_var
               outer_var = "inner"
           inner_function()
           print(outer_var)
       outer_function()
       ```

#### 5. **Variable Types and Type Casting**
   - **Different Data Types**
     - Integer: `num = 10`
     - Float: `pi = 3.14`
     - String: `name = "Alice"`
     - Boolean: `is_active = True`
   - **Type Casting**
     - Example: 
       ```python
       num = "100"
       num_int = int(num)
       ```

#### 6. **Variable Naming Conventions**
   - **Rules and Best Practices**
     - Use descriptive names
     - Start with a letter or underscore
     - Avoid using Python keywords
     - Example: 
       ```python
       student_name = "Alice"
       _counter = 1
       total_sum = 100
       ```

#### 7. **Immutable vs Mutable Variables**
   - **Immutable Types**
     - Strings, integers, floats, tuples
     - Example: 
       ```python
       name = "Alice"
       name = "Bob"  # Reassignment
       ```
   - **Mutable Types**
     - Lists, dictionaries, sets
     - Example: 
       ```python
       numbers = [1, 2, 3]
       numbers[0] = 10
       ```

#### 8. **Scope of Variables**
   - **Global Scope**
     - Example: 
       ```python
       x = "global"
       def my_func():
           print(x)
       my_func()
       ```
   - **Local Scope**
     - Example: 
       ```python
       def my_func():
           y = "local"
           print(y)
       my_func()
       ```

#### 9. **Constants in Python**
   - **Defining Constants**
     - By convention, constants are named in all uppercase
     - Example: `PI = 3.14`
   - **Using Constants**
     - Example: 
       ```python
       MAX_SPEED = 120
       print(MAX_SPEED)
       ```

#### 10. **Best Practices and Common Pitfalls**
   - **Avoiding Common Mistakes**
     - Overwriting variables
     - Example: 
       ```python
       x = 10
       x = "text"  # Overwriting
       ```
   - **Best Practices**
     - Use clear and meaningful names
     - Keep variable scope limited to where it is needed

#### 11. **Conclusion**
   - **Recap of Key Points**
     - Importance of proper variable declaration and assignment
     - Impact on code readability and maintainability
   - **Encouragement to Practice**
     - Experiment with variables in different scopes and types

---

