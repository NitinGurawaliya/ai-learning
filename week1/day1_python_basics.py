# 🐍 DAY 1: Python Basics - Your AI Foundation
# =============================================

print("🚀 Welcome to Day 1 of your AI Learning Journey!")
print("Today we'll master Python fundamentals that power all AI/ML work.\n")

# ============================================================================
# 1. VARIABLES & DATA TYPES
# ============================================================================

print("📚 SECTION 1: Variables & Data Types")
print("-" * 50)

# Numbers
age = 25                    # Integer
height = 5.9               # Float
print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")

# Strings
name = "AI Learner"
print(f"Name: {name} (type: {type(name)})")

# Booleans
is_student = True
print(f"Is student: {is_student} (type: {type(is_student)})")

# Lists in Python are mutable (changeable) and ordered collections of items.
# Here, we create a list of fruits:
fruits = ["apple", "banana", "orange"]  # Initial list with three fruits

# We can add new items to a list using the .append() method:
fruits.append("grape")  # Adds "grape" to the end of the list

# Print the updated list to see all the fruits:
print(f"Fruits list: {fruits}")  # Output: Fruits list: ['apple', 'banana', 'orange', 'grape']

# We can also remove items from a list using the .remove() method:
fruits.remove("banana")  # Removes "banana" from the list

# Print the updated list to see the changes:
print(f"Fruits list: {fruits}")  # Output: Fruits list: ['apple', 'orange', 'grape']

# Dictionaries in Python are mutable (changeable) and unordered collections of key-value pairs.
# Here, we create a dictionary of a person's information:
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# We can access the value associated with a key using square brackets:
print(f"John's age: {person['age']}")  # Output: John's age: 30

# We can also add new key-value pairs to a dictionary using square brackets:
person["email"] = "john@example.com"  # Adds "email" key with value "john@example.com"

# Print the updated dictionary to see the changes:
print(f"Person dict: {person}")  # Output: Person dict: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}

# We can also remove key-value pairs from a dictionary using the .pop() method:
person.pop("city")  # Removes "city" key from the dictionary

# Print the updated dictionary to see the changes:
print(f"Person dict: {person}")  # Output: Person dict: {'name': 'John', 'age': 30, 'email': 'john@example.com'}

# Sets in Python are unordered collections of unique items.
# Here, we create a set of numbers:
unique_numbers = {1, 2, 2, 3, 4, 4, 5}  # Creates a set with the numbers 1 through 5

# Print the set to see the unique numbers:
print(f"Unique numbers: {unique_numbers}")  # Output: Unique numbers: {1, 2, 3, 4, 5}

# We can also add new items to a set using the .add() method:
unique_numbers.add(6)  # Adds 6 to the set

# Print the updated set to see the changes:
print(f"Unique numbers: {unique_numbers}")  # Output: Unique numbers: {1, 2, 3, 4, 5, 6}

# We can also remove items from a set using the .remove() method:
unique_numbers.remove(2)  # Removes 2 from the set

# Print the updated set to see the changes:
print(f"Unique numbers: {unique_numbers}")  # Output: Unique numbers: {1, 3, 4, 5, 6}

# Tuples in Python are immutable (unchangeable) and ordered collections of items.
# Here, we create a tuple of coordinates:       
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

print("\n" + "="*60 + "\n")

# ============================================================================
# 2. LOOPS & CONDITIONALS
# ============================================================================

print("🔄 SECTION 2: Loops & Conditionals")
print("-" * 50)

# For loop with list
print("\nIterating through fruits:")
for fruit in fruits:
    print(f"  I like {fruit}")

# For loop with range
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(f"  Number: {i}") # Output: Number: 1, Number: 2, Number: 3, Number: 4, Number: 5

# For loop with dictionary
print("\nIterating through person:")
for key, value in person.items():
    print(f"  {key}: {value}")  # Output: name: John, age: 30, email: john@example.com

# For loop with set
print("\nIterating through unique_numbers:")
for num in unique_numbers:
    print(f"  Number: {num}")  # Output: Number: 1, Number: 3, Number: 4, Number: 5, Number: 6

# For loop with tuple
print("\nIterating through coordinates:")
for coord in coordinates:
    print(f"  Coordinate: {coord}")  # Output: Coordinate: 10, Coordinate: 20

# For loop with range
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(f"  Number: {i}") # Output: Number: 1, Number: 2, Number: 3, Number: 4, Number: 5

# While loop
print("\nWhile loop countdown:")
count = 3
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  Blast off! 🚀")

# List comprehension with condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"\nEven numbers: {even_numbers}")

print("\n" + "="*60 + "\n")

# ============================================================================
# 3. FUNCTIONS
# ============================================================================

print("⚙️ SECTION 3: Functions")
print("-" * 50)

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("AI Learner"))

# Function with multiple parameters
def calculate_area(length, width):
    area = length * width
    return area

print(f"Rectangle area: {calculate_area(5, 3)}")

# Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print(f"5 squared: {power(5)}")
print(f"2 cubed: {power(2, 3)}")

# Function with multiple return values
def analyze_number(num):
    square = num ** 2
    is_even = num % 2 == 0
    return square, is_even

result_square, result_even = analyze_number(7)
print(f"7 squared: {result_square}, is even: {result_even}")

