def first_task(file_1,file_2):
    with open(file_1,'r') as file_1:
        first_file_empty_check = file_1.readline()
        if first_file_empty_check == ' ':
            return -1
        file_1.seek(0)
        with open(file_2, 'r') as file_2:
            second_file_empty_check = file_2.readline()
            if second_file_empty_check == ' ':
                return -1
            file_2.seek(0)
            for file_1_line in file_1:
                for file_2_line in file_2:
                    if file_1_line != file_2_line:
                        print(f'{file_1_line} doesnt match {file_2_line}')

first_task(r'C:\Users\sasha\Desktop\file1.txt', r'C:\Users\sasha\Desktop\file2.txt')