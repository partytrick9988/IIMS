def vowelcount(name) :
    sum = 0 
    vowels = "aeiouAEIOU"
    for char in name :
        if char in vowels :
            sum += 1
    return sum
name = input("Enter your name: ")
result = vowelcount(name)
print(f"The number of vowels in {name} is {result}")

