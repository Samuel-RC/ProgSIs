#include <iostream>
using namespace std;

int buscador(int num[],int n, int b){
	if(n==0){
		if(num[n]==b){
			return 1;
		}else{
			return 0;
		}	
	}else{
		if(num[n]==b){
			return 1 + buscador(num,n-1,b);
		}else{
			return 0 + buscador(num,n-1,b);
		}
	}
}
int main(int argc, char *argv[]) {
	int n;
	int b;
	cout<<"De cuantos espacios va a ser tu arreglo"<<endl;
	cin>>n;
	int* arreglo = new int[n];
	for(int i=0; i<n;i++){
		cout<<"Dame el valor de la posicion "<<i+1<<endl;
		cin>>arreglo[i];
	}
	cout<<"¿Que numero vas a buscar?"<<endl;
	cin>>b;
	int k=buscador(arreglo,n-1,b);
	cout<<"El número "<<b<<" se encuentra "<<k<<" veces en tu arreglo"<<endl;
	return 0;
}
