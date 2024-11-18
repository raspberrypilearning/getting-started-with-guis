## ButtonGroup widget

The `ButtonGroup` widget allows you to create a group of radio buttons on your GUI so that users can choose one of a set of options.

- Add `ButtonGroup` to your `import` statement.

- Add a `ButtonGroup` widget to the GUI:

    ```python
    row_choice = ButtonGroup(app, options=[ ["Front", "F"], ["Middle", "M"],["Back", "B"] ],
    selected="M", horizontal=True, grid=[1,2], align="left")
    ```

    Let's look at this code more closely:
    - As before, `app` tells the `ButtonGroup` that the app is the boss.
    - `options` is a list of options which will appear as buttons. Note that each option is itself a list containing the button label and a hidden value associated with that option. (You will find out later what the hidden value is useful for.)
    - `selected` tells the `ButtonGroup` which button is selected to begin with.
    - `horizontal=True` tells the `ButtonGroup` to display in a horizontal line.
    - As with other widgets, `grid` specifies where the `ButtonGroup` will be placed on the grid, and `align="left"` positions the `ButtonGroup` on the left of the grid square.

- You can also add another `Text` widget in `[0,2]` to explain what the `ButtonGroup` is for.

- Press <kbd>F5</kbd> to run your code. You should see three buttons: the 'Middle' option should be selected when the program begins, and you should be able to switch between the options.

    ![Button Group demo](images/button-group.png)

