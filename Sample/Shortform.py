sentence = input("Enter the full form: ")
List = sentence.split()
shortform = " "
for x in List:
    #shortform =" ".append(x[0].upper())
    shortform = shortform+str((x[0]).upper())
    #shortform1 = str(" ").append(str(x[0].upper()))
print(shortform)
print(shortform1)