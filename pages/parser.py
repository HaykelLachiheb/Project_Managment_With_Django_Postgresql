from html.parser import exceptions.ParserError
from exceptions import ParserError

# ... your code ...

try:
    # ... your HTML parsing code ...
except ParserError as e:
    # Handle the parsing error
    print(f"Parsing error: {e}")