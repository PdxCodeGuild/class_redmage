def graph(data,peak,valley):
    print(peak)
    print(valley)
    print(data)
    length_data = len(data)
    for num in range(len(data)):
        print(num)
        #list index 
        if data.index(num) not in peak and data.index(num) not in valley:
            print('x')
        elif data.index(num) in peak:
            print('peak')
        elif data.index(num) in valley:
            print('valley')