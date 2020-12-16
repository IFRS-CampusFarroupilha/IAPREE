from data.student import getDataset
import colorama

def main():
	colorama.init()

	print(colorama.Fore.BLUE + getDataset())

if __name__ == "__main__":
	main()