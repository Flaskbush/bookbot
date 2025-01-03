def print_report_start():

    print("\n--- Begin report of books/frankenstein.txt ---\n")
    


def count_words():

    with open("books/frankenstein.txt", "r", encoding="utf-8") as file:

        file_contents = file.read()

        words = file_contents.split()

        word_count = len(words)

    print(f"\n{word_count} words were found in the document\n")



def count_letters_in_file():
    
    letter_counts = {}

    with open("books/frankenstein.txt", "r", encoding="utf-8") as file:
        text = file.read().lower()  

   
    for char in text:
        if char.isalpha():  
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1


    sorted_letter_counts = dict(sorted(letter_counts.items()))
    for letter, count in sorted_letter_counts.items():
        print(f"The '{letter}' character was found {count} times")



def print_report_end():
     
    print("\n--- End report ---\n")




if __name__ == "__main__":
    print_report_start()
    count_words()
    count_letters_in_file()
    print_report_end()





     
        
    






    







