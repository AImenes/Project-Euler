// ipAdresses.cpp : Defines the entry point for the console application.
// Skrevet av Anders Imenes

//Bibliotek
#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#include "math.h"

//Definerer konstanter
#define adressLen 32

//IP-struct
struct myIP {
	unsigned int adr[4] = {0, 0, 0, 0};
	unsigned int prefix = 0; 
};
struct myIP adresse;
struct myIP submask;
struct myIP subnett;

//Parameterdeklarasjon
void dec();
void menu();
void display();
void bin();
void prefixCalc();
void waiter(int postponation);
void printBin();
void printDec();
void launch();
void reset();
void resetSub();
int convertBinaryToDecimal(long long n);
void printSubBin();
void printSubDec();
void printSubnetBin();
void printSubnetDec();
int checkAdrWithSubnet();
void subNett();

//Globale variabler
long long int antallKomb = pow(2, adressLen);


int main()
{
	launch();
	menu();
    return 0;
}

void bin() {
	long long n;
	int i;
	for (i = 0; i < 4;i++) {
		printf("Skriv inn det %i. leddet i 8-bit: ", i+1);
		scanf("%lld", &n);
		adresse.adr[i] = convertBinaryToDecimal(n);
	}
	subNett();

}

void dec() {
	int i, j;
	unsigned int temp = 0;
	for (i = 0; i < 4; i++) {
		printf("Skriv inn det %i. leddet\n", i+1);
		scanf("%u", &temp);
		while (temp > 255) {
			printf("Tallet er over 255. Tast inn det %i. leddet p\x86 nytt.\nSkriv inn: ", i+1);
			scanf("%u", &temp);
		}
		adresse.adr[i] = temp;
	}
	system("cls");
	printf("Adressen du har tastet inn er:\n%u.%u.%u.%u", adresse.adr[0], adresse.adr[1], adresse.adr[2], adresse.adr[3]);
	waiter(1200);
	subNett();
}

//Regner ut subnettet ved hjelp av IP adresse og masken.
void subNett() {
	int i;
	for (i = 0; i < 4; i++) {
		subnett.adr[i] = submask.adr[i] & adresse.adr[i];
	}
}

//Kalkuleter Submaske ved hjelp av prefixen
void prefixCalc() {
	resetSub();
	int temp, i, j;
	int antallHeleTall = 0;
	int resten = 0;
	printf("Skriv inn prefix i antall bits: ");
	scanf("%u", &temp);
	while (temp > adressLen) {
		printf("For mange bits, skriv inn ett tall under mellom 0 og 32. \nSkriv inn her: ");
		scanf("%u", &temp);
	}
	adresse.prefix = temp;
	antallHeleTall = temp / 8;
	resten = temp % 8;
		for (i = 0; i < antallHeleTall; i++) {
			submask.adr[i] = 255;
		}
		//submask.adr[antallHeleTall
		for (i = 0; i < resten; i++) {
			submask.adr[antallHeleTall] |= (1 << (7-i));
		}
		antallKomb = (pow(2,(adressLen - temp)))-2;
		subNett();
}

//Ventefunksjon
void waiter(int postponation) {
	int delay = clock();
	while (clock() < delay + postponation){}
}

//Gjør om fra binært til desimal
int convertBinaryToDecimal(long long n)
{
	int decimalNumber = 0, i = 0, remainder;
	while (n != 0)
	{
		remainder = n % 10;
		n /= 10;
		decimalNumber += remainder*pow(2, i);
		++i;
	}
	return decimalNumber;
}

//Output vinduet i programmet
void display() {
	int j;
	printf("------------------OUTPUT-vindu------------------\n");
	printf("\nAKTIV IP-ADRESSE \n");
	printf("Desimalform: ");printDec();
	printf("Binaryform:  ");printBin();
	printf("\n\n");
	printf("SUBMASKE\n");
	printf("Desimalform: ");printSubDec();
	printf("Binaryform:  ");printSubBin();
	printf("\n\nSUBNETT\n");
	printf("Desimalform: ");printSubnetDec();
	printf("Binaryform:  ");printSubnetBin();
	printf("\nTilgjengelige IP-adresser p\x86 subnettet: %lli", antallKomb);
	printf("\n\nPREFIX\n");
	printf("Desimalform: "); printf("%u\n", adresse.prefix);

	printf("Binaryform:  ");
		for (j = 7; j >= 0; j--) {
			if (adresse.prefix & (1 << j)) {
				printf("1");
			}
			else { printf("0"); }
		};

		if (checkAdrWithSubnet() == 1) {
			printf("\n\nIP-adressen matcher ikke subnettet.\n");
		}
		else {
			printf("\n\nIP-adressen er innenfor subnettet.\n");
		}
	printf("\n------------------------------------------------\n");

}

