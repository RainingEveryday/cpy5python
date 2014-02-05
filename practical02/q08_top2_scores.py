#8 Finding top two scores:

number = int(input("Please enter the number of students: "))

namelist = []
scorelist = []

while number > len(namelist):
    name = str(input("Please enter the name of the student: "))
    score = float(input("Please enter the score of " + name + ": "))
    namelist.append(name)
    scorelist.append(score)

first = scorelist.index(max(scorelist))
second = scorelist.index(max(score for score in scorelist if score < max(scorelist)))

print("{0} has the highest score with {1}.".format(namelist[first], scorelist[first])) 
print("{0} has the second highest score with {1}.".format(namelist[second], scorelist[second]))
