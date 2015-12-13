'''
------------------------------------------------------------------------------------------------
	DAY SIX
------------------------------------------------------------------------------------------------
	
PROBLEM:

Because your neighbors keep defeating you in the holiday house decorating contest year after year, 
you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions 
on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are 
at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle 
various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite 
corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 
lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the 
instructions Santa sent you in order.

For example:

- turn on 0,0 through 999,999 would turn on (or leave on) every light.

- toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, 
and turning on the ones that were off.

- turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

------------------------------------------------------------------------------------------------

SOLUTION:

'''
import util

ON = True
OFF = False

Instructions = util.enum(TOGGLE = 0, ON = 1, OFF = 2)
roof_lights = []

def main():
	global roof_lights

	roof_lights = [[True for l in range(0,1000)] for j in range(0, 1000)]

	string_list_instructions = util.get_file_as_list_of_strings('Input/day_6_input.txt') 

	for string_instruction in string_list_instructions:
		consume_string_instruction(string_instruction)

	lights_on_count = 0
	for l in range(0, 1000):
		for j in range(0, 1000):
			if (roof_lights[l][j]):
				lights_on_count += 1

	print ("Number of Lights On : " + str(lights_on_count))
	
def consume_string_instruction(instruction):

	words = instruction.split(" ")

	if (words[0] == "toggle"):
		instr_type = Instructions.TOGGLE

		start_point_strings = words[1].split(",")
		start_point = (int(start_point_strings[0]), int(start_point_strings[1]))

		end_point_strings = words[3].split(",")
		end_point = (int(end_point_strings[0]), int(end_point_strings[1]))

	else:
		if (words[1] == "off"):
			instr_type = Instructions.OFF
		elif (words[1] == "on"):
			instr_type = Instructions.ON

		start_point_strings = words[2].split(",")
		start_point = (int(start_point_strings[0]), int(start_point_strings[1]))

		end_point_strings = words[4].split(",")
		end_point = (int(end_point_strings[0]), int(end_point_strings[1]))

	consume_instruction(instr_type, start_point, end_point)


def consume_instruction(instr_type, start_point, end_point):
	global ON
	global OFF
	global roof_lights

	affected_points = get_points_in_square(start_point, end_point)

	for point in affected_points:
		x = point[0]
		y = point[1]

		if(instr_type == Instructions.TOGGLE):
			if(roof_lights[x][y] == ON):
				roof_lights[x][y] = OFF
			else:
				roof_lights[x][y] = ON

		elif(instr_type == Instructions.ON):
			roof_lights[x][y] = ON

		elif(instr_type == Instructions.OFF):
			roof_lights[x][y] = OFF

#returns list of points in square 
def get_points_in_square(start_point, end_point):
	
	start_point_x = start_point[0]
	start_point_y = start_point[1]

	end_point_x = end_point[0]
	end_point_y = end_point[1]

	point_list = [] 

	for x in range(start_point_x, 1 + end_point_x):
		for y in range(start_point_y, 1 +  end_point_y):
			point_list.append((x,y))

	return point_list


if __name__ == '__main__':
	main()