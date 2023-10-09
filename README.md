# Implementing Error Handling and Testing in Tkinter apps

## `starter.py`

`starter.py` starts a basic tkinter GUI application named "Hello Name". The application consists of:

- an instruction label
- an input box for the user to enter their name
- a submit button
- an output label to display greetings or messages.

### Imports

[tkinter](https://docs.python.org/3/library/tk.html) is imported with the alias `tk` to allow for the creation of the main GUI components.

`messagebox` from `tkinter.messagebox` is imported for potential use in displaying pop-up errors.

HelloName Class Definition:

This class, `HelloName()`, inherits from `tk.Tk()` which is the main class for creating tkinter applications.

The `__init__()` method (the constructor) initializes the application window and its components.

`self.title(...)`, `self.geometry(...)`, and other configurations set up the main application window.

The get_name method is a placeholder function: it is called when the submit button is clicked. Currently, it does nothing (indicated by the pass statement).

The `if __name__ == "__main__":` block ensures the application runs when the script is executed directly. It initializes an instance of the `HelloName()` class and enters the main event loop with `app.mainloop().`
