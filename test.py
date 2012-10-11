my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
	print "Key == %r, value == %r"  % (key, value)

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}


states.get("Oregon")
print states
print states.get("Mars",1)

# states.setdefault("Oregon", 1)
# print states
# a = ["cat", "dog", "rat"]
# for animal in a:
# 	states.setdefault(animal,1)
	
# states.setdefault("Venus", "llalalala")
# print states 

# states.setdefault("Venus",1)
# print states


# # create a basic set of states and some cities in them
# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'
# }

# # add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'

# print out some cities
# print '-' * 10
# print "NY State has: ", cities['NY']
# print "OR State has: ", cities['OR']

# # print some states
# print '-' * 10
# print "Michigan's abbreviation is: ", states['Michigan']
# print "Florida's abbreviation is: ", states['Florida']

# # do it by using the state then cities dict
# print '-' * 10
# print "Michigan has: ", cities[states['Michigan']]
# print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
# print '-' * 10
# for state, abbrev in states.items():
#     print "%s is abbreviated %s" % (state, abbrev)

# # print every city in state
# print '-' * 10
# for abbrev, city in cities.items():
#     print "%s has the city %s" % (abbrev, city)

# # now do both at the same time
# print '-' * 10
# for state, abbrev in states.items():
#     print "%s state is abbreviated %s and has city %s" % (
#         state, abbrev, cities[abbrev])

# print '-' * 10
# # safely get a abbreviation by state that might not be there
# state = states.get('Texas', None)

# if not state:
#     print "Sorry, no Texas."

# # get a city with a default value
# city = cities.get('TX', 'Does Not Exist')
# print "The city for the state 'TX' is: %s" % city

# phonebook = {}
# phonebook["John"] = 938477566
# phonebook["Jack"] = 938377264
# phonebook["Jill"] = 947662781

# for name, number in phonebook.iteritems():
#     print "Phone number of %s is %d" % (name, number)

# #phonebook.pop("John")
# del phonebook["John"]
# print phonebook