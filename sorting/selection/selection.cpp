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

	for(int indexSortedEnd = 0; indexSortedEnd < n - 1; indexSortedEnd++){

		int indexMin = indexSortedEnd;

		// find minimum among remaining values
		for(int i = indexSortedEnd + 1; i < n; i++){
			if(x[i] < x[indexMin]){ indexMin = i; }
		}

		// swap minimum into Left subarray
		int temp = x[indexSortedEnd];
		x[indexSortedEnd] = x[indexMin];
		x[indexMin] = temp;
	}
}

void PrintArray(int x[], int n){

	for(int i = 0; i < n; i++){
		cout << x[i] << " ";
	}
}
