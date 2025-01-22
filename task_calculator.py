import re

class Calculator_add:
    def calculate_sum(self, num1):
        if not num1:  # input string is empty, return 0
            return 0

        negative_num = []
        
        # string starts with "//", handle custom delimiter
        if num1.startswith("//"):
            delimiter = num1[2:3]  # extract delimiter
            num1 = num1[4:]  # Remove the delimiter

            # split the numbers 
            list_n = re.split(f"[{delimiter}\n]", num1)

            # check negative numbers
            for i in list_n:
                num = int(i)

                if num < 0:
                    negative_num.append(num)

            if negative_num:
                raise ValueError(
                    f"negative numbers not allowed: {', '.join(map(str, negative_num))}"
                )

            # sum of the integers
            return sum(map(int, list_n))

        else:
            # split by commas and newlines
            v = re.split("[,\n]", num1)

            # Check negative numbers
            for i in v:
                num = int(i)
                if num < 0:
                    negative_num.append(num)

            if negative_num:
                raise ValueError(
                    f"negative numbers not allowed: {', '.join(map(str, negative_num))}"
                )

            # Return sum integers
            return sum(map(int, v))


if __name__ == "__main__":
    add_num = Calculator_add()

    try:
        print(add_num.calculate_sum(""))  # Expected 0
        print(add_num.calculate_sum("1"))  # Expected 1
        print(add_num.calculate_sum("1,5"))  # Expected 6
        print(add_num.calculate_sum("1\n2,3"))  # Expected 6
        print(add_num.calculate_sum("//;\n1;2"))  # Expected 3
        print(add_num.calculate_sum("1,2,-3,4"))  # Raise an exception due to negative number (-3)

    # Exception handling
    except ValueError as ex:
        print(ex)  # Print the error message
