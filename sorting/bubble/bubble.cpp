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

	for(int i = n - 2; i >= 0; i--){

		bool swapped = false;

		for(int j = 0; j <= i; j++){

			if(x[j] > x[j + 1]){
				int temp = x[j];
				x[j] = x[j + 1];
				x[j + 1] = temp;
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
