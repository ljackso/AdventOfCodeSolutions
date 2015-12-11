
'''
------------------------------------------------------------------------------------------------
	DAY TWO 
------------------------------------------------------------------------------------------------
	
PROBLEM:

The elves are running low on wrapping paper, and so they need to submit an order for more. They 
have a list of the dimensions (length l, width w, and height h) of each present, and only want 
to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating 
the required wrapping paper for each gift a little easier: find the surface area of the box,
which is 2*l*w + 2*w*h + 2*h*l. 

The elves also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper,
    plus 6 square feet of slack, for a total of 58 square feet.

    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper,
    plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

------------------------------------------------------------------------------------------------

SOLUTION:

'''

def main():
	print (GetTotalWrappingPaper(ParseStringListIntoDataList(GetInputAsStringList())))

def GetInputAsStringList():

	with open('Input/DayTwoInput') as f:
		content = f.readlines()

	return content

#returns list of [l,w,h] to be counted
def ParseStringListIntoDataList(stringList):
	
	newDataList = []

	for string in stringList:
		cleanString = string.replace("\n","")
		cleanList = cleanString.split("x")
		numList= []
		for item in cleanList:
			numList.append(int(item))

		newDataList.append(numList)

	return newDataList



def GetTotalWrappingPaper(dimensionsList):

	totalPaper = 0;

	for dimensions in dimensionsList:
		totalPaper += GetWrappingPaperNeedForIndividualPresent(dimensions[0], dimensions[1], dimensions[2])

	return(totalPaper)



def GetWrappingPaperNeedForIndividualPresent(length, width, height):

	side1 = (length * width)
	side2 = (height * width)
	side3 = (length * height)

	coverNeeded = (2 * side1) + (2 * side2) + (2 * side3)
	slackNeeded = min(float(s) for s in [side1, side2, side3])

	return (coverNeeded + slackNeeded)


if __name__ == '__main__':
	main()
