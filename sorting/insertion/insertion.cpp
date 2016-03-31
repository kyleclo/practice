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

	for(int indexCandidate = 1; indexCandidate < n; indexCandidate++){

		int candidate = x[indexCandidate];
		int i = indexCandidate - 1;

		while(i >= 0 && x[i] > candidate){
			x[i + 1] = x[i];
			i--;
		}

		x[i + 1] = candidate;
	}
}


void PrintArray(int x[], int n){

	for(int i = 0; i < n; i++){
		cout << x[i] << " ";
	}
}
