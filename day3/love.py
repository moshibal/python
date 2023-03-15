# get the input name of both
boy_name=input("type your boy name? ").lower()
girl_name=input("type your girl name? ").lower()
# count number of letter occur in true and love
t=boy_name.count("t")+girl_name.count("t")
r=boy_name.count("r")+girl_name.count("r")
u=boy_name.count("u")+girl_name.count("u")
e=boy_name.count("e")+girl_name.count("e")
true=t+r+u+e

l=boy_name.count("l")+girl_name.count("l")
o=boy_name.count("o")+girl_name.count("o")
v=boy_name.count("v")+girl_name.count("v")
e=boy_name.count("e")+girl_name.count("e")
love=l+o+v+e

totalNum=int(str(true)+str(love))

if totalNum < 10 or totalNum > 90:
    print(f"your score is {totalNum}, you go together like coke and mentos")
elif totalNum>40 and totalNum<50:
    print(f"your score is {totalNum}.you are alright together.")
else:
    print(f"your score is {totalNum}")