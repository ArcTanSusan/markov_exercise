import random
import string 

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

def markov_dictionary(text, ngram):
	text = process_file(text)
	#print type(text)
	#print len(text)
	#index = ngram
	index = 0
	markov_dict = {}
	ngram = int(ngram)
	# while count <= ngram:
	# 	key +=text[count]
	key = []
	key_index = 0

	while index <(len(text)):
		#index= ngram-index
		index -= ngram 
		while key_index < ngram: # Placing every character from sample text into the string "key". 
			key.append(text[index]) #+" "+ str(text[index])
			key_index +=1
			index += 1
		key = " ".join(key)
	 	if markov_dict.get(key): #markov_dict[key] == None:
 	 		markov_dict[key].append(text[index])
 	 		index +=1
 	 		key_index = 0
 	 		key =[]
	 	else:
 			markov_dict[key] = [(text[index])] #Values have to  be in a list! There can be more than 1 value in a key! Tuples or strings won't work 
 			index += 1
 			key_index = 0
 	 		key = [] 


# 1. Produce the n-keys in the dictionary. Fill up dictionary with unique n-keys. 
# 2. Stop producing keys when you run out of text. Use while loop. 
# 3. Print_markov: Access the dictionary to pull out the associated values for each key. 
		
	# if len(text) == 0:
	# 	return markov_dict
	# while index < len(text)-1: #the index must be less than the length of text to make while loop activate
	#  	if index <= ngram:
	#  		markov_dict[(text[0], text[1])] = [text[2]]
	#  		index  += 1
	#  	elif index >ngram:
	#  	 	if markov_dict.get((text[index-1], text[index])): #markov_dict[key] == None:
	#  	 		markov_dict[(text[index-1], text[index])].append(text[index+1])
	#  	 		index +=1
	#  		else:
	#  			markov_dict[(text[index-1], text[index])] = [(text[index+1])]
	#  			index += 1	
	 			
	#print markov_dict
	#print len(text)
	return markov_dict

#markov_dictionary("sample5.txt",6)
#markov_dictionary("emma.txt",5)
#markov_dictionary("emma.txt",10)

def print_markov(text, ngram):
	text_split = process_file(text)
	#print len(text_split)
	markov_dict = markov_dictionary(text, ngram)
	keys = markov_dict.keys()
	key = random.choice(keys)
	val = random.choice(markov_dict[key])

	keywords = key.split()

	new_list = [ ]
	new_list.extend(keywords)
	new_list.append(val)
	#print new_list
	last_word = val

	while last_word[-1] not in '?.!': #"?.!": #this makes the while loop stop when there's a  #period at the end of a word
		# ( w1 ... wn ) -> w( n+ 1)
		# ( w2 .... wn + 1)

		keywords = keywords[1:]
		keywords.append(last_word)
		new_val = markov_dict[" ".join(keywords)]
		last_word = random.choice(new_val)
		new_list.append(last_word)

	#  Non-functional alternative	
	#if len(new_list) <= 1:
	# 		desired_value = markov_dict[key]#desired_value=markov_dict.get(key) #
	# 		desired_value = random.choice(desired_value)
	# 	# t = (new_list[i], new_list[i+1])
	# 	t = new_list[i]  # t contains key. t is a string
	# 	t = t.split()	# split the key into a list. t is now list.
	# 	t = t[1:]
	# 	str([desired_value])
	# 	if desired_value[-1] == ".":
	# 		foo = False  	# take all elements in the key list, skipping the zeroth element. Still a list.
	# 	t.append(desired_value) # append desired value to the key list { [b,c, "boo"]}. t now contains updated key. Still a list.
	# 	t = " ".join(t) #t=str(t) #t= t + " " #t = " ".join(t). t has to become a string. 
	# 	new_list.append(t)
	# 	desired_value = markov_dict[t]
	# 	#print type(desired_value)
	# 	i+=1
	# 	if len(desired_value)>1: #choose the random value inside the list of values
	# 		number = random.randrange(0,len(desired_value))
	# 		desired_value =desired_value[number]
	# 		#new_list.append(desired_value)	
	# 	else: # when there's only 1 element in the values list 
	# 		desired_value = desired_value[0]
	# 		#new_list.append(desired_value)
	# #stringifying process is here!

	new_list = " ".join(new_list)
	#print new_list
	first_char = new_list[0].capitalize()
	#print type(first_char)
	#print first_char
	new_list=new_list.replace(new_list[0], first_char,1)
	#print new_list
	return new_list

#print_markov("emma.txt", 3)

def print_twitter(sample_text, num_sentences, ngram): 
	#num_sentences= 2
	 #int(raw_input("Type in # of sentences:"))
	# print num_sentences
	# print type(num_sentences)
	i=0
	sentences= " "
	char_count=0 

	while i<num_sentences: 
		sentences+=print_markov(sample_text,ngram) 
		i+=1	
	# print sentences
	num_chars =0
	for chars in sentences:
		num_chars +=1
	#print num_chars
	if num_chars > 140:
		print_twitter(sample_text, 1, ngram)
	else:
		print sentences
		return sentences

#print_twitter("emma.txt",2, 3)		
# print_markov("sample5.txt")	
#print_twitter("emma.txt", 3)