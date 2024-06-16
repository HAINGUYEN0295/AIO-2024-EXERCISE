def word_count(file_path):
    counter = {}
    with open(file_path, 'r') as f:
        data = f.read()
    data = data.lower()
    data = data.split()
    for word in data:
        counter[word] = counter.get(word, 0) + 1
    return counter


if __name__ == "__main__":
    file_path = 'MODULE-1-TOWARDS AI AND DS/WEEK 2/P1_data.txt'
    result = word_count(file_path)
    print(result['man'])
