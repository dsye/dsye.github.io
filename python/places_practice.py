#Creates full sentence based on places I want to visit.
places= ["Vienna", "Galapagos Islands", "Utah", "Colorado"]
statement=[]
#each element is called city, even though only one is an actual city
for city in places:
    statement.append("I would like to visit " + city + ".")
#prints out sentence
print(statement)
