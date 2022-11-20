w, h = 10, 16;
sequenceNumber = [[0 for x in range(w)] for y in range(h)] 

uniqueCode = [None] * 16;

for i in range(0,16):
	for j in range (0,10):
			sequenceNumber[i][j] = 1;



# print
for i in range(0,16):
	print(sequenceNumber[i]);


def remove(sequence, correct):
	currentSeq = str(sequence);

	if (correct == 0)
	for i in range(len(currentSeq)):
