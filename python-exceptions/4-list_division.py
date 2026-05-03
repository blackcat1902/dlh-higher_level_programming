#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Try to access elements
            a = my_list_1[i]
            b = my_list_2[i]

            # Check types
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError

            # Perform division
            value = a / b

        except ZeroDivisionError:
            print("division by 0")
            value = 0
        except TypeError:
            print("wrong type")
            value = 0
        except IndexError:
            print("out of range")
            value = 0
        finally:
            result.append(value)

    return result
    