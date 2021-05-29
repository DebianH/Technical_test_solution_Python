"""
Problem 1 (A) 
* Create an Object with a "hello" method that writes 
"Hello <name> in the console".
"""
print("++++ Solution 1 ++++\n")

def Hello(name):
    greet = "hello"
    return greet + " " + name
       
p = Hello('Carlos')
print(p)


"""
Problem 2 (B)
* How would you make the name inmutable?
* (Can write or juts describe)
"""
print("\n---- Solution 2 ----\n")

def Hello_Inmutable(name):
    greet = "hello"
    
    if name != "Carlos": #Add this line so that the result does not change
        name = "Carlos"  #In python there is no JS freeze function

    return greet + " " + name
       
d = Hello_Inmutable('Pedro')
print(d)


"""
Problem 3 
* Write a function that logs the 5 cities that occur the most in the array below in
* order from the most number of occurences to least.
"""
print("\n____ Solution 3 ____\n")

cities_List = [
    "nashville",
    "nashville",
    "los angeles",
    "nashville",
    "memphis",
    "barcelona",
    "los angeles",
    "sevilla",
    "madrid",
    "canary islands",
    "barcelona",
    "madrid",
    "nashville",
    "barcelona",
    "london",
    "berlin",
    "madrid",
    "nashville",
    "london",
    "madrid",
    ]
    
cities = dict()

for city in cities_List:
    cities[city] = cities.get(city,0) + 1 

c = cities

c2 = sorted([(ciudad,number) for number,ciudad in c.items()], reverse=True) #Sort from highest to lowest according to number

c3 = c2[0:5] #We save the first 5 names

for x in c3: #Print only the names
    print(x[1])
    

