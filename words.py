def print_upper_words(words,must_start_with):
    """prints out each word of words in uppercase if it starts with a letter in must_start_with"""
    for word in words:
        for letter in must_start_with:
            if word[0] == letter or word[0] == letter.upper():
                print(word.upper())
        
# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})