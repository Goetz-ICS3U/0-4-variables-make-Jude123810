import re
import sys
import io
import os
import glob


def find_student_file():
    """Find the student's Python file"""
    # List current directory contents for debugging
    all_files = os.listdir('.')
    py_files_in_dir = [f for f in all_files if f.endswith('.py')]
    
    # List of possible filenames
    possible_names = [
        "vars_make.py",
        "var_make.py",
        "vars_making.py",
        "var_making.py"
    ]
    
    # Check current directory
    for name in possible_names:
        if os.path.exists(name):
            return name
    
    # Check for any Python file that's not the test file
    py_files = [f for f in glob.glob("*.py") if not f.startswith("test_")]
    if len(py_files) == 1:
        return py_files[0]
    elif len(py_files) > 1:
        # Multiple files found, try to find the most likely one
        for f in py_files:
            if "var" in f.lower() and "make" in f.lower():
                return f
        # If no match, return the first non-test file
        return py_files[0]
    
    # If we get here, provide helpful error message
    error_msg = f"Could not find student's Python file. "
    error_msg += f"Files in directory: {', '.join(py_files_in_dir)}. "
    error_msg += f"Make sure you have created a .py file with your code (expected one of: {', '.join(possible_names)})."
    raise FileNotFoundError(error_msg)


# Find the student file once at module level
try:
    STUDENT_FILE = find_student_file()
    STUDENT_MODULE = STUDENT_FILE.replace(".py", "")
except FileNotFoundError as e:
    STUDENT_FILE = None
    STUDENT_MODULE = None
    print(f"Error: {e}")


def test_header_comments():
    """Test that student included author and date in header comments"""
    if STUDENT_FILE is None:
        raise AssertionError("Could not find student's Python file. Make sure you have created a .py file with your code.")
    
    with open(STUDENT_FILE, encoding="utf-8") as f:
        kids_code = f.read()
    
    # Get first 500 characters to check header
    header = kids_code[:500]
    
    # Check for author comment
    has_author = bool(re.search(r'author\s*:', header, re.IGNORECASE))
    assert has_author, "Missing 'author:' in header comments. Please add your name in the header."
    
    # Check for date comment
    has_date = bool(re.search(r'date\s*:', header, re.IGNORECASE))
    assert has_date, "Missing 'date:' in header comments. Please add the date in the header."
    
    # Check that author is not empty or still the default
    author_match = re.search(r'author\s*:\s*(.+)', header, re.IGNORECASE)
    if author_match:
        author_value = author_match.group(1).strip()
        assert author_value and author_value.lower() not in ['', 'mr. habib', 'student name'], \
            "Please fill in your actual name for 'author:' in the header"


def test_circle_calculation(capsys, monkeypatch):
    """Test that student correctly calculated circle area and perimeter"""
    if STUDENT_FILE is None or STUDENT_MODULE is None:
        raise AssertionError("Could not find student's Python file. Make sure you have created a .py file with your code.")
    
    inputs = ["2", "2", "2", "2"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop())
    
    try:
        # Dynamically import the student's module
        import importlib
        # Clear any previously imported module
        if STUDENT_MODULE in sys.modules:
            del sys.modules[STUDENT_MODULE]
        student_module = importlib.import_module(STUDENT_MODULE)
    except ModuleNotFoundError:
        raise AssertionError(f"Could not import {STUDENT_FILE}. Make sure the file is named correctly.")
    except Exception as e:
        raise AssertionError(f"Error running {STUDENT_FILE}: {str(e)}")
    
    captured = capsys.readouterr()

    assert "he circle has an area of 12.566370614359172 and a perimeter of 12.566370614359172" in captured.out, \
        "Circle calculation is incorrect. Check your circle area and perimeter formulas. Expected area=12.566370614359172 and perimeter=12.566370614359172 for radius=2"


def test_rectangle_calculation(capsys, monkeypatch):
    """Test that student correctly calculated rectangle area and perimeter"""
    if STUDENT_FILE is None or STUDENT_MODULE is None:
        raise AssertionError("Could not find student's Python file. Make sure you have created a .py file with your code.")
    
    inputs = ["2", "2", "2", "2"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop())
    
    try:
        # Dynamically import the student's module
        import importlib
        # Clear any previously imported module
        if STUDENT_MODULE in sys.modules:
            del sys.modules[STUDENT_MODULE]
        student_module = importlib.import_module(STUDENT_MODULE)
    except ModuleNotFoundError:
        raise AssertionError(f"Could not import {STUDENT_FILE}. Make sure the file is named correctly.")
    except Exception as e:
        raise AssertionError(f"Error running {STUDENT_FILE}: {str(e)}")
    
    captured = capsys.readouterr()

    assert "The rectangle has an area of 4 and a perimeter of 8" in captured.out, \
        "Rectangle calculation is incorrect. Check your rectangle area and perimeter formulas. Expected area=4 and perimeter=8 for length=2, width=2"


def test_octagon_calculation(capsys, monkeypatch):
    """Test that student correctly calculated octagon area and perimeter"""
    if STUDENT_FILE is None or STUDENT_MODULE is None:
        raise AssertionError("Could not find student's Python file. Make sure you have created a .py file with your code.")
    
    inputs = ["2", "2", "2", "2"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop())
    
    try:
        # Dynamically import the student's module
        import importlib
        # Clear any previously imported module
        if STUDENT_MODULE in sys.modules:
            del sys.modules[STUDENT_MODULE]
        student_module = importlib.import_module(STUDENT_MODULE)
    except ModuleNotFoundError:
        raise AssertionError(f"Could not import {STUDENT_FILE}. Make sure the file is named correctly.")
    except Exception as e:
        raise AssertionError(f"Error running {STUDENT_FILE}: {str(e)}")
    
    captured = capsys.readouterr()

    assert "The octagon has an area of 19.31370849898476 and a perimeter of 16" in captured.out, \
        "Octagon calculation is incorrect. Check your octagon area and perimeter formulas. Expected area=19.31370849898476 and perimeter=16 for side=2"


if __name__ == "__main__":
    # This allows running the tests directly
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
