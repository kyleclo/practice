#include <iostream>

using namespace std;

void MergeSort(int x[], int indexStart, int indexEnd);
void Merge(int x[], int indexStart, int indexMiddle, int indexEnd);
void PrintArray(int x[], int n);



int main(){

	int n = 6;
	int x[] = {6,5,4,3,2,1};

	MergeSort(x, 0, n - 1);
	PrintArray(x, n);

	return 0;
}


void MergeSort(int x[], int indexStart, int indexEnd){

	if(indexStart < indexEnd){

		int indexMiddle = (indexEnd + indexStart) / 2;    // floors decimals by default
		MergeSort(x, indexStart, indexMiddle);
		MergeSort(x, indexMiddle + 1, indexEnd);
		Merge(x, indexStart, indexMiddle, indexEnd);
	}
}

void Merge(int x[], int indexStart, int indexMiddle, int indexEnd){

	int n = indexEnd - indexStart + 1;
	int* temp = new int[n];

	int i = 0;
	int indexLeft = indexStart;
	int indexRight = indexMiddle + 1;

	// while both left & right subarrays non-empty
	while(indexLeft <= indexMiddle && indexRight <= indexEnd){

		if(x[indexLeft] <= x[indexRight]){
			temp[i] = x[indexLeft];
			indexLeft++;
		}  else{
			temp[i] = x[indexRight];
			indexRight++;
		}

		i++;
	}

	// if one subarray finishes early, continue with remaining
	while(indexLeft <= indexMiddle){
		temp[i] = x[indexLeft];
		indexLeft++;
		i++;
	}

	while(indexRight <= indexEnd){
		temp[i] = x[indexRight];
		indexRight++;
		i++;
	}

	// replace x with sorted values in temp
	for(int k = 0; k < n; k++){
		x[indexStart + k] = temp[k];
	}

	delete[] temp;
}


void PrintArray(int x[], int n){

	for(int i = 0; i < n; i++){
		cout << x[i] << " ";
	}
}
