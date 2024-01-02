
def is_end(c):
	return c == '.' or c == '!' or c == '?'

def is_quote(c):
	return c == "\"" or c == "\'" 

def closing_quote(s, i):
	if i >= len(s):
		return False
	elif is_quote(s[i]):
		j = i + 1
		while True:
			if s[j+1].isalpha():
				if s[j+1].islower():
					return False
				else:
					return True
			else:
				j += 1
	else:
		return False	

def get_sentences(s):
	sentences = []
	current_sentence_start = 0
	last_word_upper = False
	inside_quotes = False
	i = 0
	while i < len(s):
		if is_end(s[i]) and not last_word_upper and not inside_quotes:
			sentences.append(s[current_sentence_start:i + 1].strip())
			current_sentence_start = i + 1
		elif is_quote(s[i]) and inside_quotes:
			inside_quotes = False 
		elif is_quote(s[i]) and not inside_quotes and s[i + 1] != 's':
			inside_quotes = True
		elif is_end(s[i]) and not last_word_upper and inside_quotes and closing_quote(s, i + 1):
			sentences.append(s[current_sentence_start:i + 2].strip())
			current_sentence_start = i + 2
			i += 1
			inside_quotes = False 
		i += 1
	return sentences

s = input()
print("\n".join(get_sentences(s)))
