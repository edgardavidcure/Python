
highest_number = -1
scripture_name = ""
user_book = input("What book are you interested in?")
with open("/Users/edgardavidcure/Desktop/Python/books_and_chapters.txt") as file:
    for line in file:
        data = line.split(":")
        scripture = data[2].strip()
        book = data[0].strip()
        chapters = int(data[1])
        #print(f"scripture: {scripture}, book: {book}, chapters: {chapters}")
        if chapters > highest_number and scripture.lower() == user_book.lower():
            highest_number = chapters
            scripture_name = book
print (f"The book with most chapters is: {scripture_name} with {highest_number} chapters")

    









