#If num is the first number put X in graph for starting point add one to counter
        if num == 0:
            graph_data.append(counter+1)
            counter += 1
            print('First Iteration adding one')
            continue
        #if data in index num is not in a peak of valley run this
        if data[num] not in peak and data[num] not in valley:
            if data[num] > data[num - 1]:
                graph_data.append(counter+1)
                counter += 1
                print('Not in adding one')
            elif data[num] < data[num-1]:
                graph_data.append(counter-1)
                counter -= 1
                print('not in minus one')
        #if data in index num IS in a peak of valley run this
        if data[num] in peak: 
            graph_data.append(counter+1)
            counter += 1
            print('Is in adding one')

        if data[num] in valley:
            graph_data.append(counter-1)
            counter -= 1
            print('Is in minus one')