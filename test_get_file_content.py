from config import MAX_CHARS
from functions.get_file_content import get_file_content

# 1. Test reading a normal file (main.py)
print(get_file_content("calculator", "main.py"))


# 2. Test reading inside a subpackage (pkg/calculator.py)
print(get_file_content("calculator", "pkg/calculator.py"))

# 3. Test truncation on lorem.txt
lorem_content = get_file_content("calculator", "lorem.txt")
is_truncated = len(lorem_content) > MAX_CHARS or "[... File truncated" in lorem_content
print(f"lorem.txt truncated: {is_truncated}")

# 4. Test directory traversal protection
print(get_file_content("calculator", "/bin/cat"))

# 5. Test non-existent file
print(get_file_content("calculator", "pkg/does_not_exist.py"))