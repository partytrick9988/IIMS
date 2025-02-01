#Mutable = list , dictionary , set (Direct modification is possible) mpdification of this data does not change the ram used
#Immutable = int , flat , str , tuple (Modification creates new object)modification does change the ram used unless the previous data is deleted the new data takes new space increasing the amount of ram used




fruit_basket = []

fruit_basket.append("appple")
fruit_basket.append("banana")
fruit_basket.append("orange")
fruit_basket.append("apple")
fruit_basket.append("banana")
fruit_basket.append("orange")

print(fruit_basket)
print(fruit_basket[-3])
print(fruit_basket[-2])
print(fruit_basket[-1])

s = "ruman"
print(fruit_basket[::2])

fruit_basket.remove("apple")
print(fruit_basket)



student_form = {
    "name" : "ruman",
    "age" : "28" ,
    "gender": "male"
}

print(student_form["name"])
print(student_form["age"])
print(student_form["gender"])


student_form["name"] = "pratik"
student_form["address"] = "ktm"

print(student_form)