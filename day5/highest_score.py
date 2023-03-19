lists_score=input("please provide the lists of score of all the students.\n").split()
#converting the string of array to number of array

for n in range(0,len(lists_score)):
    lists_score[n]=int(lists_score[n])

highest_score=0
for score in lists_score:
    if score > highest_score:
        highest_score=score
print(f'the highest score in the student lists is {highest_score}.')