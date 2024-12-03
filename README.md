# In-Memory Database Manager

## Overview
This project provides a simple in-memory database manager implemented in Python. the spec can be found [here](https://docs.google.com/document/d/1GVdJngVnufjrnXlWGC_eSru_ZxDdOOQkLT7KO2ZHF2Q/edit?tab=t.0)

---

## Requirements
- **Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/).

---

## Instructions

### Step 1: Clone the Repository
Run the following command in your terminal or command prompt to clone the repository:
```bash
git clone <repository-url>
```

### Step 2: Change to the Project Directory
Navigate into the cloned directory:
```bash
cd <project-directory>
```

### Step 3: Start working in the directory
Start the Python interpreter. Use python (or py for Windows) and python3 for Linux/Mac, from the working directory:
```bash
python
```
or for mac/linux:
```bash
python3
```

### Step 4: Import the Class
Once in the Python interpreter, import the InMemoryDB class:
```python
from in_memory_db import InMemoryDB
```

### Step 5: Create an Instance of the Class
Create an instance of the InMemoryDB class to start using the database:
```python
inmemoryDB = InMemoryDB()
```

### Step 6: Test the Memory manager
Test the memory manager using the commands specified in the project documentation or specifications. For example:
```python
# should return null, because A doesn’t exist in the DB yet
inmemoryDB.get(“A”)

# etc...
```

## WRITEUP
I think it would be easier to grade this assignment if the student took pictures of given results, or if there was an autograder to run test cases on. I think the wording of how to implement the rollback function is ambiguous and needs work. I interpreted it as saying the rollback function should clear the uncommitted changes of the current transaction, but based on the examples and spec, it is unclear.