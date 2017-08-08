## PushButton widget

**PushButton** widgets create a button. When the button is pushed, a function is called.

- **Before** the code which creates the GUI app, write a function which will be called when the button is pressed. It is a good idea to put all of your function code at the start of your program, immediately after the `import` line.

    ```python
    def say_my_name():
        welcome_message.set( my_name.get() )
    ```

    This function refers to the `Text` widget (`welcome_message`) and sets its value to what was typed into the `TextBox` widget (`my_name`).
    You can use the `get()` and `set()` functions with many widgets to retrieve their current value or set them to something new.

- Add the `PushButton` widget to your import statement.

- Add a `PushButton` to the GUI:

    ```python
    update_text = PushButton(app, command=say_my_name, text="Display my name")
    ```

    The first argument tells the PushButton that the app is its boss. Then we use two keyword arguments - `command` tells the button which function to call when it is pressed, and `text` is the text which will be displayed on the button.

- Press F5 to run your code. Type your name into the text box and then press the button. You should see your name displayed in large text at the top.

    ![Display my name](images/display-my-name.png)

    You have now experienced the basis for how the event loop works. The GUI waits for an event (in this case, you clicking on the button) and it calls a function in response to the event. This function may contain code to change something on the GUI, and if so, the display is updated accordingly.


