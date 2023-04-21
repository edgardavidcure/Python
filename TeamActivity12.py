largest = -1
book_largest = ""
interest = input("Enter the name of the book you are interested in: ").capitalize()

with open("/Users/edgardavidcure/Desktop/Python/books_and_chapters.txt") as team_file:

    for line in team_file:
        data = line.split(":")
        scripture = data[2].strip()
        book = data[0].strip()
        chapters = int(data[1])
         
        if scripture.lower() == interest.lower():
            print(f"Scripture: {scripture}, Book {book}, Chapters: {chapters}")
            if chapters > largest:
                largest = chapters
                book_largest = book
print(f"The book with the most chapters is: {book_largest} with {largest} chapters. ")
   



        
