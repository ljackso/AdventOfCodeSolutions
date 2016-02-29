'''
------------------------------------------------------------------------------------------------
	DAY FOUR
------------------------------------------------------------------------------------------------
	
PROBLEM:
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all 
the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. 
The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number 
in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 
	1, 2, 3, ...) that produces such a hash.

For example:

    - If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 
      starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.

    - If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash 
      starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 
      000006136ef....

Your puzzle input is yzbqklnj.

------------------------------------------------------------------------------------------------

SOLUTION:

'''


import md5

def main():

	input_string = "yzbqklnj"

	number_key = 0
	string_key = input_string + str(number_key)

	hashed_string = md5.new()
	hashed_string.update(string_key)

	while(starts_with_zeros(hashed_string.hexdigest(), 6) == False):
		
		number_key += 1
		string_key = input_string + str(number_key)

		hashed_string  = md5.new()
		hashed_string.update(string_key)


	print(str(number_key))



def starts_with_zeros(input_string, num_zeros):
	char_list = list(input_string)

	for i in range(0, num_zeros):
		if(char_list[i] != '0'):
			return False

	return True


if __name__ == '__main__':
	main()