#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module automates GUI interactions by simulating typing code in a GUI
window. It also has options to remove indentation, skip typing closing
brackets or delete everything after the end of the code.
"""

# Import the ctypes library to access keyboard keys state.
# ctypes accesses C functions through Python, interfacing with platform libs.
import ctypes

# Import the PyAutoGUI library to automate GUI interactions.
# PyAutoGUI is used for simulating typing, clicking, and other user actions.
import pyautogui

# Auto-indenting in IDEs or editors can mess with typing if code is indented.
# When set to True, the code will be stripped of any indentation.
REMOVE_INDENTATION = True

# Auto-closing of brackets in IDEs or editors can cause excess closing brackets.
# When set to True, the code will skip closing brackets when being typed.
SKIP_CLOSING_BRACKETS = True

# Alternative to skipping closing brackets.
# When set to True, everything after the end of the code will be deleted.
DELETE_AFTER_END = False

# Define the block of code as a string.
CODE = """
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


def is_numlock_on():
    """
    This function uses the ctypes library and the GetKeyState function from the
    user32 DLL to check the state of the numlock key.

    A virtual-key code is a unique value assigned by the operating system to
    identify each key on the keyboard.
    The virtual-key code for numlock key is 0x90 and for capslock key is 0x14.

    The GetKeyState function takes a virtual-key code as an argument and returns
    the status of the key as a 16-bit value, with the high-order bit indicating
    the toggle state of the key.
    If the high-order bit is set, the function returns True if key is on.
    If the high-order bit is not set, the function returns False if key is off.
    """
    return True if ctypes.windll.user32.GetKeyState(0x90) & 1 else False


def strip_multiline_text(text):
    """
    Removes indentation from the given multiline text

    :param text: the text to be stripped of indentation
    :return: the text with all indentation removed
    """
    return '\n'.join(line.strip() for line in text.split("\n"))


# If the REMOVE_INDENTATION flag is set to True, remove the code indentation.
if REMOVE_INDENTATION:
    CODE = strip_multiline_text(CODE)

# Determine the hotkey to use based on the state of numlock.
SKIP_CLOSING_CURLY_BRACKET_HOTKEY = "shiftright, down" if is_numlock_on() else "down"
SKIP_CLOSING_ROUND_BRACKET_HOTKEY = "shiftright, right" if is_numlock_on() else "right"

# If the SKIP_CLOSING_BRACKETS flag is set to True, skip typing closing bracket.
# Otherwise, type the entire code block into the active window.
if SKIP_CLOSING_BRACKETS:
    for char in CODE:
        if char in ["}"]:
            # Skip the closing curly bracket character using the hotkey.
            pyautogui.hotkey(*SKIP_CLOSING_CURLY_BRACKET_HOTKEY .split(", "))
        elif char in [")"]:
            # Skip the closing round bracket character using the hotkey.
            pyautogui.hotkey(*SKIP_CLOSING_ROUND_BRACKET_HOTKEY.split(", "))
        else:
            # Type the remaining characters as normal.
            pyautogui.press(char)
else:
    # Type the entire code block into the active window.
    pyautogui.typewrite(CODE, interval=0.10)

# The hotkey for selecting everything after the caret.
SELECT_AFTER_CARET_HOTKEY = "ctrl, shiftright, shiftleft, end"
# The key for delete.
DELETE_KEY = "delete"

# If the DELETE_AFTER_END flag is set to True, delete everything after caret.
if DELETE_AFTER_END:
    # Select everything after the caret in the active window.
    pyautogui.hotkey(*SELECT_AFTER_CARET_HOTKEY.split(", "))
    # Press the Delete key to delete the selected text.
    pyautogui.press(DELETE_KEY)
