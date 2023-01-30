# 💻 Code-Typing-Automation

This Python script uses the PyAutoGUI library to simulate typing code into the currently open window. This script also has options to remove indentation, skip closing braces, and remove extra code at the end of entered code, which might be helpful when typing code into an IDE or text editor.

## 🎉 Features

- 🔥 **REMOVE_INDENTATION:** Removes indentation from the code block.
- 💥 **SKIP_CLOSING_BRACKETS:** Skips over closing brackets when being typed into the active window.
- 🗑️ **DELETE_AFTER_END:** Deletes everything after the typed code.

## 📋 Requirements

- [🐍 Python 3.x](https://www.python.org/downloads/)
- [🛠️ PyAutoGUI library](https://pypi.org/project/PyAutoGUI/): To install it using pip run the following command `pip install pyautogui`

## 🚀 Usage

1. 💾 Clone the repository to your device.
2. 📦 Install the required packages.
3. ✏️ Edit the `code` variable with the code you want to type.
4. 🛠️ Adjust the settings as per your requirement.
5. 🚀 Run the script using the following command `python code_auto_typer.py`

## ⚠️ Note

- **This script will not work properly if the numlock key is off.** See [Github issue #01](https://github.com/chaudharydeepanshu/Code-Typing-Automation/issues/1) for updates on the fix for numlock compatibility.
- Use this script with caution; if improperly used, it may result in undesirable actions on your system.
- Before using the script on your primary system, it is always a good idea to test it in a virtual environment or on a different device.

## 🤝 Contributing

Feel free to contribute to this project by submitting a pull request 🙌. Any suggestions or bug reports are also welcome 💬.
