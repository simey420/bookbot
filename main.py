import sys
from stats import get_wordcount, get_charcount, sort_dict


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        bookpath = sys.argv[1]
        
        def get_book_text(path_to_file):
            file_contents = ""

            with open(path_to_file) as f:
                file_contents = f.read()

            return file_contents        
        
        text = get_book_text(bookpath)

        wordcounte = get_wordcount(text)
        charcount = get_charcount(text)
        
        print(f"{wordcounte} words found in the document")
        charlist = sort_dict(charcount)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookpath}")
        print("----------- Word Count ----------")
        print(f"Found {wordcounte} total words")
        print("--------- Character Count -------")
        for x in charlist:
            if x["char"].isalpha():
                print(f"{x["char"]}: {x["num"]}")
        print("============= END ===============")

main()