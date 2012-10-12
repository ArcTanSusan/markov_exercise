import random
import string 
import twitter

def process_file(str):
	#open desired file
	f = open(str)
	#read it in, lower case
	text = f.read() #.lower()
	f.close()
	text=text.split()
	#print len(text)
	return text

#process_file("emma.txt")

def markov_dictionary(text):
	text = process_file(text)
	#print len(text)
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
	 			
	#print markov_dict
	#print len(text)
	return markov_dict

#markov_dictionary("emma.txt")

def print_markov(text):
	text_split = process_file(text)
	markov_dict = markov_dictionary(text)
	# Start with a random pair 

	rand_num=random.randrange(1,(len(text_split)-1)) 
	start_key=text_split[rand_num] 
	end_key= text_split[(rand_num)+1]

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
	new_list = " ".join(new_list)
	print new_list
	first_char = new_list[0].capitalize()
	#print type(first_char)
	#print first_char
	new_list=new_list.replace(new_list[0], first_char,1)
	print new_list
	# for i in new_list: 
	# 	new_string = new_string + i + " "
	#new_list = new_list[0].capitalize()
		#new_string= new_string.capitalize()
	return new_list

print_markov("emma.txt")

def print_twitter(sample_text, num_sentences): 
	#num_sentences= 2
	 #int(raw_input("Type in # of sentences:"))
	# print num_sentences
	# print type(num_sentences)
	i=0
	sentences= " "
	char_count=0 

	# while char_count<140: 
	while i<num_sentences: 
		sentences+=print_markov(sample_text) 
		i+=1	
	# print sentences
	num_chars =0
	for chars in sentences:
		num_chars +=1
	print num_chars
	if num_chars > 140:
		print_twitter(sample_text, 1)
	else:
		print sentences

#print_twitter("sample4.txt",10)		
# print_markov("sample5.txt")	
print_twitter("emma.txt", 3)
