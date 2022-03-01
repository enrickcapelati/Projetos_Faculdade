#include <iostream>
#include <string.h>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>


typedef struct carro

{

int cod;

char marca [20];

char modelo [20];

int ano;

char placa[10];

}carro;

carro car[10];

void menu();

void inicializar();

void imprimir();

void cadastrar();

int main(int argc, char** argv) {

setlocale(LC_ALL,"portuguese");

int i;

int op;

int ano;

int z;

char modelo[20];

z=0;

ano=0;

i=0;

car[i].cod = 0;

strcpy(car[i].marca,"NULL");

strcpy(car[i].modelo,"NULL");

strcpy(car[i].placa,"NULL");

car[i].ano = 0;

do
{

printf("\n Opções:");

printf("\n 1. CADASTRAR VEÍCULO");

printf("\n 2. LISTAR VEÍCULOS");

printf("\n 3. PESQUISAR UM MODELO");

printf("\n 4. MOSTRAR VEÍCULOS A PARTIR DE UM ANO");

printf("\n 5. SAIR");

printf("\n \n DIGITE A OPÇÃO: ");

scanf("%d",&op);

switch(op)

{

case 1:

if (car[i].cod<=9)

{

car[i].cod=i;

printf("\n Digite a marca do veículo:");

scanf("%s",&car[i].marca);

printf("\n Digite o modelo do veículo:");

scanf("%s",&car[i].modelo);

printf("\n Digite a placa do veículo:");

scanf("%s",&car[i].placa);

printf("\n Digite o ano do veículo:");

scanf("%d",&car[i].ano);

i=i+1;



}



else



{

printf("\n Limite de cadastro é 10!");

}



break;



case 2:

for(int x=0; x<i; x++)



{

printf("\n A marca do veículo é: %s",car[x].marca);

printf("\n O modelo do veículo é: %s",car[x].modelo);

printf("\n O ano do veículo é: %d",car[x].ano);

printf("\n A placa do veículo é: %s",car[x].placa);

printf("\n\n =================================== \n \n");

}



break;



case 3:

printf("\n INSIRA O MODELO A SER PESQUISADO:");

scanf("%s",&modelo);

for (int x=0; x<i; x++)



{

if (strcmp(car[x].modelo,strlwr(modelo)) == 0)

{

printf("\n A marca do veículo é: %s",car[x].marca);

printf("\n O modelo do veículo é: %s",car[x].modelo);

printf("\n O ano do veículo é: %d",car[x].ano);

printf("\n A placa do veículo é: %s",car[x].placa);

printf("\n\n =================================== \n \n");



z++;

}



}



if (z==0)



{

printf("\n NÃO FOI ENCONTRADO O MODELO %s \n\n",modelo);

}



else



{

z=0;

}



break;



case 4:

printf("\n INSIRA O ANO A SER PESQUISADO:");

scanf("%d",&ano);



for (int x=0; x<i; x++)

{

if (car[x].ano >= ano)



{

printf("\n A marca do veículo é: %s",car[x].marca);

printf("\n O modelo do veículo é: %s",car[x].modelo);

printf("\n O ano do veículo é: %d",car[x].ano);

printf("\n A placa do veículo é: %s",car[x].placa);

printf("\n\n =================================== \n \n");



z++;

}

}



if (z==0)

{

printf("\n NÃO FOI ENCONTRADO VEÍCULOS ACIMA DE %d \n\n",ano);

}

else


{

z=0;

}

break;

default:

printf("\n Opção não existe");



break;
}

}

while (op!=5 && i<=9);

if (i==9)

{

printf("\n \n LIMITE DE VEÍCULOS ALCANÇADO! \n \n \n");

}

for (int y=0; y<i; y++)

{

printf("\n A marca do veículo é: %s",car[y].marca);

printf("\n O modelo do veículo é: %s",car[y].modelo);

printf("\n O ano do veículo é: %d",car[y].ano);

printf("\n A placa do veículo é: %s",car[y].placa);

printf("\n\n =================================== \n \n");

}

return 0;

}
