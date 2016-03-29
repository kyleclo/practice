#include <iostream>

using namespace std;

void InsertionSort(int x[], int n);
void PrintArray(int x[], int n);



int main(){

	int n = 6;
	int x[] = {2, 5, 3, 6, 1, 4};

	InsertionSort(x, n);
	PrintArray(x, n);

	return 0;
}


void InsertionSort(int x[], int n){

	for(int i = 1; i < n; i++){

		int candidate = x[i];
		int j = i - 1;

		while(j >= 0 && x[j] > candidate){
			x[j + 1] = x[j];
			j--;
		}

		x[j + 1] = candidate;
	}

}


void PrintArray(int x[], int n){

	for(int i = 0; i < n; i++){
		cout << x[i] << " ";
	}
}
