def int_selection(valid_answers=set, message=str, error_message=str):
    while True:
        try:
            selection = int(input(message))
            if (selection in valid_answers or selection < 0):
                return selection
            print(f'Selection not availible: {error_message}')
        except ValueError:
            print(f'Invalid Selection: {error_message}')