import re
import os

if __name__ == '__main__':
    print()

    # ex1
    sentence = ('234234312 435 gfd 45gfd6%%$ tre'
                'fds$fdg ^&%4f dfafdsf Gy/ael noiGfeld 432#$#'
                '123 456 abc %$# ag4$ fad/s%$ tertergh')
    # ex2
    search_type = re.compile(r'\w*[Gg]\w*')
    res = search_type.search(sentence)
    try:
        print(res.group())
    except:
        print("Not exist")

    # ex3
    words_after_space = re.findall(r'\s\w+', sentence)
    words_with_backslash = re.findall(r'\w*\/\w*', sentence)
    print("Words after space:")
    for word in words_after_space:
        print(word)
    print("\nWords with backslash:")
    for word in words_with_backslash:
        print(word)

    # ex4
    first_names = []
    last_names = []
    birth_dates = []
    id_numbers = []

    for i in range(3):
        user_input = input("Enter first name, last name, birth date (DD.MM.YY), and ID number separated by spaces: ")
        parts = user_input.split()

        if len(parts) != 4:
            print("Invalid input format. Please enter exactly 4 parts.")
            continue

        first_name, last_name, birth_date, id_number = parts
        first_names.append(first_name)
        last_names.append(last_name)
        birth_dates.append(birth_date)
        id_numbers.append(id_number)

    print("First Names:", first_names)
    print("Last Names:", last_names)
    print("Birth Dates:", birth_dates)
    print("ID Numbers:", id_numbers)


    #ex5
    file_content = """Hello world 1234
    This is a test 5678
    Python programming 9876
    My phone number is 0541234567
    Another line with 54321
    """

    file_path = 'sample.txt'
    with open(file_path, 'w') as f:
        f.write(file_content)

    with open(file_path, 'r') as f:
        lines = f.readlines()

    first_number_position = None
    phone_number_position = None
    long_words = []

    phone_pattern = re.compile(r'\b05[0-9]{8}\b')
    number_pattern = re.compile(r'\d+')

    for line_num, line in enumerate(lines):
        if first_number_position is None:
            match = number_pattern.search(line)
            if match:
                first_number_position = (line_num, match.start())

        phone_match = phone_pattern.search(line)
        if phone_match:
            phone_number_position = (line_num, phone_match.end())

        words = line.split()
        for word in words:
            if len(word) > 5:
                long_words.append(word)

    print("First number position:", first_number_position)
    print("Phone number end position:", phone_number_position)
    print("Long words:", long_words)

    #ex6
    def find_py_files(directory):
        python_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        return python_files


    directory_path = 'C:\\Users\\User\\Documents\\תכנות\\שנה ב\\python מתקדם\\תירגולים\\WEEK3'
    py_files = find_py_files(directory_path)

    print("Python files in directory:")
    for file in py_files:
        print(file)
