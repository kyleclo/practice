#include <iostream>

using namespace std;

void SelectionSort(int x[], int n);
void PrintArray(int x[], int n);



int main(){

	int n = 6;
	int x[] = {2, 5, 3, 6, 1, 4};

	SelectionSort(x, n);
	PrintArray(x, n);

	return 0;
}



void SelectionSort(int x[], int n){

	for(int i = 0; i < n - 1; i++){

		int indexMin = i;

		// find minimum
		for(int j = i + 1; j < n; j++){
			if(x[j] < x[indexMin]){ indexMin = j; }
		}

		// swap positions
		int temp = x[i];
		x[i] = x[indexMin];
		x[indexMin] = temp;
	}
}

void PrintArray(int x[], int n){

	for(int i = 0; i < n; i++){
		cout << x[i] << " ";
	}
}
