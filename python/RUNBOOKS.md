# IT Project Runbooks - Complete Directory Guide

This document provides comprehensive runbooks for each directory in the IT projects workspace, explaining the purpose, structure, and best practices for each area.

---

## Table of Contents
1. [bash/](#bash) - Bash scripting utilities
2. [classes/](#classes) - Object-oriented programming concepts
3. [dictionaries/](#dictionaries) - Dictionary data structure operations
4. [dir/](#dir) - Directory and file management
5. [exception/](#exception) - Exception handling patterns
6. [exercise/](#exercise) - Comprehensive coding exercises
7. [file/](#file) - File I/O operations
8. [list/](#list) - List data structure operations
9. [list-comprehension/](#list-comprehension) - List comprehension patterns
10. [loops/](#loops) - Loop structures and iterations
11. [mail/](#mail) - Email and data processing
12. [os-py/](#os-py) - Operating system interactions
13. [puppet/](#puppet) - Puppet infrastructure configuration
14. [recursion/](#recursion) - Recursive algorithm patterns
15. [resize_image/](#resize_image) - Image processing
16. [strings/](#strings) - String manipulation operations
17. [testing/](#testing) - Test case development
18. [tuple/](#tuple) - Tuple data structure operations
19. [web/](#web) - Web utilities and monitoring

---

## bash/
**Purpose:** Bash shell scripting utilities and commands

**Learning Path:**
- Basic shell commands and scripting
- File system navigation and manipulation
- Shell scripting best practices
- Automation through shell scripts

**When to Use:**
- Need to create shell automation scripts
- Working with Linux/Unix systems
- System administration tasks
- Cross-platform scripting scenarios

**Common Tasks:**
- Create executable shell scripts (.sh files)
- Understand shell variables and control flow
- Work with pipes and redirects
- Develop command-line tools

**Getting Started:**
1. Review existing bash scripts for patterns
2. Practice basic shell commands
3. Build simple automation scripts
4. Test scripts in shell environment

---

## classes/
**Purpose:** Object-oriented programming (OOP) concepts in Python

**Key Concepts:**
- Class definitions and constructors (`__init__`)
- Dunder methods (magic methods like `__init__`, `__str__`, `__repr__`)
- Instance attributes and methods
- Inheritance and encapsulation
- Special methods for class behavior

**Files Included:**
- `apple.py` - Basic class definition example with `__init__` constructor
- `method.md` - Documentation on class methods
- `special_methods.md` - Reference for dunder methods and magic methods

**Learning Path:**
1. Start with `apple.py` - understand class structure and `__init__`
2. Read `method.md` - learn about different method types
3. Explore `special_methods.md` - understand dunder methods
4. Create your own classes using these patterns

**Common Patterns:**
```python
class ClassName:
    def __init__(self, parameters):
        self.attribute = value
    
    def method(self):
        return self.attribute
```

**Best Practices:**
- Use clear, descriptive class names (PascalCase)
- Initialize all attributes in `__init__`
- Document class purpose and methods
- Use special methods for intuitive class behavior
- Follow Python conventions and style guidelines

---

## dictionaries/
**Purpose:** Dictionary (key-value mapping) operations and patterns

**Key Concepts:**
- Dictionary creation and access
- `.keys()` - retrieve all keys
- `.values()` - retrieve all values
- `.items()` - retrieve key-value pairs
- Dictionary updates and modifications
- Nested dictionaries

**Files Included:**
- `full_names.py` - Working with name data in dictionaries
- `items.py` - Using `.items()` method for key-value pairs
- `keys_values.py` - Basic `.keys()` and `.values()` operations
- `resources.py` - Managing resource data with dictionaries

**Learning Path:**
1. `keys_values.py` - Basic dictionary operations
2. `items.py` - Working with key-value pairs
3. `full_names.py` - Real-world name data handling
4. `resources.py` - Complex dictionary structures

**Common Operations:**
```python
# Create dictionary
data = {"key": "value"}

# Access methods
data.keys()        # All keys
data.values()      # All values
data.items()       # Key-value pairs
data.get("key")    # Safe access
data.update(...)   # Merge dictionaries
```

**When to Use:**
- Need to store and retrieve key-value pairs
- Working with JSON-like data
- Mapping relationships between data
- Configuration management

**Performance Note:** Dictionaries offer O(1) lookup time, making them ideal for fast data retrieval.

---

## dir/
**Purpose:** Directory listing and file operations

**Key Concepts:**
- Directory traversal
- File system operations
- Listing directory contents
- File path manipulation
- Working with os and pathlib modules

**Files Included:**
- `log-sample.py` - Sample log file operations
- `task-01.py` through `task-04.py` - Incremental difficulty tasks
- `test.py` - Testing file operations

**Learning Path:**
1. `log-sample.py` - Understand basic directory/file operations
2. `task-01.py` - Simple directory tasks
3. `task-02.py` - Intermediate directory operations
4. `task-03.py` - Advanced operations
5. `task-04.py` - Complex scenarios
6. `test.py` - Validation and testing

**Common Tasks:**
- List files in directory with `os.listdir()`
- Walk directory tree with `os.walk()`
- Get file information (size, date modified)
- Filter files by extension
- Create/delete directories

**Best Practices:**
- Use `pathlib.Path` for cross-platform paths
- Always handle errors with try-except
- Validate paths exist before operations
- Use context managers for file operations

---

## exception/
**Purpose:** Exception handling patterns and error management

**Key Concepts:**
- Try-except blocks
- Custom exception handling
- Raising exceptions
- Exception hierarchy
- Defensive programming

**Files Included:**
- `exemption-01.py` - Basic exception handling patterns
- `exemption-02.py` - Advanced exception scenarios
- `raise.py` - Raising custom exceptions

**Learning Path:**
1. `exemption-01.py` - Basic try-except patterns
2. `raise.py` - Creating and raising exceptions
3. `exemption-02.py` - Complex exception scenarios

**Common Patterns:**
```python
try:
    # Code that might raise exception
    result = risky_operation()
except SpecificException as e:
    # Handle specific exception
    print(f"Error: {e}")
except Exception as e:
    # Handle general exceptions
    print(f"Unexpected error: {e}")
finally:
    # Cleanup code (always runs)
    cleanup()
```

**When to Use:**
- Preventing program crashes
- Handling errors gracefully
- Logging errors for debugging
- Validating user input
- Resource cleanup

**Best Practices:**
- Be specific about exception types
- Don't catch all exceptions blindly
- Log exceptions for debugging
- Provide meaningful error messages
- Clean up resources in finally block

---

## exercise/
**Purpose:** Comprehensive coding exercises organized by topic

**Subdirectories:**
- `csv/` - CSV file handling and data processing
- `dict/` - Dictionary operations and data management
- `loops/` - Loop structures and iterations
- `sample/` - Sample code patterns
- `strings/` - String manipulation exercises
- `tuple/` - Tuple operations

**Files Overview:**
- `sort.py` - Sorting algorithms and techniques
- CSV exercises: `file.py`, `file2.py`, `report.py`
- Dictionary exercises: `dic_key.py`, `email.py`, `group.py`, `network.py`, `total.py`
- Loop exercises: `class_01.py`, `digits.py`, `multiply.py`, `odd.py`, `tricky.py`
- Sample exercises: `post.py`, `send.py`
- String exercises: `brain_teaser.py`, `palindrome.py`, `UNIQUE.py`
- Tuple exercises: `bio.py`, `convert_to_turple.py`

**Learning Path:**
Start with simpler exercises and progress to complex ones:
1. **Strings** → Basic text manipulation
2. **Lists/Loops** → Iteration patterns
3. **Dictionaries** → Data structure combinations
4. **CSV/File Operations** → Real-world data handling
5. **Tuples** → Immutable data structures

**Exercise Categories:**

### Strings (`strings/`)
- Pattern matching and searching
- Text transformation
- Palindrome checking
- Unique character identification
- Cryptic algorithm challenges

### Loops (`loops/`)
- Iterating with for/while loops
- Nested loop patterns
- Conditional iterations
- Number manipulation
- Complex logic challenges

### Dictionaries (`dict/`)
- Key-value operations
- Email data organization
- Grouping operations
- Network data management
- Calculation and aggregation

### CSV (`csv/`)
- Reading CSV files
- Processing tabular data
- Generating reports
- Data transformation

### Tuples (`tuple/`)
- Immutable sequences
- Data conversion
- Biographical data handling

**Progression Strategy:**
- Follow difficulty level within each category
- Mix different categories for variety
- Review solutions and refactor code
- Understand edge cases and constraints

---

## file/
**Purpose:** File I/O operations - reading and writing files

**Key Concepts:**
- Opening and closing files
- Reading file contents
- Writing to files
- CSV file handling
- File paths and permissions

**Files Included:**
- `read_csv.py` - Reading CSV files
- `write_csv.py` - Writing data to CSV files

**Learning Path:**
1. `read_csv.py` - Understanding how to read CSV data
2. `write_csv.py` - Writing data to CSV format

**Common Operations:**
```python
# Reading files
with open('file.txt', 'r') as f:
    content = f.read()         # Read entire file
    lines = f.readlines()      # Read as list of lines

# Writing files
with open('file.txt', 'w') as f:
    f.write('content')         # Write string
    f.writelines(lines)        # Write multiple lines

# CSV operations
import csv
reader = csv.reader(file)      # Parse CSV
writer = csv.writer(file)      # Write CSV
```

**Best Practices:**
- Always use `with` statement for file operations
- Specify file mode correctly ('r', 'w', 'a', 'rb', 'wb')
- Handle encoding issues (UTF-8)
- Check file existence before reading
- Use context managers for automatic cleanup

**When to Use:**
- Loading data from files
- Saving results to files
- Processing CSV/tabular data
- Log file operations
- Configuration file management

---

## list/
**Purpose:** List data structure operations and methods

**Key Concepts:**
- List creation and indexing
- List methods: `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`
- List slicing
- List iteration
- Nested lists

**Files Included:**
- `list.py` - Basic list operations
- `insert.py` - Using `.insert()` method
- `pop.py` - Using `.pop()` to remove items
- `remove.py` - Using `.remove()` method
- `map.py` - Applying functions to lists
- `squares.py` - Computing squares of numbers
- `readme.md` - Documentation on list operations

**Learning Path:**
1. `list.py` - Understand list basics
2. Individual method files - Learn specific operations
3. `map.py` - Functional programming with lists
4. `squares.py` - Practical applications

**Common Operations:**
```python
# Creation and access
lst = [1, 2, 3]
lst[0]           # Access by index
lst[-1]          # Last element
lst[1:3]         # Slicing

# Modification methods
lst.append(4)    # Add to end
lst.extend([5,6])# Add multiple items
lst.insert(0, 0) # Insert at position
lst.remove(2)    # Remove by value
lst.pop()        # Remove last item
lst.pop(0)       # Remove by index

# Utility methods
lst.sort()       # Sort in place
lst.reverse()    # Reverse in place
len(lst)         # Get length
```

**When to Use:**
- Store ordered collections
- Need mutable sequences
- Working with arrays of data
- Stack/queue operations
- Grouping related values

**Performance Considerations:**
- Append: O(1) average
- Insert/Remove: O(n) due to shifting
- Access by index: O(1)
- Search: O(n)

---

## list-comprehension/
**Purpose:** Concise and efficient list creation using comprehension syntax

**Key Concepts:**
- List comprehension syntax
- Filtering with conditions
- Nested comprehensions
- Transformations and mappings
- Readable, Pythonic code

**Files Included:**
- `example.py` - Basic comprehension examples
- `example_01.py` through `example_03.py` - Progressive examples
- `odd.py` - Filtering odd numbers
- `pig_latin.py` - String transformation example
- `score.py` - Numerical calculations

**Learning Path:**
1. `example.py` - Basic syntax
2. `example_01.py` - Foundational patterns
3. `odd.py` - Filtering operations
4. `score.py` - Calculations
5. `pig_latin.py` - Complex transformations

**Common Patterns:**
```python
# Basic comprehension
squares = [x**2 for x in range(10)]

# With filter condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]

# String transformation
upper = [s.upper() for s in words]
```

**Advantages:**
- More concise than for loops
- Often faster (optimized in Python)
- More readable and Pythonic
- Functional programming style
- Single expression instead of multiple lines

**When to Use:**
- Creating filtered or transformed lists
- Replacing simple for loops with append
- Generating sequences
- Data transformation
- When readability is maintained

**Avoid When:**
- Logic becomes too complex
- Multiple levels of nesting (>2)
- Comprehension becomes less readable than loop

---

## loops/
**Purpose:** Loop structures - for loops, while loops, and nested iterations

**Key Concepts:**
- For loops with ranges
- While loops and conditions
- Nested loops
- Loop control (break, continue)
- Iterating over sequences

**Subdirectories:**
- `for_loops/` - For loop patterns
- `nested_loops/` - Nested loop examples

**Files Included:**
- `divisible_by_2.py` - Filtering even numbers
- `loop-01.py` - Basic loop patterns with factors
- `sum_of_integer.py` - Accumulation patterns
- `for_loops/def.py` - Function definitions in loops
- `for_loops/product.py` - Computing products
- `nested_loops/left_right.py` - 2D iteration patterns

**Learning Path:**
1. `loop-01.py` - Basic while loop patterns
2. `divisible_by_2.py` - Conditional iterations
3. `sum_of_integer.py` - Accumulation
4. `for_loops/product.py` - For loop patterns
5. `nested_loops/left_right.py` - 2D iterations

**Common Patterns:**
```python
# For loop
for i in range(10):
    print(i)

# While loop
while condition:
    # Code
    if stop_condition:
        break

# Nested loops
for i in range(3):
    for j in range(3):
        print(i, j)
```

**Loop Control:**
- `break` - Exit loop immediately
- `continue` - Skip to next iteration
- `else` - Run if loop completes normally

**When to Use:**
- Iterating over sequences
- Counting or accumulating values
- Processing collections
- Creating patterns
- Algorithm implementation

**Optimization Tips:**
- Use range() efficiently
- Consider list comprehensions for simple transformations
- Avoid nested loops when possible
- Break early when condition met

---

## mail/
**Purpose:** Email operations, data processing, and communication

**Key Concepts:**
- Email data handling
- Message composition
- Data transformation
- Report generation
- Integration with mail systems

**Files Included:**
- `car.txt` - Sample data file
- `cars.py` - Vehicle data processing
- `example.py` - Example patterns
- `mail.py` - Email operations
- `report.py` - Report generation from data

**Learning Path:**
1. `cars.py` - Understand data processing
2. `mail.py` - Email sending/handling
3. `report.py` - Generate formatted reports
4. `example.py` - Practical implementations

**Common Use Cases:**
- Send automated emails
- Parse email data
- Generate mail reports
- Template-based messages
- Batch email operations

**Best Practices:**
- Use secure SMTP connections
- Template emails for consistency
- Log email operations
- Handle failures gracefully
- Validate email addresses

---

## os-py/
**Purpose:** Operating system interactions and environment management

**Key Concepts:**
- Environment variables
- System commands execution
- Process management
- OS-specific operations
- Cross-platform compatibility

**Files Included:**
- `env.py` - Environment variable operations

**Learning Path:**
1. `env.py` - Understanding environment variables

**Common Operations:**
```python
import os

# Environment variables
os.getenv('VAR_NAME')          # Get variable
os.environ['VAR_NAME']         # Access environment
os.environ['NEW_VAR'] = 'value' # Set variable

# System info
os.name                        # OS name
os.getcwd()                    # Current directory
os.listdir('path')             # List files
```

**When to Use:**
- Accessing environment configuration
- Cross-platform file operations
- System information retrieval
- Setting up paths dynamically
- OS detection and adaptation

---

## puppet/
**Purpose:** Puppet infrastructure configuration and automation

**Key Concepts:**
- Infrastructure as Code (IaC)
- Puppet manifests (.pp files)
- Resource declarations
- Node configuration
- Service management

**Files Included:**
- `machine_info.pp` - Machine information resources
- `node.pp` - Node configuration
- `puppet-lint.pp` - Linting rules
- `restart.pp` - Service restart management
- `server.pp` - Server configuration
- `test-01.pp` - Test configurations
- `readme.md` - Puppet documentation

**Learning Path:**
1. `readme.md` - Puppet basics
2. `node.pp` - Node declarations
3. `server.pp` - Server configuration
4. `restart.pp` - Service management
5. `puppet-lint.pp` - Code quality

**Common Resources:**
```puppet
# Package management
package { 'package_name':
  ensure => installed,
}

# Service management
service { 'service_name':
  ensure => running,
  enable => true,
}

# File management
file { '/path/to/file':
  ensure  => present,
  content => 'file content',
}
```

**When to Use:**
- Automated server provisioning
- Configuration management
- Infrastructure consistency
- Deployment automation
- Multi-machine setups

---

## recursion/
**Purpose:** Recursive algorithm patterns and recursive problem-solving

**Key Concepts:**
- Base cases and recursive cases
- Function calling itself
- Stack overflow prevention
- Recursive data structures
- Memoization and optimization

**Files Included:**
- `factorial.py` - Computing factorial recursively
- `matrix.py` - Matrix operations with recursion
- `recursive_file.py` - Recursive file system operations
- `sum_positive.py` - Summing positive numbers recursively

**Learning Path:**
1. `factorial.py` - Simple base case example
2. `sum_positive.py` - Accumulation with recursion
3. `matrix.py` - Complex data structure recursion
4. `recursive_file.py` - Real-world recursion

**Common Pattern:**
```python
def recursive_function(n):
    # Base case
    if n == 0:
        return 0
    
    # Recursive case
    return n + recursive_function(n - 1)
```

**When to Use:**
- Tree/graph traversal
- Divide-and-conquer algorithms
- Backtracking problems
- Natural recursive structures
- Mathematical computations

**Cautions:**
- Define clear base case
- Ensure termination
- Watch for stack overflow
- Consider iterative alternative
- Use memoization for optimization

---

## resize_image/
**Purpose:** Image processing and manipulation

**Key Concepts:**
- Image library usage (PIL/Pillow)
- Image resizing
- Format conversion
- Batch processing
- Dimension preservation

**Files Included:**
- `script.py` - Image resizing script

**Learning Path:**
1. `script.py` - Image processing patterns

**Common Operations:**
```python
from PIL import Image

# Open image
img = Image.open('image.jpg')

# Get dimensions
width, height = img.size

# Resize
resized = img.resize((new_width, new_height))

# Save
resized.save('output.jpg')
```

**When to Use:**
- Batch image processing
- Thumbnail generation
- Format conversion
- Image optimization
- Automated image workflows

**Best Practices:**
- Preserve aspect ratio
- Validate image formats
- Handle file errors
- Use efficient libraries (Pillow)
- Optimize for target use

---

## strings/
**Purpose:** String manipulation and text processing operations

**Key Concepts:**
- String methods: `.upper()`, `.lower()`, `.split()`, `.join()`, `.replace()`, `.format()`
- String indexing and slicing
- String length with `len()`
- Character checking: `.isnumeric()`, `.isalpha()`
- String operations and transformations

**Files Included:**
- `format_method.py` - Using `.format()` for string formatting
- `join.py` - Using `.join()` to combine strings
- `loop_strings.py` - Iterating through strings
- `reverse.py` - Reversing string contents
- `square.py` - Formatting numbers as strings
- `string.py` - Basic string operations
- `strings.py` - Additional string patterns

**Learning Path:**
1. `string.py` - Basic string basics
2. `format_method.py` - String formatting
3. `join.py` - String joining
4. `reverse.py` - String manipulation
5. `loop_strings.py` - Iteration patterns
6. `square.py` - Numerical string formatting

**Common Operations:**
```python
# Case conversion
"hello".upper()                # "HELLO"
"HELLO".lower()                # "hello"

# Splitting and joining
"a,b,c".split(',')             # ['a', 'b', 'c']
'-'.join(['a', 'b', 'c'])      # 'a-b-c'

# Formatting
"Hello {}".format(name)        # Positional
f"Hello {name}"                # F-string (Python 3.6+)

# Searching and replacing
"hello world".replace("world", "python")
"hello world".find("world")    # Index or -1

# Checking
"123".isnumeric()              # True
"abc".isalpha()                # True
"hello".startswith("hel")      # True
```

**When to Use:**
- Text processing and parsing
- Data validation
- String formatting for output
- Text transformation
- Report generation

**Performance Tips:**
- Use `.join()` instead of `+` for multiple concatenations
- Use f-strings for complex formatting (faster)
- Use generator expressions for large strings
- Consider regex for complex patterns

---

## testing/
**Purpose:** Test case development and validation

**Key Concepts:**
- Test organization
- Test case writing
- Assertions and validation
- Test execution
- Code coverage

**Subdirectories:**
- `test-case-1/` - First test case set

**Files Included:**
- `code.py` - Implementation code to test
- `test-01.py` - Test cases for validation

**Learning Path:**
1. `code.py` - Understand implementation
2. `test-01.py` - Review test patterns

**Common Test Pattern:**
```python
def test_function():
    # Arrange
    input_data = ...
    
    # Act
    result = function_to_test(input_data)
    
    # Assert
    assert result == expected_value
```

**When to Use:**
- Ensuring code reliability
- Regression prevention
- Documentation through tests
- Refactoring safety
- Continuous integration

**Best Practices:**
- Test both happy path and edge cases
- Keep tests independent
- Use descriptive test names
- Maintain test organization
- Aim for reasonable coverage

---

## tuple/
**Purpose:** Tuple data structure operations - immutable sequences

**Key Concepts:**
- Tuple creation and unpacking
- Immutability and performance
- Tuple indexing and slicing
- Converting between sequences
- Using tuples as dictionary keys

**Files Included:**
- `email.py` - Email data organized in tuples
- `my_tuple.py` - Basic tuple operations
- `bio.py` - Biographical data in tuples (in exercise directory)
- `convert_to_turple.py` - Converting lists to tuples

**Learning Path:**
1. `my_tuple.py` - Basic tuple operations
2. `convert_to_turple.py` - Conversion patterns
3. `email.py` - Real-world tuple usage

**Common Operations:**
```python
# Creation
t = (1, 2, 3)              # Tuple literal
t = tuple([1, 2, 3])       # From list

# Access
t[0]                       # Index access
t[-1]                      # Last element
x, y, z = t                # Unpacking

# Properties
len(t)                     # Length
1 in t                     # Membership
t.count(1)                 # Count occurrences
t.index(2)                 # Index of value
```

**When to Use:**
- Fixed-size sequences
- Dictionary keys (tuples are hashable)
- Function return multiple values
- Protecting data from modification
- Performance when immutability needed

**Advantages Over Lists:**
- Immutable (safer for concurrent access)
- Can be dictionary keys
- Slightly faster and less memory
- Clearer intent (fixed data)
- Function return values

---

## web/
**Purpose:** Web utilities, monitoring, and HTTP operations

**Key Concepts:**
- HTTP requests and responses
- JSON data handling
- Web monitoring and health checks
- Logging for debugging
- API interactions

**Files Included:**
- `convert_json.py` - JSON data conversion
- `health.py` - Health check monitoring
- `logger_setup.py` - Logging configuration
- `monitoring.py` - System monitoring
- `python-01.py` - Web operation examples
- `test.py` - Testing web operations
- `dir/task-01.py` - Additional web tasks

**Learning Path:**
1. `logger_setup.py` - Setup logging framework
2. `health.py` - Understand health checks
3. `convert_json.py` - JSON operations
4. `monitoring.py` - System monitoring patterns
5. `python-01.py` - Web request patterns

**Common Operations:**
```python
import requests
import json

# HTTP requests
response = requests.get('https://api.example.com/data')
data = response.json()         # Parse JSON

# JSON operations
json.dumps(dict)               # Convert to JSON string
json.loads(json_string)        # Parse JSON string

# Error handling
if response.status_code == 200:
    process_data(response.json())
else:
    log_error(response.status_code)
```

**When to Use:**
- API interactions
- Web scraping (with permission)
- Health monitoring
- Data collection from web services
- Integration with web platforms

**Best Practices:**
- Handle network timeouts
- Validate SSL certificates
- Log all web operations
- Implement rate limiting
- Use connection pooling for efficiency
- Handle various HTTP status codes

---

## Summary: Learning Progression

### Beginner Level
1. Start with **strings/** - basic text manipulation
2. Move to **list/** - data collection basics
3. Explore **dictionaries/** - key-value storage
4. Practice **loops/** - iteration patterns

### Intermediate Level
1. **list-comprehension/** - Pythonic data transformation
2. **exception/** - Error handling and robustness
3. **classes/** - Object-oriented programming
4. **file/** - Data persistence

### Advanced Level
1. **recursion/** - Algorithm optimization
2. **exercise/** - Complex problem-solving
3. **web/** - External integrations
4. **testing/** - Code quality assurance

### Specialized Topics
- **tuple/** - Advanced data structures
- **mail/** - Communication automation
- **dir/** - File system operations
- **os-py/** - System administration
- **puppet/** - Infrastructure automation
- **resize_image/** - Image processing
- **bash/** - Shell scripting

---

## Best Practices Across All Directories

1. **Code Organization**
   - Keep related code together
   - Use meaningful file names
   - Document complex logic

2. **Error Handling**
   - Always use try-except for risky operations
   - Provide meaningful error messages
   - Log errors for debugging

3. **Performance**
   - Use appropriate data structures
   - Avoid unnecessary iterations
   - Profile code for bottlenecks

4. **Readability**
   - Use clear variable names
   - Add comments for complex logic
   - Follow PEP 8 style guidelines

5. **Testing**
   - Write tests for critical functions
   - Test edge cases and error conditions
   - Maintain test organization

6. **Documentation**
   - Document function purposes
   - Include usage examples
   - Keep documentation up-to-date

---

## Quick Reference: Data Structures

| Structure | Type | Mutable | Use Case |
|-----------|------|---------|----------|
| List | `[1, 2, 3]` | Yes | Ordered, changeable collections |
| Tuple | `(1, 2, 3)` | No | Immutable, hashable sequences |
| Dictionary | `{a: 1}` | Yes | Key-value mappings |
| Set | `{1, 2, 3}` | Yes | Unique items, fast lookup |
| String | `"hello"` | No | Text, immutable sequences |

---

## Quick Reference: Common Methods

### String Methods
- `.upper()`, `.lower()`, `.capitalize()`
- `.split()`, `.join()`, `.replace()`
- `.strip()`, `.startswith()`, `.endswith()`

### List Methods
- `.append()`, `.extend()`, `.insert()`
- `.remove()`, `.pop()`, `.sort()`, `.reverse()`

### Dictionary Methods
- `.keys()`, `.values()`, `.items()`
- `.get()`, `.update()`, `.pop()`

### File Operations
- `open()`, `close()`, `read()`, `write()`
- Context manager: `with open() as f:`

---

**Last Updated:** January 20, 2026
**Status:** Complete reference guide for all project directories

