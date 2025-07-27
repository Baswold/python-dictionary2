# Python Function Dictionary

A modern, desktop dictionary application for Python functions and methods. Built with tkinter and inspired by macOS Dictionary app design.

## Features

🔍 **Smart Search**
- Search for individual function names (e.g., `append`, `len`, `split`)
- Paste code snippets to find all functions within them
- Real-time search as you type
- Intelligent function name extraction from code

🎨 **Modern UI**
- Dark theme inspired by macOS Dictionary app
- Clean typography with Apple system fonts
- Syntax-highlighted code examples
- Responsive and intuitive interface

📝 **Easy Management**
- File-based definition storage in JSON format
- Bulk import/export capabilities
- One-click reload for updated definitions
- No complex database setup required

⚡ **Fast & Offline**
- Instant search results
- Works completely offline
- Lightweight and responsive
- No internet connection required

## Installation

### Prerequisites

- Python 3.7 or higher
- tkinter (usually included with Python)

### macOS Setup

If you encounter a tkinter import error on macOS:

```bash
# Install tkinter via Homebrew
brew install python-tk
```

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/Baswold/python-dictionary2.git
cd python-dictionary2
```

2. Run the application:
```bash
python3 python_dictionary_app.py
```

That's it! The app will launch with sample definitions included.

## Usage

### Searching Functions

**Single Function Lookup:**
```
Type: append
Result: Shows definition and examples for list.append()
```

**Code Snippet Analysis:**
```python
# Paste this code to find all functions:
my_list = [1, 2, 3]
my_list.append(4)
text = "hello world"
words = text.split(" ")
print(len(words))
```
The app will automatically identify and show definitions for `append`, `split`, `len`, and `print`.

**Real-time Search:**
Start typing any function name and results appear automatically after 3+ characters.

### Managing Definitions

The app uses a simple JSON file format for storing function definitions:

```json
{
  "function_name": {
    "definition": "What the function does",
    "example": "Code example showing usage"
  }
}
```

**To add new functions:**

1. Edit `definitions.json` in any text editor
2. Add your function definitions
3. Click "Reload Definitions" in the app
4. Your new functions are immediately available

**Example definition:**
```json
{
  "enumerate": {
    "definition": "Returns an enumerate object that produces pairs of index and value from an iterable.",
    "example": "fruits = ['apple', 'banana', 'cherry']\nfor i, fruit in enumerate(fruits):\n    print(f'{i}: {fruit}')\n# Output: 0: apple, 1: banana, 2: cherry"
  }
}
```

## File Structure

```
python-dictionary2/
├── python_dictionary_app.py    # Main application
├── definitions.json           # Function definitions database
└── README.md                 # This file
```

## Search Capabilities

The app intelligently extracts function names from:

- **Function calls**: `function_name()`
- **Method calls**: `object.method_name()`
- **Single words**: Direct function name lookup
- **Mixed code**: Any combination of the above

### Search Examples

| Input | Functions Found |
|-------|----------------|
| `my_list.append(5)` | `append` |
| `text.split().join()` | `split`, `join` |
| `len` | `len` |
| `print(len(data.split()))` | `print`, `len`, `split` |

## Customization

### Adding Your Own Functions

Create comprehensive definitions for any Python functions you use frequently:

```json
{
  "your_function": {
    "definition": "Detailed explanation of what it does, parameters, return values",
    "example": "# Clear, working code example\nresult = your_function(param1, param2)\nprint(result)  # Expected output"
  }
}
```

### UI Customization

The app uses system fonts and follows macOS design patterns. You can modify colors and styling in the `setup_ui()` method.

## Contributing

1. Fork the repository
2. Add your function definitions to `definitions.json`
3. Test with the app
4. Submit a pull request

Popular functions to add:
- String methods (`strip`, `replace`, `format`)
- List methods (`extend`, `remove`, `pop`, `index`)
- Dictionary methods (`get`, `keys`, `values`, `items`)
- File operations (`open`, `read`, `write`)
- Data structures (`set`, `tuple`, `dict`)

## Technical Details

- **Built with**: Python 3, tkinter
- **Search engine**: Regular expressions with intelligent pattern matching
- **Data format**: JSON for easy editing and version control
- **Performance**: Instant search, minimal memory usage
- **Compatibility**: Cross-platform (Windows, macOS, Linux)

## Roadmap

- [ ] Export search results to text/markdown
- [ ] Import definitions from Python documentation
- [ ] Fuzzy search for typos
- [ ] Categories and tagging system
- [ ] Dark/light theme toggle
- [ ] Keyboard shortcuts

## License

MIT License - feel free to use, modify, and distribute.

## Support

Found a bug or have a suggestion? [Open an issue](https://github.com/Baswold/python-dictionary2/issues) on GitHub.

---

**Happy coding!** 🐍✨