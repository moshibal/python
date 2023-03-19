#calculate the average height
total_height=0
total_num_of_student=0
students_height=input("please give a list of student heights ").split()
#basically changing to array of number.
for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])

#loop
for student_height in students_height:
   total_height+=student_height
   total_num_of_student+=1
average_height=(total_height/total_num_of_student)
print(f'the average height of the {total_num_of_student} students is {average_height}')