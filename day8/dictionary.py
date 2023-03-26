student_scores={"Harry":81,"Ron":78,"Hermione":99,"Draco":74,"Neville":62}
#new array
new_scores={}

#loop in student_scores dictionary>gives you the key
for key in student_scores:
    #accessing the value with the key,and comparing,if true,adding to the new dictionary with the same name.
    if(student_scores[key]>91):
        new_scores[key]="Outstanding"
    elif(student_scores[key]>81):
        new_scores[key]="Exceeds Expectation"
    elif(student_scores[key]>71):
        new_scores[key]="Acceptable"
print(new_scores)