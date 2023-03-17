row1=["🙈","🙈","🙈"]
row2=["🙈","🙈","🙈"]
row3=["🙈","🙈","🙈"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
#getting the position
position=(input("where do you want to place the treasure? please know first letter will be col and second letter will be row. "))
#chaning that into int and also reducing 1 as lists starts with 0
col_position=(int(list(position)[0])-1)
row_position=(int(list(position)[1])-1)
#first finding the row, as to find col in that row would be easy because its a same list, all we need is the column number
fetch_row=map[row_position]
#after knowing row, we swap the value of the col position with x.
fetch_row[col_position]="X"
#final print
print(f"{row1}\n{row2}\n{row3}")
