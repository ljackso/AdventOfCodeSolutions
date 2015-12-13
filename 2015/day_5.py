'''
------------------------------------------------------------------------------------------------
	DAY FIVE 
------------------------------------------------------------------------------------------------
	
PROBLEM:

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

- It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.

- It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd 
(aa, bb, cc, or dd).

- It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other 
requirements.

For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), 
and none of the disallowed substrings.

aaa is nice because it has at least three vowels and a double letter, even though the letters 
used by different rules overlap.

jchzalrnumimnmhp is naughty because it has no double letter.

haegwjzuvuyypxyu is naughty because it contains the string xy.

dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice? (from the input file )
------------------------------------------------------------------------------------------------

SOLUTION:

'''

import util

naughty_strings = ["ab", "cd", "pq", "xy"]
vowels = ['a','e', 'i', 'o', 'u']

def main():
	words = util.get_file_as_list_of_strings('Input/day_5_input.txt')
	nice_words = 0

	for word in words:
		if (is_nice_word(word)):
			nice_words += 1

	print("Number of nice words : " + nice_words)

def is_nice_word(word):
	global naughty_strings
	global vowels

	word_as_list = list(word)
	contains_pair = False
	for i in range(0, len(word_as_list) -1):
			pair = (word_as_list[i] + word_as_list[i+1])

			if pair in naughty_strings:
				return False 

			if word_as_list[i] == word_as_list[i+1]:
				contains_pair = True

	vowel_count = 0;
	for c in word_as_list:
		if c in vowels:
			vowel_count += 1

	return (contains_pair and (vowel_count >= 3)) 

if __name__ == '__main__':
	main()




