#include <iostream>
using namespace std;
int buscador(int num[],int n, int b, int n1){
	if(n==n1-1){
		if(num[n]==b){
			return n;
		}else{
			return -1;
		}
	}else{
		if(num[n]==b){
			return n;
		}
		return buscador(num,n+1,b,n1);
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
	int k=buscador(arreglo,0,b,n);
	cout<<k;
	if(k>=0){
		cout<<"Tu numero si se encuentra y lo puedes encontrar en la posicion "<<k<<endl;
	}else{
		cout<<"Tu numero no se encuentra en el arreglo"<<endl;
	}
	
	
}

