import re

streng = "192.168.0.1"
valid = re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}');
ipAttempt = valid.findall(streng);

print(ipAttempt[2]);

for i in range(0,4):
	if (ipAttempt[i] > 255):
			print("Tallet er for stort")

print(ipAttempt);




