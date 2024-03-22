def third_task(file_1_path):
    with open(file_1_path, 'r') as file_1:
        lines = file_1.readlines()
        if lines:
            del lines[-1]


    with open(file_1_path, 'w') as file_1:
        file_1.writelines(lines)

    file_2_path = r"C:\Users\sasha\Desktop\new_file.txt"
    with open(file_2_path, 'w') as file_2:
        file_2.writelines(lines)

third_task(r"C:\Users\sasha\Desktop\file1.txt")
