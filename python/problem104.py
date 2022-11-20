def fib(n):
	arr = [None] * (3);
	arr[1] = 1;
	arr[2] = 1;
	found = False;
	count = 3;

	while (found == False):
		arr[0] = arr[1] + arr[2];
		#print(arr[0]);
		lengthNum = len(str(arr[0]));
		if lengthNum > 17:
			startSection = str(arr[0])[:9];
			endingSection = str(arr[0])[-9:];
			if ((("1") in startSection) and (("2") in startSection) and (("3") in startSection) and (("4") in startSection) and (("5") in startSection) and (("6") in startSection) and (("7") in startSection) and (("8") in startSection) and (("9") in startSection)):
				if ((("1") in endingSection) and (("2") in endingSection) and (("3") in endingSection) and (("4") in endingSection) and (("5") in endingSection) and (("6") in endingSection) and (("7") in endingSection) and (("8") in endingSection) and (("9") in endingSection)):
					print(arr[0],count);
					found = True;
					
		arr[2] = arr[1];
		arr[1] = arr[0];
		count += 1;

	return 0;



fib(10);