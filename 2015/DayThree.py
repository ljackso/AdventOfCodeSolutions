
import copy

currentX = 0
currentY = 0
vistiedPoints = []

def main():

	consumeInstructions(getListOfInstructions())
	print(len(vistiedPoints))

def getListOfInstructions():

	with open('Input/DayThreeInput') as f:
		content = f.read()
	
	return content 
	
def consumeInstructions(instructionList):

	currentPoint = [currentX, currentY]

	if currentPoint not in vistiedPoints:
		vistiedPoints.append(currentPoint)

	for instruction in instructionList :
		consumeInstruction(instruction)

def consumeInstruction(direction):
	global currentX
	global currentY

	if (direction == '>'):
		currentX += 1
	elif (direction == '<'):
		currentX -= 1
	elif (direction == '^'):
		currentY += 1
	elif (direction == 'v'):
		currentY -= 1

	newPoint = [currentX, currentY]

	if newPoint not in vistiedPoints:
		vistiedPoints.append(newPoint)


if __name__ == '__main__':
	main()