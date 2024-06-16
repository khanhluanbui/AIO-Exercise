#exercise 3:

def word_count(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Đọc nội dung file và chuyển tất cả về chữ thường\
        file.close()

    word_list = text.split()
    word_frequency = {}

    for word in word_list:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

    sorted_word_frequency = dict(sorted(word_frequency.items()))  # Sắp xếp dictionary theo thứ tự bảng chữ cái
    return sorted_word_frequency


if __name__ == "__main__":
    file_path = 'module01/week02/P1_data.txt'
    print(word_count(file_path))