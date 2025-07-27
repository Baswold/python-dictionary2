# Python Function Definition Template

This template shows the exact format needed for adding function definitions to the `definitions.json` file.

## Template Format

```json
{
  "function_name": {
    "definition": "Brief, clear description of what the function does.",
    "example": "# Code example showing usage\nresult = function_name(parameters)\nprint(result)  # Expected output"
  }
}
```

## Required Fields

- **function_name**: The exact name of the Python function/method (use parentheses for custom functions like "my_function()")
- **definition**: A concise explanation of what the function does
- **example**: Working Python code that demonstrates usage, including expected output

## Examples

### Built-in Function
```json
{
  "len": {
    "definition": "Returns the number of items in an object (string, list, tuple, etc.).",
    "example": "text = \"hello\"\nprint(len(text))  # 5\n\nmy_list = [1, 2, 3]\nprint(len(my_list))  # 3"
  }
}
```

### List Method
```json
{
  "append": {
    "definition": "Adds an element to the end of a list.",
    "example": "my_list = [1, 2, 3]\nmy_list.append(4)\nprint(my_list)  # [1, 2, 3, 4]"
  }
}
```

### String Method
```json
{
  "split": {
    "definition": "Splits a string into a list using a specified delimiter.",
    "example": "text = \"apple,banana,cherry\"\nresult = text.split(\",\")\nprint(result)  # ['apple', 'banana', 'cherry']"
  }
}
```

### Custom Function
```json
{
  "my_function()": {
    "definition": "Description of what your custom function does.",
    "example": "result = my_function(arg1, arg2)\nprint(result)  # Expected output"
  }
}
```

## Guidelines

1. **Definition**: Keep it concise but informative (1-2 sentences)
2. **Example**: Include actual runnable code with expected output
3. **Formatting**: Use `\n` for line breaks in the JSON string
4. **Output**: Show expected results using `# comment` format
5. **Function Names**: Use exact Python names; add `()` for custom functions to distinguish them

## Adding Multiple Functions

When adding multiple functions, separate them with commas:

```json
{
  "len": {
    "definition": "Returns the number of items in an object.",
    "example": "print(len([1, 2, 3]))  # 3"
  },
  "max": {
    "definition": "Returns the largest item in an iterable.",
    "example": "numbers = [1, 5, 3, 9, 2]\nprint(max(numbers))  # 9"
  }
}
```

## After Adding Definitions

1. Save the `definitions.json` file
2. Open the Python Dictionary App
3. Click "Reload Definitions" to load your new entries
4. Test by searching for your function names