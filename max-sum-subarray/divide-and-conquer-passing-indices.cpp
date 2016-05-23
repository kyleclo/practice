#include <iostream>

struct Subarray{
    
    int indexStart;
    int indexEnd;
    int sum;
};


void printArray(int* x, int indexStart, int indexEnd);
Subarray findMaxCrossSubarray(int* x, int indexStart, int indexMiddle, int indexEnd);
Subarray findMaxSumSubarray(int* x, int indexStart, int indexEnd);


int main(){
    
    int x[] = {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7};
    int n = sizeof(x) / sizeof(x[0]);
    
    Subarray maxSumSubarray = findMaxSumSubarray(x, 0, n - 1);
    printArray(x, maxSumSubarray.indexStart, maxSumSubarray.indexEnd);
    
    
    return 0;
}


void printArray(int* x, int indexStart, int indexEnd){
    
    for(int i = indexStart; i <= indexEnd; i++)
        std::cout << x[i] << " ";
    
    std::cout << std::endl;
}


Subarray findMaxCrossSubarray(int* x, int indexStart, int indexMiddle, int indexEnd){
    
    // find max left subarray that ends at indexMiddle
    int indexLeft = indexMiddle;
    int maxSumLeft = 0;
    int sumLeft = 0;
    for(int i = indexLeft; i >= indexStart; i--){
        
        sumLeft += x[i];
        
        if(sumLeft > maxSumLeft){
            indexLeft = i;
            maxSumLeft = sumLeft;
        }
    }

    // find max right subarray that starts at indexMiddle + 1
    int indexRight = indexMiddle + 1;
    int maxSumRight = 0;
    int sumRight = 0;
    for(int i = indexRight; i <= indexEnd; i++){
        
        sumRight += x[i];
        
        if(sumRight > maxSumRight){
            indexRight = i;
            maxSumRight = sumRight;
        }
    }
    
    // get maximum cross subarray
    Subarray out = {indexLeft, indexRight, maxSumLeft + maxSumRight};
    
    return out;
}


Subarray findMaxSumSubarray(int* x, int indexStart, int indexEnd){
    
    if(indexStart < indexEnd){
        
        int indexMiddle = indexStart + (indexEnd - indexStart) / 2;
        
        Subarray left = findMaxSumSubarray(x, indexStart, indexMiddle);
        Subarray right = findMaxSumSubarray(x, indexMiddle + 1, indexEnd);
        Subarray cross = findMaxCrossSubarray(x, indexStart, indexMiddle, indexEnd);
        
        if(left.sum > right.sum && left.sum > cross.sum)
            return left;
            
        else if(right.sum > left.sum && right.sum > cross.sum)
            return right;
            
        else
            return cross;
    }
    
    else{
        
        Subarray single = {indexStart, indexStart, x[indexStart]};
        return single;
    }
}
