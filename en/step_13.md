## Combo widget

The `Combo` widget allows you to select an option from a drop-down menu.

- Add `Combo` to your `import` statement.

- Add a `Combo` widget to the GUI:

    ```python
    film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1,0], align="left")
    ```

    - As usual, we have specified the `app` parameter to tell the `Combo` widget that the app is its master.
    - The `options` argument is a list of options we wish to display in the widget.
    - Because we specified `layout=grid` in the `app` object, we have to now include a `grid` argument with each widget to tell it where to appear. The `grid` argument should be a list containing `[x,y]` values for where you would like the widget to appear on the grid. `[0,0`] on the grid is the top left-hand corner. We can also `align` the widget within the grid square, in this case on the `"left"`.

- Save your code and press <kbd>F5</kbd> to run it. Note that the `Combo` widget appears in the very top left of the screen, even though we specified its grid position as `[1,0]`. This is because grid square `[0,0]` is empty, and empty grid squares have no height or width.

- Add the `Text` widget to your `import` statement, then add a `Text` object in grid square `[0,0]` to provide some description of what the person will be selecting using the `Combo` widget:

    ```python
    film_description = Text(app, text="Which film?", grid=[0,0], align="left")
    ```

    Run the program to check that the `Text` and the `Combo` are both displayed properly.

    ![Combo with text](images/combo-with-text.png)

