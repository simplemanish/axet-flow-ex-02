The purpose of this code block is to create a graphical calculator using the `tkinter` library in Python. The calculator has a user interface that allows performing basic mathematical operations such as addition, subtraction, multiplication, division, squaring, and square roots. The interface includes buttons for digits, operators, and special functions, as well as a display area to show expressions and results.

### Code Explanation

1. **Importing the `tkinter` Library**:
   ```python
   import tkinter as tk
   ```
   The `tkinter` library is imported, which is used to create graphical user interfaces in Python.

2. **Defining Styles and Colors**:
   ```python
   LARGE_FONT_STYLE = ("Arial", 40, "bold")
   SMALL_FONT_STYLE = ("Arial", 16)
   DIGITS_FONT_STYLE = ("Arial", 24, "bold")
   DEFAULT_FONT_STYLE = ("Arial", 20)

   OFF_WHITE = "#F8FAFF"
   WHITE = "#FFFFFF"
   LIGHT_BLUE = "#CCEDFF"
   LIGHT_GRAY = "#F5F5F5"
   LABEL_COLOR = "#25265E"
   ```
   Font styles and colors are defined for use in the calculator's interface.

3. **`Calculator` Class**:
   ```python
   class Calculator:
       def __init__(self):
           self.window = tk.Tk()
           self.window.geometry("375x667")
           self.window.resizable(0, 0)
           self.window.title("Calculator")
           ...
   ```
   The `Calculator` class contains all the methods and attributes needed to create and manage the calculator. The `__init__` method initializes the main window and sets its size, title, and other properties.

4. **Creating the Interface**:
   - **Display Frame**:
     ```python
     self.display_frame = self.create_display_frame()
     ```
     A frame is created to display expressions and results.

   - **Display Labels**:
     ```python
     self.total_label, self.label = self.create_display_labels()
     ```
     Labels are created to show the total expression and the current expression.

   - **Digit and Operator Buttons**:
     ```python
     self.create_digit_buttons()
     self.create_operator_buttons()
     self.create_special_buttons()
     ```
     Buttons are created for digits, operators, and special functions (clear, equals, square, square root).

   - **Key Bindings**:
     ```python
     self.bind_keys()
     ```
     Keyboard keys are bound to the corresponding functions of the calculator.

5. **Methods of the `Calculator` Class**:
   - **`create_display_frame`**: Creates the display frame.
   - **`create_display_labels`**: Creates the display labels.
   - **`add_to_expression`**: Adds a digit to the current expression.
   - **`append_operator`**: Adds an operator to the current expression.
   - **`evaluate`**: Evaluates the mathematical expression.
   - **`clear`**: Clears the expressions.
   - **`square`**: Calculates the square of the current expression.
   - **`sqrt`**: Calculates the square root of the current expression.
   - **`update_label`**: Updates the current expression label.
   - **`update_total_label`**: Updates the total expression label.
   - **`run`**: Runs the main loop of the window.

### Example of Usage

To run the calculator, simply execute the script. The calculator will appear in a graphical window, and you can interact with it using the buttons and the keyboard.

```python
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
```

When you run this code, a window with the calculator will open, ready for use. You can click the buttons or use the keyboard to perform calculations.
