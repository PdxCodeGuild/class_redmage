
listNames = ['Dan', 'Neil', 'Chad', 'David', 'Zuriel', 'Tom']
listNames2 = ['Dan', 'Chad', 'Chad', 'David', 'Zuriel', 'Tom']


enumList1 = list(enumerate(listNames))
enumList2 = list(enumerate(listNames2))

for test_value in range(6):

   if enumList1[test_value] == enumList2[test_value]:
      print('won')
   else:
      print('You Loose')