//Loading-skjermen i starten
void launch() {
	int t, loading = 0;
	t = clock();
	printf("\n\n\n                Velkommen til\n\n            IP-ADRESSE KALKULATOR\n\n              Av Anders Imenes\n\n\n\n\n");
	printf("Loading: |");waiter(400);
	for(t = 0; t<25;t++){
		printf("-");
		waiter(50);
	}
	printf("|");
	waiter(600);
}

//Resetter alle verdier til default
void reset() {
	for (int i = 0; i < 4; i++) {
		adresse.adr[i] = 0;
		submask.adr[i] = 0;
		subnett.adr[i] = 0;
	}
	adresse.prefix = 0;
	antallKomb = pow(2, adressLen);
}

//Resetter bare subnettet. Måtte opprettes hvis man ønsker å gå til en lavere prefix
void resetSub() {
	int i;
	for (i = 0; i < 4;i++)
	{
		submask.adr[i] = 0;
	}
}

//Menyen
void menu() {
	int run = 1, valg;
	while (run == 1) {
		system("cls");
		display();
		printf("\n\nValg(0) : Avslutt \nValg(1) : Skriv inn IP - adresse i binform\nValg(2) : Skriv inn IP - adresse i decform\nValg(3) : Skriv inn prefix\nValg(4) : Skriv inn ett subnett\nValg(5) : Er IP-en innenfor subnettet?\nValg(6) : Nullstill\n\nAngi menyvalg : ");
		scanf("%i", &valg);
		switch (valg)
		{
		case 0:
			run = 0;
			system("cls");
			printf("Takk for n\x86.\n");
			waiter(1500);
			system("cls");
			break;
		case 1:
			system("cls");
			bin();
			break;
		case 2:
			system("cls");
			dec();
			break;
		case 3:
			system("cls");
			prefixCalc();
			break;
		case 4:
			break;
		case 5:
			break;
		case 6:
			reset();
			break;
		default:
			printf("No galt skjedde.\n");
		}
	}
}

int checkAdrWithSubnet(){
	int i, j;
	int helTall = adresse.prefix / 8;
	int resten = adresse.prefix % 8;
	for (i = 0; i < helTall; i++) {
		for (j = 7; j >= 0; j--){
			if ((adresse.adr[i] & (1 << j)) == (subnett.adr[i] & (1 << j))){
				return 1;
			}
		}
	}
	for (i = 0; i < resten; i++) {
		if ((adresse.adr[helTall] & (1 << (7 - i))) == (subnett.adr[helTall] & (1 << (7 - i)))) {
			return 1;
		}
	}
	return 0;
}





void printBin() {
	int i, j;
	for (i = 0; i < 4; i++) {
		for (j = 7; j >= 0; j--) {
			if (adresse.adr[i] & (1 << j)) {
				printf("1");
			}
			else { printf("0"); }
		}
		printf(" ");
	}
}

void printDec() {
	for (int i = 0; i < 4;i++) {
		printf("%u", adresse.adr[i]);
		if (i < 3) { printf("."); }
	}
	printf("\n");
}

void printSubBin(){
	int i, j;
	for (i = 0; i < 4; i++) {
		for (j = 7; j >= 0; j--) {
			if (submask.adr[i] & (1 << j)) {
				printf("1");
			}
			else { printf("0"); }
		}
		printf(" ");
	}
}

void printSubDec(){
	for (int i = 0; i < 4;i++) {
		printf("%u", submask.adr[i]);
		if (i < 3) { printf("."); }
	}
	printf("\n");
}

void printSubnetBin(){
	int i, j;
	for (i = 0; i < 4; i++) {
		for (j = 7; j >= 0; j--) {
			if (subnett.adr[i] & (1 << j)) {
				printf("1");
			}
			else { printf("0"); }
		}
		printf(" ");
	}
}

void printSubnetDec(){
	for (int i = 0; i < 4;i++) {
		printf("%u", subnett.adr[i]);
		if (i < 3) { printf("."); }
	}
	printf("\n");
}