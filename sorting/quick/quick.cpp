#include <iostream>

using namespace std;

void QuickSortSlow(int x[], int indexStart, int indexEnd);
void QuickSortFast(int x[], int indexStart, int indexEnd);
void PrintArray(int x[], int n);



int main(){

	int n = 6;
	int x[] = {2, 5, 3, 6, 3, 4};
	QuickSortSlow(x, 0, n - 1);
	PrintArray(x, n);

	cout << endl;

	int y[] = {2, 5, 3, 6, 3, 4};
	QuickSortFast(y, 0, n - 1);

	PrintArray(y, n);

	return 0;
}

void QuickSortSlow(int x[], int indexStart, int indexEnd){

	// length of x greater than 1
	if(indexStart < indexEnd){

		// partition
		int pivot = x[indexEnd];
		int indexMiddle = indexStart;

		for(int i = indexStart; i < indexEnd; i++){

			// if any x[i] < pivot, then swap it into left side
			if(x[i] < pivot){
				int temp = x[indexMiddle];
				x[indexMiddle] = x[i];
				x[i] = temp;
				indexMiddle++;
			}
		}

		// swap last value (pivot) into middle
		x[indexEnd] = x[indexMiddle];
		x[indexMiddle] = pivot;

		// sort left/right subarrays
		QuickSortSlow(x, indexStart, indexMiddle - 1);
		QuickSortSlow(x, indexMiddle + 1, indexEnd);
	}
}


void QuickSortFast(int x[], int indexStart, int indexEnd){

	if(indexStart < indexEnd){

		int pivot = x[indexStart];
		int indexLeft = indexStart;
		int indexRight = indexEnd;

		while(x[indexLeft] < pivot){ indexLeft++; }
		while(x[indexRight] > pivot){ indexRight--; }

		if(indexLeft <= indexRight){
			int temp = x[indexLeft];
			x[indexLeft] = x[indexRight];
			x[indexRight] = temp;
			indexLeft++;
			indexRight--;
		}

		QuickSortFast(x, indexStart, indexRight);
		QuickSortFast(x, indexLeft, indexEnd);
	}
}



void PrintArray(int x[], int n){

	for(int i = 0; i < n; i++){
		cout << x[i] << " ";
	}
}

