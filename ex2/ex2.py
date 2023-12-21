import sys


def get_lines(lines):
	for line in sys.stdin:
		lines.append(line.rstrip('\n'))
	return lines


def main():
	lines = []
	nb_pizzeria_and_livraison = []
	pizzeria = []
	pizzeria_split =[]
	livraison = []
	livraison_split = []
	get_lines(lines)
	total_distance = 0
	distance = 1000000000
	for line in lines:
		if len(nb_pizzeria_and_livraison) == 0:
			nb_pizzeria_and_livraison = line
			continue
		if len(pizzeria) < int(nb_pizzeria_and_livraison.split()[0]):
			pizzeria.append(line)
			continue
		livraison.append(line)
	for addresse in pizzeria:
		if len(addresse) == 1:
			pizzeria_split.append(int(addresse))
			continue
		for coord in addresse.split():
			pizzeria_split.append(int(coord))
	for addresse in livraison:
		if len(addresse) == 1:
			livraison_split.append(int(addresse))
			continue
		for coord in addresse.split():
			livraison_split.append(int(coord))
	for i in range(0, len(livraison_split), 2):
		distance = 1000000000
		for j in range(0, len(pizzeria_split), 2):
			calcul = abs(livraison_split[i] - pizzeria_split[j]) + abs(livraison_split[i + 1] - pizzeria_split[j + 1])

			if calcul < distance:
				distance = calcul
		total_distance += distance
	total_distance *= 2
	print(total_distance)


if __name__ == '__main__':
	main()
