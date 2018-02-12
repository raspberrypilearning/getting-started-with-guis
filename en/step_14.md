## CheckBox widget

The **CheckBox** widget allows you to select or deselect an option.

- Add the `CheckBox` widget to your `import` statement.

- Add a `CheckBox` object to the GUI:

    ```python
    vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")
    ```

    We also chose to add a `Text` widget in grid `[0,1]` to explain what the checkbox is for.

- Press <kbd>F5</kbd> to run your code. You should see the checkbox, and you should be able to tick and untick it.

    ![CheckBox demo](images/checkbox-demo.png)


