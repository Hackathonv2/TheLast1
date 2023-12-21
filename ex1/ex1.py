import sys


def get_lines(lines):
	for line in sys.stdin:
		lines.append(line.rstrip('\n'))
	return lines


if __name__ == '__main__':
	lines = []
	ingredients = []
	already = []
	nb_ingredient = 0
	get_lines(lines)
	for line in lines:
		if len(line.split()) == 1:
			ingredients.append(line)
			continue
		line = line.split()
		for ingredient in line:
			ingredients.append(ingredient)
	ingredients.pop(0)
	for ingredient in ingredients:
		if ingredient in already:
			continue
		already.append(ingredient)
		nb_ingredient += 1
	print(nb_ingredient)
