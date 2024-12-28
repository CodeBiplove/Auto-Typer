
# Auto-Typer from DOCX

This Python script simulates typing the contents of a `.docx` file using the `pyautogui` library. 
It automates the process of reading text from a Word document and typing it into a focused text editor or any other window on your computer.

## Features

- Reads text from a `.docx` file.
- Simulates realistic typing with random speed variations.
- Can be customized for different typing speeds and delay times.
- Ideal for automating tasks such as text input in forms, demonstrations, or testing.

## Requirements

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `pyautogui` library
- `python-docx` library

You can install the required dependencies using `pip`:

```bash
pip install pyautogui python-docx
```

## Installation

1. Clone this repository to your local machine.
2. Ensure that the required libraries (`pyautogui` and `python-docx`) are installed.
3. Place the `.docx` file you want to simulate typing from in the same directory as the script, or provide the full path to the file.

## Usage

1. Open a text editor, word processor, or any other program where you want to "type" the contents of the `.docx` file.
2. Focus the window of the program where you want the text to appear.
3. Run the script:

```bash
Run in the dedicated terminal
```

4. The script will wait for 5 seconds (default), allowing you to switch to the window where you want the text typed.
5. The script will then type the contents of the `.docx` file with a randomized typing speed.

### Customization

- **Typing Speed**: You can adjust the typing speed by modifying the `random.uniform(0.0000001, 0.0000003)` value inside the loop.
- Smaller numbers will result in faster typing, while larger numbers will slow it down.
  
  For example:
  ```python
  typing_speed = random.uniform(0.000001, 0.000005)  # Slightly slower typing
  ```

- **File Path**: Modify the `docx_file_path` variable to point to your desired `.docx` file.
  
  ```python
  docx_file_path = 'path_to_your_file.docx'
  ```

## Code Overview

1. **Reading the `.docx` file**: 
   The script uses the `python-docx` library to read the text from the Word document.

   ```python
   def read_docx(file_path):
       doc = Document(file_path)
       full_text = []
       for para in doc.paragraphs:
           full_text.append(para.text)
       return '\n'.join(full_text)
   ```

2. **Simulating Typing**: 
   The `pyautogui.press(char)` function is used to simulate pressing each character in the text read from the `.docx` file. A random typing speed is applied between key presses to simulate human-like typing behavior.

   ```python
   for char in text:
       pyautogui.press(char)
       typing_speed = random.uniform(0.0000001, 0.0000003)
       time.sleep(typing_speed)
   ```

3. **Timing**: 
   A 5-second delay is added at the beginning of the script, giving the user time to focus on the correct window where the text will be typed.

   ```python
   time.sleep(5)
   ```

4. **Completion**: 
   After the script finishes typing, a "Done" message will be printed to the console.

   ```python
   print("Done")
   ```

## Limitations

- **Window Focus**: The script requires the window where the text is to be typed to be in focus. Make sure the window is active and ready to receive keyboard input.
- **Typing Speed**: While the script simulates typing speed, it might not perfectly replicate human typing behavior, especially on very fast speeds.
- **Text Formatting**: Only the raw text from the document is typed; any formatting (such as bold, italics, or font color) is not preserved.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

- [Your Name](https://github.com/codebiplove)

---
