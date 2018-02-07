## CheckBox widget

The **CheckBox** widget allows you to select or unselect a true or false option.

- Add the `CheckBox` widget to your import statement.

- Add a `CheckBox` widget to the GUI:

    ```python
    vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")
    ```

    We also chose to add a `Text` widget in grid `[0,1]` to explain what the checkbox is for.

- Press F5 to run your code. You should see the checkbox appear and be able to tick and untick it.

    ![CheckBox demo](images/checkbox-demo.png)


