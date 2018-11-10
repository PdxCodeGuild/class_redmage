with open('scrape_data.csv', 'r') as f:
    data = f.read().strip().split('\n')
f.close()   


header = data[0].split(',')
print(header)

book_list = []
for i in range(1, len(data)):
    book_list.append(data[i] for i in range(1, len(data)))

book_list = book_list[1].split(',')
print(book_list)