print("\n" + "="*60 + "\n")

# ============================================================================
# 4. OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================================================

print("🏗️ SECTION 4: Object-Oriented Programming")
print("-" * 50)

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, studying {self.major}"
    
    def study(self, subject):
        return f"{self.name} is studying {subject}"
    
    def birthday(self):
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}"

# Create student objects
student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 22, "Mathematics")

print(student1.introduce())
print(student2.introduce())
print(student1.study("Python"))
print(student1.birthday())

print("\n" + "="*60 + "\n")

# ============================================================================
# 5. NUMPY BASICS (Essential for AI/ML)
# ============================================================================

print("🔢 SECTION 5: NumPy Basics")
print("-" * 50)

try:
    import numpy as np
    print("✅ NumPy imported successfully!")
    
    # Creating arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    
    print(f"1D array: {arr1}")
    print(f"2D array:\n{arr2}")
    print(f"Array shape: {arr2.shape}")
    print(f"Array dimensions: {arr2.ndim}")
    
    # Array operations
    print(f"\nArray operations:")
    print(f"Original: {arr1}")
    print(f"Doubled: {arr1 * 2}")
    print(f"Squared: {arr1 ** 2}")
    print(f"Sum: {np.sum(arr1)}")
    print(f"Mean: {np.mean(arr1)}")

    # Slicing
    # Slicing in NumPy arrays allows you to extract specific parts of an array.
    # The syntax is similar to Python lists: arr[start:stop:step]
    print(f"\nSlicing examples:")

    # Get the first 3 elements (indices 0, 1, 2)
    print(f"First 3 elements: {arr1[:3]}")  # Output: [1 2 3]

    # Get the last 3 elements of the array.
    # arr1[-3:] means "start from the third-to-last element and go to the end"
    print(f"Last 3 elements: {arr1[-3:]}")  # Output: [3 4 5]

    # Get every other element (step of 2)
    print(f"Every other element: {arr1[::2]}")  # Output: [1 3 5]

    # Explanation:
    # - arr1[:3] means "from the start up to (but not including) index 3"
    # - arr1[-3:] means "from the third-to-last element to the end"
    # - arr1[::2] means "from start to end, take every second element"
    
    # Broadcasting
    print(f"\nBroadcasting example:")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    result = matrix + 10
    print(f"Matrix + 10:\n{result}")
    
except ImportError:
    print("❌ NumPy not installed. Run: pip install numpy")

print("\n" + "="*60 + "\n")

# ============================================================================
# 🎯 PRACTICE PROJECT: Square & Filter Even Numbers
# ============================================================================

print("🎯 PRACTICE PROJECT: Square & Filter Even Numbers")
print("-" * 50)

def square_and_filter_even(numbers):
    """
    Take a list of numbers, square each, and return only the even results.
    
    Args:
        numbers (list): List of integers
        
    Returns:
        list: List of squared even numbers
    """
    # Step 1: Square each number
    squared = [num ** 2 for num in numbers]
    print(f"Step 1 - Squared numbers: {squared}")
    
    # Step 2: Filter to keep only even numbers
    even_squared = [num for num in squared if num % 2 == 0]
    print(f"Step 2 - Even squared numbers: {even_squared}")
    
    return even_squared

# Test the function
test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Input numbers: {test_numbers}")
result = square_and_filter_even(test_numbers)
print(f"Final result: {result}")

# Let's verify the math:
print("\nVerification:")
for num in test_numbers:
    squared = num ** 2
    is_even = squared % 2 == 0
    status = "✓" if is_even else "✗"
    print(f"  {num}² = {squared} {'(even)' if is_even else '(odd)'} {status}")

print("\n" + "="*60 + "\n")

# ============================================================================
# 🧪 EXTRA PRACTICE EXERCISES
# ============================================================================

print("🧪 EXTRA PRACTICE EXERCISES")
print("-" * 50)

print("Try these exercises to reinforce your learning:")
print("1. Create a function that finds the maximum number in a list")
print("2. Write a function that counts vowels in a string")
print("3. Create a class 'Rectangle' with methods to calculate area and perimeter")
print("4. Use NumPy to create a 3x3 identity matrix")
print("5. Write a function that reverses a string")

print("\n" + "="*60 + "\n")

# ============================================================================
# 📝 SUMMARY & NEXT STEPS
# ============================================================================

print("📝 DAY 1 SUMMARY")
print("-" * 50)

print("✅ What you learned today:")
print("  • Variables, data types, and data structures")
print("  • Control flow with loops and conditionals")
print("  • Function definition and usage")
print("  • Object-oriented programming basics")
print("  • NumPy arrays and operations")
print("  • List comprehensions and functional programming")

print("\n🎯 Key concepts for AI/ML:")
print("  • Lists and dictionaries for data manipulation")
print("  • Functions for code organization and reusability")
print("  • NumPy arrays for numerical computations")
print("  • OOP for building complex systems")

print("\n🚀 Tomorrow: Python for Data & APIs (Pandas, Matplotlib, APIs)")
print("Get ready to work with real data and create visualizations!")

print("\n" + "="*60)
print("🎉 Congratulations on completing Day 1! 🎉")
print("You've built a solid Python foundation for your AI journey!")
