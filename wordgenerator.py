import random
import string 

def process_file(str):
	#open desired file
	f = open(str)
	#read it in, lower case
	text = f.read().lower()
	f.close()
	text=text.split()
	return text

def markov_dictionary(text):
	text = process_file(text)
	index = 0
	markov_dict = {}
	if len(text) == 0:
		return markov_dict
	while index < len(text)-1: #the index must be less than the length of text to make while loop activate
	 	if index <= 1:
	 		#key = "%s %s" %(text[0], text[1])
	 		markov_dict[(text[0], text[1])] = [text[2]]
	 		index  += 1
		# elif text[-1] ==".":
		#  		return markov_dict
	 	elif index >1:
	 	 	#key = "%s %s" %(text[index-1], text[index])
	 	 	if markov_dict.get((text[index-1], text[index])): #markov_dict[key] == None:
	 	 		markov_dict[(text[index-1], text[index])].append(text[index+1])
	 	 		index +=1

	 		else:
	 			markov_dict[(text[index-1], text[index])] = [(text[index+1])]
	 			index += 1	
	 			
	
	return markov_dict

def print_markov(text):
	text_split = process_file(text)
	markov_dict = markov_dictionary(text)
	# Start with a random pair 
	rand_num=random.randrange(1,len(text)-1) 

	#rand_num=0
	start_key=text_split[rand_num] 
	end_key= text_split[(rand_num)+1]

	foo=True
	new_list = [ ]
	new_list.append(start_key)
	new_list.append(end_key)#new_list= [ "Hello", "World"] as a starting point 
	i=0 
	desired_value =" "
	while desired_value[-1] !=".":
		t = (new_list[i], new_list[i+1])
		desired_value = markov_dict[t]
		 #this makes the while loop stop when there's a  #period at the end of a word
		i+=1
		if len(desired_value)>1: #choose the random value inside the list of values
			random_number = random.randrange(0,len(desired_value))
			new_list.append(desired_value[random_number])
			
		else: # when there's only 1 element in the values list 
			desired_value = desired_value[0]
			new_list.append(desired_value)
	

	#stringifying process is here!
	new_string= "" 
	for i in new_list: 
		new_string = new_string + i + " "
		new_string= new_string.capitalize()
	print new_string

	# #This is an alternative stringifying, capitalize-only-first-letter-in-sentence process
	# new_list = " ".join(new_list)
	# print new_list
	# first_char = new_list[0].capitalize()
	# new_list=new_list.replace(new_list[0], first_char,1)
	# print new_list
	# return new_list

def print_num_sentences(sample_text): 
	num_sentences=int(raw_input("Type in # of sentences:"))
	# print num_sentences
	# print type(num_sentences)
	i=0
	while i<num_sentences: 
		print_markov(sample_text) 
		i+=1	

print_num_sentences("sample4.txt")		
# print_markov("sample5.txt")	
# print_markov("emma.txt")

	
