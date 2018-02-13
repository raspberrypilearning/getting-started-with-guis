## CheckBox widget

The `CheckBox` widget allows you to select or deselect an option.

- Add `CheckBox` to your `import` statement.

- Add a `CheckBox` widget to the GUI:

    ```python
    vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")
    ```

- You can also add a `Text` widget in grid `[0,1]` to explain what the checkbox is for.

- Press <kbd>F5</kbd> to run your code. You should see the `CheckBox`, you should be able to tick and untick it, and if you've added a `Text` widget as a label, this should be visible next to the check box.

    ![CheckBox demo](images/checkbox-demo.png)
