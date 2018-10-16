padj1 = input("Give me an adjective for a person: ")
padj2 = input("Give me an adjective for a person: ")
sadj1 = input("Give me a speed: ")
dadj1 = input("Give me a duration: ")
num1 = input("Give me an integer: ")
lnoun1 = input("Give me a location noun: ")
cnoun1 = input("Give me a conflict noun: ")
noun3 = input("Give me a noun: ")
noun4 = input("Give me an noun: ")
noun5 = input("Give me an assistance noun: ")
noun6 = input("Give me a clothing noun: ")
noun7 = input("Give me a path noun: ")
noun8 = input("Give me a person noun: ")
noun9 = input("Give me a noun: ")
noun10 = input("Give me a smelly noun: ")
noun11 = input("Give me a currency noun: ")
verb1 = input("Give me a daytime verb: ")
verb2 = input("Give me a nighttime verb: ")
verb3 = input("Give me a verb for writing: ")
verb4 = input("Give me a verb: ")
activitynoun1 = input("Give me an activity: ")
activitynoun2 = input("Give me an activity: ")
activitynoun3 = input("Give me an activity: ")
comverb1 = input("Give me a reporting verb (eg. said): ")

par1 = f"""There once was an {padj1}, {padj2} lady that lived in a {lnoun1}. 
She had {num1} children and she did not know what to do. 
She would {verb1} all day and {verb2} all night and pull apart her children when they got in a {cnoun1}. 
She did not have {noun3} for {activitynoun1} or {activitynoun2}. 
"You've got too many {noun4}!" her neighbors would {comverb1}. 
She decided to look for some {noun5} to reduce her load. 
So she put on her {noun6} and walked down the {noun7}. 
Down at the canteen she found a {noun8}. 
It needed a[n] {noun9} for it smelled like a {noun10}, but it wanted some {noun11} for booze, and she 
needed help to find time to {activitynoun3}. 
So she {verb3} up a contract and he {verb4} it real {sadj1}. 
Let's hope that this arrangement will {dadj1}."""

print(par1)