
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    number_of_words = get_number_words(text)
    #print(number_of_words)
    chars = get_letter_count(text)

    #print report using sorted character dictionary
    printed_book_report(book_path, number_of_words, sorted_char_dictionary(chars))
    
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_words(book_text):
    words = book_text.split()
    return len(words)

def get_letter_count(book_text):
    #dictionary of the letter and the count {"letter": count}
    letter_count = {}

    #convert to lower case string to homogenise data
    lowercase_book_text = book_text.lower()

    for letter in lowercase_book_text:
        #Check if letter exists in the dictionary already
        if letter in letter_count :
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    #Return the count of letters occuring in a string
    return letter_count

def sort_on(dict):
    return dict["num"]

def sorted_char_dictionary(char_dictionary):
    sorted_char_dict = []
    
    #Sort the character dictionary into structure [{"char": "x", "num" : 1},]
    for key in char_dictionary:
        if key.isalpha():
            new_char_count = {}
            new_char_count["char"] = key
            new_char_count["num"] = char_dictionary[key]
            sorted_char_dict.append(new_char_count)

    
    sorted_char_dict.sort(reverse=True, key=sort_on)
     
    return sorted_char_dict

def printed_book_report(book_path, word_count, sorted_char_dict):
    #Report structure for printing
    structured_report = f"--- Begin report of {book_path} ---"
    word_count_report = f"{word_count} words found in the document"
    end_of_report = f"--- End Report ---"

    print(structured_report)
    print(word_count_report)

    for i in range(len(sorted_char_dict)):
        char = sorted_char_dict[i]["char"]
        char_count = sorted_char_dict[i]["num"]

        print(f"The '{char}' character appears was found {char_count} times")

    print(end_of_report)

main()