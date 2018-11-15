import os



def rule_file():
    # Directory to rules folder
    dir = '/Users/chadbean/Documents/Programing and Development/github/class_redmage/code/chad/python_final_project/rules'

    os.chdir(dir)
    print(os.getcwd())
    with open('__keyword_Filepointer.csv', 'r') as rules_file:
        rules = rules_file.read().strip('\n').split('\n')
    rules_file.close()
    print(rules)
    for i in rules:
        print(i)
rule_file()