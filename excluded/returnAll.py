def isNumInAll(list):
	inAll = []

	#Går gjennom de alle tallene i første linje
	for x in range(len(list[0])):

		#nullstiller teller
		counter = 0;

		#går gjennom hver liste i listen
		for y in range(len(list)):

			#sjekker om verdien i første liste eksisterer i hver eneste liste videre
			if (list[0][x] in list[y]):
				counter += 1;

		#sjekker om tellern er like stor som antall lister, hvis ja, legges til i resultarray
		if (counter == len(list)):
			inAll.append(numberArray[0][x]);

	#return resultatArray
	return inAll;


numberArray = [[1,2,3,4,5],[9,8,7,6,5],[10,2,4,1,5]];
result = isNumInAll(numberArray);
print(result);

