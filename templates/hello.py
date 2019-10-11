def square(x):
	return x * x

def main(num):
	for num in range(10):
		print( "The square of {} is {}".format( num, square(num)))


if __name__ == "__main__":
	main()
