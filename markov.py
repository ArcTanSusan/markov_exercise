"""
markov.py

Reference text: section 13.8, how to think like a computer scientist

Do markov analysis of a text and produce mimic text based off the original.

Markov analysis consists of taking a text, and producing a mapping of prefixes to suffixes. 
A prefix consists of one or more words, and the next word to follow the prefix in the text. Note, a prefix can have more than one suffix.

Eg: markov analysis with a prefix length of '1'

    Original text:
        "The quick brown fox jumped over the lazy dog"

        "the": ["quick", "lazy"]
        "quick": ["brown"]
        "brown": ["fox"]
        "fox": ["jumped"]
        ... etc.

With this, you can reassemble a random text similar to the original style by choosing a random prefix and one of its suffixes, 
then using that suffix as a prefix and repeating the process.

You will write a program that performs markov analysis on a text file, then produce random text from the analysis. 
The length of the markov prefixes will be adjustable, as will the length of the output produced.
""" 
def main (): 
	text = process_file("sample.txt")
	new_dict=making_dictionary(text)



if __name__ == "__main__":
	main()

def process_file(str):
	f = open(str)
	text = f.readline()
	f.close()
	text=text.split()
	markov_dictionary = markov_dict(text)
	return markov_dictionary

def markov_dict(text):
	index = 0
	markov_dict = {}
	if len(text) == 0:
		return markov_dict
	for word in text:
	 	if index <= 1:
	 		#key = "%s %s" %(text[0], text[1])
	 		markov_dict[(text[0], text[1])] = [text[2]]
	 		index  += 1
		elif word[-1] ==".":
		 		return markov_dict
	 	elif index >1 :
	 	 	#key = "%s %s" %(text[index-1], text[index])
	 	 	if markov_dict.get(text[index-1], text[index]): #markov_dict[key] == None:
	 	 		markov_dict[text[index-1], text[index]].append(text[index+1])
	 	 		index +=1
	 		else:
	 			markov_dict[text[index-1], text[index]] = [text[index+1]]
	 			index += 1	
	return markov_dict 

