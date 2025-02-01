""""
stu_list = ["a" , "b" , "a" , "b"]
stu_tuple =(1,2,3)
stu_set ={"name" , ""}
stu_dictionary = {"name" : "Roman" , "age" : 18 , "gender" : "male"}


stu_list =set (stu_list)
stu_tuple = tuple(stu_list)
stu_set = list (stu_tuple)
print(stu_list , stu_tuple , stu_set , stu_dictionary)
"""

emptlist = []

while True : 
    uinput = input("Enter name : ")
    if uinput == "q" :
        quit()
    emptlist.append(uinput)

    for i , name in enumerate(emptlist) :
        print(i , name)

s