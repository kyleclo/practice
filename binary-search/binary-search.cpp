#include <iostream>

using namespace std;

int BinarySearchIter(int array[], int n, int x);
int BinarySearchRecurs(int array[], int x, int indexStart, int indexEnd);

int main(){

	int n = 6;
	int array[] = {1, 2, 3, 4, 5, 6};

	cout << BinarySearchIter(array, n, 1) << endl;
	cout << BinarySearchIter(array, n, 6) << endl;
	cout << BinarySearchIter(array, n, 3) << endl;
	cout << BinarySearchIter(array, n, 7) << endl;
	cout << BinarySearchIter(array, n, 0) << endl;

	cout << BinarySearchRecurs(array, 1, 0, n - 1) << endl;
	cout << BinarySearchRecurs(array, 6, 0, n - 1) << endl;
	cout << BinarySearchRecurs(array, 3, 0, n - 1) << endl;
	cout << BinarySearchRecurs(array, 7, 0, n - 1) << endl;
	cout << BinarySearchRecurs(array, 0, 0, n - 1) << endl;

	return 0;
}


int BinarySearchIter(int array[], int n, int x){

	int indexStart = 0;
	int indexEnd = n - 1;

	// while subarray at least length 1
	while(indexStart <= indexEnd){

		int indexMiddle = indexStart + (indexEnd - indexStart) / 2;

		if(array[indexMiddle] < x){ indexStart = indexMiddle + 1; }
		else if(array[indexMiddle] > x){ indexEnd = indexMiddle - 1; }
		else{ return(indexMiddle); }
	}

	return(-1);
}


int BinarySearchRecurs(int array[], int x, int indexStart, int indexEnd){

	if(indexStart <= indexEnd){

		int indexMiddle = indexStart + (indexEnd - indexStart) / 2;

		if(array[indexMiddle] < x){ return(BinarySearchRecurs(array, x, indexMiddle + 1, indexEnd)); }
		else if(array[indexMiddle] > x){ return(BinarySearchRecurs(array, x, indexStart, indexMiddle - 1)); }
		else{ return(indexMiddle); }
	}

	else{
		return(-1);
	}

}
