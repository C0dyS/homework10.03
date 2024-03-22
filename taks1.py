def find_amount_of_selected_word(file_path,word):
    amount_of_selected_word = 0
    with open(file_path,'r') as file_1:
        for line in file_1:
            words = line.split()
            amount_of_selected_word += words.count(word)

    return amount_of_selected_word

print(find_amount_of_selected_word(r"C:\Users\sasha\Desktop\file1.txt",'hey'))