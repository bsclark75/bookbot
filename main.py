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
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        wc = word_count(file_contents)
        print(wc)
        cc = character_count(file_contents)
        print(cc)

main()
