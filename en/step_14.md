## Finishing the program

Now that users of your ticket-booking GUI can choose a film and a seat, it's time to complete the GUI script so that they can place their booking.

- Add `PushButton` to the `import` statement, then add a `PushButton` widget in `[1,3]` which calls a function called `do_booking` when it is pressed.

    ```python
    book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[1,3], align="left")
    ```

    ![Booking button](images/booking-button.png)

- Add `info` (all lower case) to the `import` statement so that you can use the info box function of `guizero`.

- Above the GUI, write the function `do_booking()`. This will make an information box pop up.

    ```python
    def do_booking():
        info("Booking", "Thank you for booking")
    ```

    ![Info box](images/info-box.png)

You'll want to be able to retrieve the options the user chose, so that you can keep track of which seats in your cinema are booked.

- Add this code to your `do_booking()` function to access the values of your widgets:

    ```python
    print( film_choice.value )
    print( vip_seat.value )
    print( row_choice.value )
    ```

    Note: `CheckBox` returns `0` if it is not checked and `1` if it is checked, and `ButtonGroup` returns the hidden value (`F`, `M`, or `B`) instead of the full label of the option that was chosen.

    ![Return values](images/return-values.png)


