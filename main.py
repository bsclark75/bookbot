import string

def word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def character_count(text):
    count_dict = {}
    for char in text:
        char = char.lower()
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def main():
    alphabet = list(string.ascii_lowercase)
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        wc = word_count(file_contents)
        print(f"{wc} words found in the document")
        cc = character_count(file_contents)
        #print(type(cc))
        for k,v in cc.items():
            if k in alphabet:
                print(f"The '{k}' character was found {v} times")
        print("--- End of report ---")
        

main()
