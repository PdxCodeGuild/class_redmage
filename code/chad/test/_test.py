test_list = [1,2,3,4,5,6]

def test2(test_list):
    for i in range(len(test_list)):
        print(test_list[i])

def test1():
    test2(test_list)
    for num in test_list:
        print(num)

test1()