#include <iostream>
#include <vector>

void mergeSort(std::vector<int>& x, const int indexStart, const int indexEnd);
void merge(std::vector<int>& x, const int indexStart, const int indexMiddle, const int indexEnd);
void printVector(std::vector<int>& x);

int main(){
    
    std::vector<int> x = {2, 5, 3, 6, 1, 4};
    
    mergeSort(x, 0, x.size() - 1);
    printVector(x);
    
    return 0;
}


void mergeSort(std::vector<int>& x, const int indexStart, const int indexEnd){
    
    if(indexStart < indexEnd){      // if length = 1, no need to sort further
        
        int indexMiddle = indexStart + (indexEnd - indexStart) / 2;      // floors decimals by default
        mergeSort(x, indexStart, indexMiddle);
        mergeSort(x, indexMiddle + 1, indexEnd);
        merge(x, indexStart, indexMiddle, indexEnd);
    }
}


void merge(std::vector<int>& x, const int indexStart, const int indexMiddle, const int indexEnd){
    
    int n = indexEnd - indexStart + 1;
    int* temp = new int[n];
    
    int indexTemp = 0;
    int indexLeft = indexStart;
    int indexRight = indexMiddle + 1;
    
    // while both left and right subarrays not-empty
    while(indexLeft <= indexMiddle && indexRight <= indexEnd){
        
        if(x[indexLeft] <= x[indexRight]){
            temp[indexTemp] = x[indexLeft];
            indexLeft++;
        }
        else{
            temp[indexTemp] = x[indexRight];
            indexRight++;
        }
        
        indexTemp++;
    }
    
    
    // if one subarray finishes early, continue with remaining
    while(indexLeft <= indexMiddle){
        temp[indexTemp] = x[indexLeft];
        indexLeft++;
        indexTemp++;
    }
    
    while(indexRight <= indexEnd){
        temp[indexTemp] = x[indexRight];
        indexRight++;
        indexTemp++;
    }
    
    
    // replace x with sorted values in temp
    for(int i = 0; i < n; i++)
        x[indexStart + i] = temp[i];
    
    
    delete[] temp;
}


void printVector(std::vector<int>& x){
    
    int n = x.size();
    
    for(int i = 0; i < n; i++)
        std::cout << x[i] << " ";
    
    std::cout << std::endl;
}
