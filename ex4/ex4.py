import sys


def get_lines(lines):
	for line in sys.stdin:
		lines = line.rstrip('\n')
	return lines


def main():
	chifumi = []
	chifumi = get_lines(chifumi)
	new_chifumi = ()
	while len(chifumi) > 1:
		if chifumi[0] == 'P' and chifumi[1] == 'F':
			new_chifumi = chifumi[1:]
			chifumi = new_chifumi
			continue
		if chifumi[0] == 'F' and chifumi[1] == 'C':
			new_chifumi = chifumi[1:]
			chifumi = new_chifumi
			continue
		if chifumi[0] == 'C' and chifumi[1] == 'P':
			new_chifumi = chifumi[1:]
			chifumi = new_chifumi
			continue
		new_chifumi = chifumi[:1] + chifumi[2:]
		chifumi = new_chifumi
	print(chifumi)


if __name__ == '__main__':
	main()
