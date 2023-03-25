student_scores={"Harry":81,"Ron":78,"Hermione":99,"Draco":74,"Neville":62}
new_scores={}
print(len(student_scores))
for key in student_scores:
    if(student_scores[key]>91):
        new_scores[key]="Outstanding"
    elif(student_scores[key]>81):
        new_scores[key]="Exceeds Expectation"
    elif(student_scores[key]>71):
        new_scores[key]="Acceptable"
print(new_scores)