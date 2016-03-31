#include <iostream>

using namespace std;

void QuickSort(int x[], int indexStart, int indexEnd);
int Partition(int x[], int indexStart, int indexEnd);
void PrintArray(int x[], int n);



int main(){

	int n = 6;
	int x[] = {2, 5, 3, 6, 1, 4};

	QuickSort(x, 0, n - 1);
	PrintArray(x, n);

	return 0;
}

void QuickSort(int x[], int indexStart, int indexEnd){

	if(indexStart < indexEnd){

		int indexMiddle = Partition(x, indexStart, indexEnd);
		QuickSort(x, indexStart, indexMiddle - 1);
		QuickSort(x, indexMiddle + 1, indexEnd);
	}
}


void QuickSort2(index x[], int indexStart, int indexEnd){

}



int Partition(int x[], int indexStart, int indexEnd){

	int pivot = x[indexEnd];
	int indexNewLocationForPivot = indexStart;

	for(int i = indexStart; i < indexEnd; i++){

		// move any x[i] less than pivot to the left
		if(x[i] <= pivot){
			int temp = x[indexNewLocationForPivot];
			x[indexNewLocationForPivot] = x[i];
			x[i] = temp;
			indexNewLocationForPivot++;
		}
	}

	// swap last value (pivot) into middle
	x[indexEnd] = x[indexNewLocationForPivot];
	x[indexNewLocationForPivot] = pivot;

	return(indexNewLocationForPivot);
}


void PrintArray(int x[], int n){

	for(int i = 0; i < n; i++){
		cout << x[i] << " ";
	}
}

