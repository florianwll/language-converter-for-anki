def split_vocabulary(file_path, output_path1, output_path2):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    words1 = []
    words2 = []
    
    for line in lines:
        if '-' in line:
            word1, word2 = line.split(' - ')
            words1.append(word1.strip())
            words2.append(word2.strip())
    
    with open(output_path1, 'w', encoding='utf-8') as file1, open(output_path2, 'w', encoding='utf-8') as file2:
        for word in words1:
            file1.write(word + '\n')
        for word in words2:
            file2.write(word + '\n')

# Example usage
input_file = 'vok.txt'
output_file1 = 'output_file1.txt'  # Words in the first language
output_file2 = 'output_file2.txt'  # Words in the second language

split_vocabulary(input_file, output_file1, output_file2)
    