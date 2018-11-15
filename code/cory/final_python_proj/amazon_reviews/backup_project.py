with open('scrape_scifi_data_Nov-11-2018_14-13-01.csv', 'r') as f:
    scrape_scifi_data = f.read().strip().split('\n')
f.close()

# Reverting '+' back to ','
def add_comma(string):

    new_string = ''
    for char in string:
        if char == '+':
            new_string += ','
        else:
            new_string += char

    return (new_string)

header = scrape_scifi_data[0].split(',')
scifi_data = [scrape_scifi_data[i].split(',') for i in range(1, len(scrape_scifi_data))]

# Adds commas back into each string in each index
for x in range(len(scifi_data)):
    for y in range(len(scifi_data[x])):
        scifi_data[x][y] = add_comma(scifi_data[x][y])

# Final List to contain scifi_data
scifi_dictionaries = []

# For each book >
for x in range(len(scifi_data)):
    # Create a key, value set from header and scifi_data[x]
    # scifi_dictionaries.append([{header[y]: scifi_data[x][y] for y in range(len(header))}])
    scifi_dictionaries.append({header[y]: scifi_data[x][y] for y in range(len(header))})

# Divider for screen clarity
div = "\n - - - - - - - - \n"

def genre_scifi():

    while True:
        print(div) 

        scifi_input = input("\nWelcome to the Sci-fi genre, please choose an option:\n"
        + "\nTop Books\n"
        + "Top Authors\n"
        + "Most Reviewed\n"
        + "All Books\n"
        + "\n> "
        ).lower()

        if scifi_input == 'top books':
            
            print(div)

            print("\n The top Sci-Fi books are as follows:\n")
            for num in range(10):
                print(f"> {num + 1}.) {scifi_dictionaries[num]['Title']}\n")

            # User input for which books
            u_i = input("Which book would you like to look at? > ").lower()

            def book_choice(u_i):
                # List of titles being displayed
                t_l = [scifi_dictionaries[num]['Title'].lower()                                                         for num in range(10)]
                
                if u_i in t_l:
                    
                    # Uses book as key, value as index. The user will choose a book, which will return a index value.
                    t_n = {scifi_dictionaries[num]['Title'].lower(): int(num) for num in range(10)}

                    return t_n[u_i]
                
                elif int(u_i) in range(1, 11):
                    return int(u_i) - 1

            print(div)

            # I should turn this into a function.
            print(
                "Purchase link: " + scifi_dictionaries[book_choice(u_i)]['Purchase Link']
                
                + "\nTitle: " + scifi_dictionaries[book_choice(u_i)]['Title']
                
                + "\nAuthor: " + scifi_dictionaries[book_choice(u_i)]['Author']
                
                + "\nRelease Date: " + scifi_dictionaries[book_choice(u_i)]['Publish Date']
                
                + "\nCost: " + scifi_dictionaries[book_choice(u_i)]['Cost']
                
                + "\nBook Type(s): " + scifi_dictionaries[book_choice(u_i)]                                                    ['Book Types']
                
                + "\nRating / Reviews: " + scifi_dictionaries[book_choice(u_i)]                                                ['Rating']
                
                + ', ' +scifi_dictionaries[book_choice(u_i)]['Review Number'] +                                                " Reviews.\n"
                
                + "\nSynopsis: \n" + scifi_dictionaries[book_choice(u_i)]                                                      ['Synopsis']  
            )

            print(div)
            
            user_continue = input("Press enter to continue... ")

        elif scifi_input == 'top authors':

            print(div)

            # Creates a list just for authors
            author_list = [scifi_dictionaries[i]['Author'] for i in range(len(scifi_dictionaries))]

            # Creates a dictionary, key is author and value is number of times the author comes up
            author_dict = {}
            for key in author_list:
                if key in author_dict:
                    author_dict[key] += 1
                else:
                    author_dict.update({key:1})

            # Sorts by greatest
            top_authors = list(author_dict.items())
            top_authors.sort(key=lambda tup: tup[1], reverse=True)

            # String of authors
            for num in range(10):
                print(f"> {num + 1}.) {top_authors[num][0]} has writen {top_authors[num][1]} books.\n")


            # Look up books by author
            user_input = input("\nWould you like to see the titles available from an author? (y/n) > ").lower()

            if user_input == 'y':
                
                user_input = input("\nWhich author would you like to look up? > ")

                print(div)

                if user_input in author_list:
                    for i in range(len(scifi_dictionaries)):
                        if scifi_dictionaries[i]['Author'] == user_input:
                            print('\n' + scifi_dictionaries[i]['Title'] + '\n')

                user_continue = input("\nPress enter to continue... ")

        elif scifi_input == 'most reviewed':

            print(div)

            # Creates a list just for viewed variables
            review_dict = {scifi_dictionaries[i]['Title']: int(scifi_dictionaries[i]['Review Number']) for i in range(len(scifi_dictionaries))}

            # Sorts by greatest
            most_reviews = list(review_dict.items())
            most_reviews.sort(key=lambda tup: tup[1], reverse=True)

            # String of authors
            for num in range(10):
                print(f"> {num + 1}.) {most_reviews[num][0]} has {most_reviews[num][1]} reviews.\n")

            user_continue = input("\nPress enter to continue... ")

        elif scifi_input == 'all books':
            
            # Creates a list just for title variables
            all_list = [scifi_dictionaries[i]['Title'].strip("'").strip('"') for i in range(len(scifi_dictionaries))]

            all_list.sort()

            # Function for changing pages
            def page_changer(page_num):
                if page_num == 1:
                    return (0, 10)
                elif page_num == 2:
                    return (10, 20)
                elif page_num == 3:
                    return (20, 30)
                elif page_num == 4:
                    return (30, 40)
                elif page_num == 5:
                    return (40, 50)
                elif page_num == 6:
                    return (50, 60)

            page = page_changer(1)

            while True:

                print(div)

                for num in range(page[0], page[1]):
                    print(f"> {num + 1}.) {all_list[num]}\n")

                print(div.lstrip('\n'))
                
                loop_permission = input("Would you like to change pages, look at a book ('look'), or quit? > ")

                if loop_permission == "change pages":
                    change_page = input("\nWhich page would you like to go to? (1 - 6) > ")

                    try:
                        change_page = int(change_page)
                        if int(change_page) in range(1, 7):
                            page = page_changer(int(change_page))
                    except ValueError as ValueError:
                            pass
                
                if loop_permission == "look":
                    pass

                if loop_permission == 'quit':
                    break
                
            
        elif scifi_input == 'quit':
            return

genre_scifi()

def user_interface():
    interface_flag = True
    while interface_flag:
        
        menu_permission = ['options', 'genres', 'about', 'sci-fi', 'scifi' 'quit']

        menu_input = input("\nWelcome to PDX Book Guild, what would you like to do today? (try 'options'): > ").lower()

        if menu_input == 'options':

            print(div)

            print(
                "\nA list of options are as follows, type these in at the main menu:\n"
                + "\nGenres\n"
                + "About"
                )
            
            print(div)
            
        elif menu_input == 'genres':
            
            print(div)
            
            print(
                "\nThe following genres are available, type these in at the main menu:\n"
                + "\nSci-fi"
            )
            
            print(div)
            
        elif menu_input == 'about':
            
            print(div)
            
            print("\nThis is a project created for the purpose of showcasing the skills I have learned from PDX Code Guild.")
            
            print(div)
            
        elif menu_input == 'sci-fi' or menu_input == 'scifi':
            genre_scifi()

        elif menu_input == 'quit':
            return

        elif menu_input not in menu_permission:
            print("The program didn't like that answer... Please try again.\n")

# user_interface()

# Purchase Link,Title,Author,Publish Date,Cost,Book Types,Rating,Review Number,Synopsis