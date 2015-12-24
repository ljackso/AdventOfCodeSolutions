import util

def main():

	stringList = util.get_file_as_list_of_strings("Input/day_7_input.txt")
	
	for item in stringList:
		item = ''.join(item.split())

	print(len(stringList[0]))
	
	charList = list(stringList[0])

	charList[:] = [x for x in charList if x != ' ']
	l = 0;

	for c in charList:
		print c
		l += 1

	print l
	print(len(charList))


if __name__ == '__main__':
 	main()