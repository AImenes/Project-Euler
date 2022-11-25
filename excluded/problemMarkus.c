#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "time.h"

/*

		Et program skrevet av

				Hanne Korneliussen
				Benjamin Granum
				Markus Holmby
				Anders Imenes

			i tett samarbeid med

				Mass
				
*/


#define LIMIT 1000

void encrypt_decrypt(unsigned int key, char plain[], char cipher[]);

int main() {

	/* Inngangs- og utgangsarray */
	char input[LIMIT] = { 0 };
	char output[LIMIT] = { 0 };

	/* Henter inn melding, begrenset av LIMIT */
	printf("Skriv inn melding: ");
	fgets(input,LIMIT,stdin);

	/* Genererer startpunkt i seed, ved primtall * tidSekSiden010170 % primtall */
	int currentKey = (3497759 *(time(NULL))) % 15486047;

	/* Kjører funksjonen to ganger */
	encrypt_decrypt(currentKey, input, output);

	printf("Krypterte melding: %s \n", output);

	encrypt_decrypt(currentKey, output, input);
	printf("Dekryptert med samme nøkkel: %s", input);

	printf ("Hemmelig informasjon til Mass: Key - %i \n\n", currentKey);
	system("pause");

	return 0;
}

void encrypt_decrypt(unsigned int key, char plain[], char cipher[]) {

	/* Use the key as seed for the random function */
	srand(key);

	/* Get length of plaintext */
	int len = strlen(plain);

	/* For each byte in the plaintext */
	int i;
	for (i = 0; i < len; i++) {

		/* Obtain a random byte to use as pad */
		unsigned char pad = (unsigned char)rand();

		/* Encrypt a byte by XORing it with the pad */
		cipher[i] = plain[i] ^ pad;
	}
}

/*
		Oppgave 1a)
		Check

		Oppgave 1b)
		Det er fordi at krypteringsmetoden benytter den bitvise operatoren XOR.
		Denne har som egenskap fordi at 
				((X XOR K) XOR K)
			Som er det samme som
				(X XOR (K XOR K))
			Som igjen er det samme
				X XOR 0
			Som er lik
				X
				;)

		Oppgave 1c)
			Fordi den pseudorandom! Det er fordi at den ikke helt tilfeldig,
			da samme inngangsverdi alltid vil gi samme tallfølje. Et godt 
			alternativ er å la seedverdien eksempelvis være definert av tiden
			fra 1. Januar 1970 (i sek (time-funksjonen)), slik at seeden blir ulik
			hver gang programmet kjøres.

		Oppgave 1d)
			Den er sårbar mot bruteforce fordi vi ikke har en helt tilfeldig
			nøkkel. Den er pseudorandom. 

			En annen svakhet er at hvis vi har to meldinger som er kryptert med samme nøkkel,
			vil vi være i stand til å få ut begge meldingene i klartekst (ved å XORe de to 
			meldingene). Dette er fordi K XOR K = 0.

		Oppgave 1e)
			Som beskrevet i oppg 1c, kan vi variere srand hver gang vi kjører. Vi
			valgte å bruke tidsfunksjonen, som gir oss antall sek siden 1. Januar 1970. 
			For å få denne enda mer tilfeldig, valgte vi å fjerne inkrementeringen i sekunder, 
			ved å bruke modlos av et stort primtall.

*/
