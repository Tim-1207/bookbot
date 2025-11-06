from stats import get_num_words, counting_characters, sort_on
import sys

def get_book_text(filepath):
    with open(filepath)  as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) <= 1:
        print("Hallo, lieber Buchanalyse-Liebhaber")
        print("Um ein bestimmtes Buch zu analysieren, bitte Startbefehl um Buchtitel erweitern:")
        print('             python 3 main.py <books/"Buchtitel.txt"> ')
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        count_char = counting_characters(text)
        sorted_list = sort_on(count_char)
        print_report(book_path, num_words, sorted_list)
   
      

def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing your book...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {item['num']}")
    print("============= END ===============")
    
main() 
