#include <iostream>
using namespace std;
void imprimir(int n, int x){
	if(n==x){
		cout<<n<<" ";
	}else{
		cout<<n<<" ";
		imprimir(n+1,x);
	}
}

int main(int argc, char *argv[]) {
	int n=0;
	cout<<"Hasta que número quieres imprimir (de 1 a n)"<<endl;
	cin>>n;
	imprimir(1,n);
	cout<<endl;
	return 0;
}

