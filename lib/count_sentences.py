#!/usr/bin/env python3

class MyString:
	def __init__(self, value = ""):
		self._value = value
    
	def get_value(self):
		return self._value

	def set_value(self, value):
		if isinstance(value, str):
			self._value = value
		else:
			print('The value must be a string.')
	
	value = property(get_value, set_value)

	def is_sentence(self):
		list_of_self = list(self._value)
		if list_of_self[-1] == ".":
			return True
		return False

	def is_question(self):
		list_of_self = list(self._value)
		if list_of_self[-1] == "?":
			return True
		return False
	
	def is_exclamation(self):
		list_of_self = list(self._value)
		if list_of_self[-1] == "!":
			return True
		return False
	
	def count_sentences(self):
		list_of_self = list(self._value)
		num_sentences = 0

		for index, character in enumerate(list_of_self):
			# print(character)
			if character == "!" or character == "?" or character == ".":
				num_sentences += 1
				if list_of_self[index - 1] == "." or list_of_self[index - 1] == "?" or list_of_self[index - 1] == "!":
					num_sentences -= 1

		return num_sentences
	
		