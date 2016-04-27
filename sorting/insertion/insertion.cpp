#include <iostream>
#include <vector>

using namespace std;

void InsertionSort(vector <int> & x);
void PrintArray(vector <int> & x);


int main(){

        int n = 6;
        int values[] = {2, 5, 3, 6, 1, 4};

        vector <int> x(&values[0], &values[n]);

        InsertionSort(x);
        PrintArray(x);

        return 0;
}


void InsertionSort(vector <int> & x){

        int n = x.size();

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


void PrintArray(vector <int> & x){

        int n = x.size();

        for(int i = 0; i < n; i++){
                cout << x[i] << " ";
        }
}

