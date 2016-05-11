#include <iostream>
#include <vector>


int sortAndCountInversions(std::vector<int>& x, const int indexStart, const int indexEnd);
int mergeAndCountInversions(std::vector<int>& x, const int indexStart, const int indexMiddle, const int indexEnd);
void printVector(std::vector<int>& x);


int main(){
    
    //  2-1, 5-3, 5-1, 5-4, 3-1, 6-1, 6-4   ==>  7 inversions
    std::vector<int> x = {2, 5, 3, 6, 1, 4};
    
    int numInversions = sortAndCountInversions(x, 0, x.size() - 1);
    printVector(x);
    std::cout << numInversions << std::endl;
    
    return 0;
}



int sortAndCountInversions(std::vector<int>& x, const int indexStart, const int indexEnd){
    
    int count = 0;
    
    if(indexStart < indexEnd){
        
        const int indexMiddle = indexStart + (indexEnd - indexStart) / 2;
        
        count += sortAndCountInversions(x, indexStart, indexMiddle);
        count += sortAndCountInversions(x, indexMiddle + 1, indexEnd);
        count += mergeAndCountInversions(x, indexStart, indexMiddle, indexEnd);
    }
    
    return count;
}


int mergeAndCountInversions(std::vector<int>& x, const int indexStart, const int indexMiddle, const int indexEnd){
    
    int n = indexEnd - indexStart + 1;
    int* temp = new int[n];
    
    int indexTemp = 0;
    int indexLeft = indexStart;
    int indexRight = indexMiddle + 1;
    
    int count = 0;
    
    while(indexLeft <= indexMiddle && indexRight <= indexEnd){
        
        if(x[indexLeft] <= x[indexRight]){
            temp[indexTemp] = x[indexLeft];
            indexLeft++;
        }
        else{
            temp[indexTemp] = x[indexRight];
            indexRight++;
            
            int numLeftRemaining = indexMiddle - indexLeft + 1;     // number of inversions between Left and Right
            count += numLeftRemaining;
        }
        
        indexTemp++;
    }
    
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
    
    
    for(int i = 0; i < n; i++)
        x[indexStart + i] = temp[i];
    
    
    delete[] temp;
    
    return count;
}


void printVector(std::vector<int>& x){
    
    int n = x.size();
    
    for(int i = 0; i < n; i++)
        std::cout << x[i] << " ";
    
    std::cout << std::endl;
}
