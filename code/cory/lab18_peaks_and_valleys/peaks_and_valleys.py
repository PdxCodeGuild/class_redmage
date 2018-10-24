# Version 2

# Define peaks, a peak has a lower number on both the left and right
def peak():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    out_list = []
    for i in range((len(data) - 1)):
        # print(i)
        if data[i - 1] < data[i] > data[i + 1]:
            # print(f"'>'+ {i}")
            out_list.append(i)
    return out_list

peak = peak()

# Define valleys, a valley is a number with a higher number on both the left and right

def valley():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    out_list = []
    for i in range(1, (len(data) - 1)):
        # print(i)
        if data[i - 1] > data[i] < data[i + 1]:
            # print(f"'>'+ {i}")
            out_list.append(i)
    return out_list

valley = valley()

# uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data

def peaks_and_valleys():
    out_list = []
    out_list.extend(peak + valley)
    # Returns peaks and values in order of apperance by index
    out_list.sort()
    return out_list

peaks_and_valleys = peaks_and_valleys()

# print(peaks_and_valleys)

def chart_func():
    data_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    out_string = ''

    for num in range(9, -1, -1):
        for data in data_list:
            if data > num:
                out_string += "X "
            else:
                out_string += "  "
        out_string += '\n'
    return out_string

    # trying to make the 'O's work

    # for num in range(9):
    #     for i in range(len(data_list)):
    #         if data_list[i] > num:
    #             out_string += "X "
    #         elif data_list[i] < 7:
    #             out_string += 'O '
    #         else:
    #             out_string += "  "
    #     out_string += '\n'
    # return out_string

print(chart_func())

print(peaks_and_valleys, end='\n')