#include <iostream>

using namespace std;

void BubbleSort(int x[], int n);
void PrintArray(int x[], int n);



int main(){

	int n = 6;
	int x[] = {2, 5, 3, 6, 1, 4};

	BubbleSort(x, n);
	PrintArray(x, n);

	return 0;
}


void BubbleSort(int x[], int n){

	for(int indexEnd = n; indexEnd >= 1; indexEnd--){   // once bubbled to end, don't check element for swap

		bool swapped = false;

		for(int i = 1; i <= indexEnd; i++){

			if(x[i - 1] > x[i]){
				int temp = x[i - 1];
				x[i - 1] = x[i];
				x[i] = temp;
				swapped = true;
			}
		}

		if(swapped == false){ break; }
	}
}


void PrintArray(int x[], int n){

	for(int i = 0; i < n; i++){
		cout << x[i] << " ";
	}
}
