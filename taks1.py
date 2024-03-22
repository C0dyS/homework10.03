def find_longest_line(file_path):
    with open(file_path,'r') as file_1:
        content = file_1.readlines()
    longest_line = ''
    for line in content:
        if len(line) > len(longest_line):
            longest_line = line
    return print(f'''
longest line is {longest_line}
''')
find_longest_line(r"C:\Users\sasha\Desktop\file1.txt")