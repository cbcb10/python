from random import  random
if __name__ == '__main__':

# ex1
    numbers = []
    while True:
        user_input = input("enter a number or 'q' to finish: ")
        if user_input.lower() == 'q':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("please enter numbers only or 'q' to finish")
    if numbers:
        average = sum(numbers) / len(numbers)
        print("the average of the numbers entered: ", average)
    else:
        print("No numbers entered")

# ex2
    def divideNoNumber(number_list, number):
        res = [num for num in number_list if num % number != 0 ]
        print(res)
        return res
    divideNoNumber([1,2,4,5,6,7,8,9,12,14,15],3)

# ex3
    input_ex3 = input("enter a string")
    if input_ex3 == input_ex3[::-1]:
        print("palindom")
    else:
        print("not palindrom")

# ex4
#     print("enter 3 numbers between 0-9")
#     num1 = int(input("number 1: "))
#     num2 = int(input("number 2: "))
#     num3 = int(input("number 3: "))
#     rand1 = random.randint(0, 9)
#     rand2 = random.randint(0, 9)
#     rand3 = random.randint(0, 9)
#     if num1 == rand1 and num2 == rand2 and num3 == rand3:
#         print("You win!!!")
#     else:
#         print("You lose...")


# ex5
    def sum_in_file(file_name):
        try:
            with open(file_name, 'r') as file:
                numbers = file.readlines()
                total_sum = sum(map(int, numbers))

            with open(file_name, 'a') as file:
                file.write(f"\n{total_sum}")

            print("The sum was written successfully")

        except FileNotFoundError:
            print("Error! the file wasn't found.")
        except Exception as e:
            print(f"Unexpected error: {e}\n")

    sum_in_file("abc.txt")

    def count_any_number(numbers_list):
        counts=[0]*10
        for num in numbers_list:
            counts[num] += 1
        return  counts

    c=[3,5,6,2,5,4,2,5,6,7,2,4,5,6,7,6,3,4,6,2,2,6,8,8,8,4,3,3,1,1,2,2,0]
    print(count_any_number(c))


    def pos_int_num(numbers_list):

        for num in numbers_list:
            if not isinstance(num, int):
                raise ValueError("All values in the list must be integers.")
            elif num <= 0:
                raise ValueError("All values in the list must be positive.")
        return True

    list = [3, 5, 2, "fs", 2]
    try:
        pos_int_num(list)
        print("All values in the list are positive integers.")
    except ValueError as e:
        print("Error:", e)
