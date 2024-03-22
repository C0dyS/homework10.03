def second_task(file_1):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    with open(file_1, 'r') as file_1:
        content = file_1.read()

    number_of_vowels_in_file_1 = 0
    number_of_consonants_in_file_1 = 0
    number_of_characters_in_file_1 = 0
    number_of_numerics_in_file_1 = 0
    for char in content:
        number_of_characters_in_file_1 += 1
        if char in vowels:
            number_of_vowels_in_file_1 += 1
        elif char in consonants:
            number_of_consonants_in_file_1 += 1
        elif char.isdigit():
            number_of_numerics_in_file_1 +=1
    number_of_lines_in_file_1 = sum(1 for line in content)
    file_2_path = r'C:\Users\sasha\Desktop\data_of_file_1.txt'
    with open(file_2_path, 'w') as file_2:
        file_2.write(f'Number of characters: {number_of_characters_in_file_1}\n')
        file_2.write(f'Number of lines: {number_of_lines_in_file_1}\n')
        file_2.write(f'Number of vowels: {number_of_vowels_in_file_1}\n')
        file_2.write(f'Number of consonants: {number_of_consonants_in_file_1}\n')
        file_2.write(f'Number of numerics: {number_of_numerics_in_file_1}\n')



second_task(r"C:\Users\sasha\Desktop\file1.txt")

