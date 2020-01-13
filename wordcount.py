# put your code here.

def word_counter(file_name):
    """Takes in a text file and prints the number of each word in the text file
    by space. Includes words with punctuation as seperate words."""

# create empty dictionary
    word_count_dict = {}

# open file
    text_file = open(file_name)


    # text_file = text_file.read()


    # print(text_file[0])

# get each line without right space
    for line in text_file:
        line = line.rstrip()


# split by space into list       
        word_list = line.split(' ')
        #print(word_list)

        for word in word_list:

            word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict
    # print(word, word_count_dict[word])


# count each word in the list and put in dict
# print each pair

def print_word_counts(count_dict):

    for item in count_dict.items():
        print(item[0], " ", item[1])




word_counts = word_counter("test.txt")

print_word_counts(word_counts)
