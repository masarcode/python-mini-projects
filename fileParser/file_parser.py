def parse_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        clean_text = ''.join(char for char in text if char.isalnum() or char.isspace()).lower()
        words = clean_text.split()

        word_count = len(words)

        freq_dict = {}
        for word in words: 
            freq_dict[word] = freq_dict.get(word, 0) + 1

        most_common = max(freq_dict, key = freq_dict.get)

        print(f"-- File Analysis: {filename} ---")
        print(f"Total Words: {word_count}")
        print(f"Most Frequent Word: '{most_common}' (appears {freq_dict[most_common]} times)")

    except FileNotFoundError:
        print("File not found. Please create 'sample.txt' first.")

with open('sample.txt', 'w') as f:
    f.write("Python is great. Python is fun. Learning Python is key.")

parse_file('sample.txt')
