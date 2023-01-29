# Import the PyAutoGUI library to automate GUI interactions.
# PyAutoGUI allows you to control the mouse and keyboard to interact with your computer's GUI.
# This is used for simulating typing, clicking, and other actions that a user might perform.
import pyautogui

# Auto-indenting in IDEs or editors can lead to incorrect code indentation if not removed.
# When set to True, the code will be stripped of any indentation.
REMOVE_INDENTATION = True

# Auto-closing brackets in IDEs or editors can result in excess closing brackets if not properly skipped.
# When set to True, the code will skip over closing brackets when being typed into the active window.
SKIP_CLOSING_BRACKETS = True

# A powerful alternative to skipping closing brackets is to delete all subsequent code, including excess closing brackets.
# When set to True, everything after the end of the code will be deleted.
DELETE_AFTER_END = False


def strip_multiline_text(text):
    """
    Removes indentation from the given multiline text

    :param text: the text to be stripped of indentation
    :return: the text with all indentation removed
    """
    return '\n'.join(line.strip() for line in text.split("\n"))


# Define the block of code as a string.
code = """
// Sample Java code.
class Sample {
    int testVar;

    Sample(int a) {
        this.testVar = a;
    }

    Sample(int b, int c) {
        this.testVar = b + c;
    }

    int getTestVar() {
        return this.testVar;
    }
}
"""

# If the REMOVE_INDENTATION flag is set to True, remove the indentation from the code block.
# Indentation can cause issues when running the code, so removing it helps ensure that the code runs as expected.
if REMOVE_INDENTATION:
    code = strip_multiline_text(code)

# If the SKIP_CLOSING_BRACKETS flag is set to True, type the code block into the active window while skipping certain characters.
# Otherwise, type the entire code block into the active window.
if SKIP_CLOSING_BRACKETS:
    for char in code:
        if char in ["}"]:
            pyautogui.press("down")
        elif char in [")"]:
            pyautogui.press("right")
        else:
            pyautogui.press(char)
else:
    pyautogui.typewrite(code, interval=0.10)

# If the DELETE_AFTER_END flag is set to True, everything after the caret will be deleted.
if DELETE_AFTER_END:
    # Select everything after the caret.
    pyautogui.hotkey("ctrl", "shiftright", "shiftleft", "end")
    # Press the Delete key to delete the selected text.
    pyautogui.press('delete')
