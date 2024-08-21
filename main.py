import sys

def main() -> str:
    fs_path = "./books/frankenstein.txt"
    text = get_book_text(fs_path)
    #word_count = wordcount(text)
    #character_dictionary = character_counter(text)
    #clist = get_count_list(character_dictionary)
    print_report(fs_path, text)
    

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def wordcount(text_in: str) -> int:
    return len(text_in.split())

def character_counter(text_in: str) -> dict:
    char_dict = {}
    for c in text_in.lower():
        char_dict[c] = char_dict.get(c, 0) + 1
    return char_dict

def sort_on_high_count(d: dict) -> int:
    return d["count"]

def get_count_list(char_dict: dict) -> list:
    char_list = []
    for k in char_dict:
        if str(k).isalpha():
            char_list.append({"char": k, "count": char_dict[k]})
    char_list.sort(reverse=True, key=sort_on_high_count)
    return char_list

def print_report(path: str, text: str) -> None:
    print(f"--- Begin report of {path} ---")
    print(f"{wordcount(text)} words found in the document")
    for d in get_count_list(character_counter(text)):
        print(f"The '{d['char']}' character was found {d['count']} times")
    print("--- End report ---")

if __name__ == '__main__':
    main()
    sys.exit(0)