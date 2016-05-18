#include <iostream>
#include <vector>


std::vector<int> findMaxSumSubarray(std::vector<int> &x, int indexStart, int indexEnd);
std::vector<int> findMaxCrossSubarray(std::vector<int> &x, int indexStart, int indexMiddle, int indexEnd);
int sumVector(std::vector<int> &x);
void printVector(std::vector<int> &x);


int main(){
    
    std::vector<int> x = {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7};
    
    std::vector<int> subX = findMaxSumSubarray(x, 0, x.size() - 1);
    
    printVector(subX);
    std::cout << sumVector(subX) << std::endl;
    
    return 0;
}


std::vector<int> findMaxSumSubarray(std::vector<int> &x, int indexStart, int indexEnd){
    
    if(indexStart < indexEnd){
        
        int indexMiddle = indexStart + (indexEnd - indexStart) / 2;
    
        std::vector<int> left = findMaxSumSubarray(x, indexStart, indexMiddle);
        std::vector<int> right = findMaxSumSubarray(x, indexMiddle + 1, indexEnd);
        std::vector<int> cross = findMaxCrossSubarray(x, indexStart, indexMiddle, indexEnd);
        
        int sumLeft = sumVector(left);
        int sumRight = sumVector(right);
        int sumCross = sumVector(cross);
        
        if(sumRight > sumLeft && sumRight > sumCross)
            return right;
            
        else if (sumLeft > sumRight && sumLeft > sumCross)
            return left;
        
        else
            return cross;
    }
    
    std::vector<int> empty = {};
    
    return empty;
}


std::vector<int> findMaxCrossSubarray(std::vector<int> &x, int indexStart, int indexMiddle, int indexEnd){

    // find max left subarray that ends at indexMiddle
    int indexMaxLeft = indexMiddle;
    int maxSumLeft = 0;
    int currentSum = 0;
    for(int i = indexMaxLeft; i >= 0; i--){
        
        currentSum += x[i];
        
        if(currentSum > maxSumLeft){
            maxSumLeft = currentSum;
            indexMaxLeft = i;
        }
    }

    // find max right subarray that starts at indexMiddle + 1
    int indexMaxRight = indexMiddle + 1;
    int maxSumRight = 0;
    currentSum = 0;
    for(int i = indexMaxRight; i <= indexEnd; i++){
        
        currentSum += x[i];
        
        if(currentSum > maxSumRight){
            maxSumRight = currentSum;
            indexMaxRight = i;
        }
    }

    // get maximum cross subarray
    std::vector<int> maxCrossSubarray;
    for(int i = indexMaxLeft; i <= indexMaxRight; i++)
        maxCrossSubarray.push_back(x[i]);

    return maxCrossSubarray;
}



int sumVector(std::vector<int> &x){
    
    int n = x.size();
    int sum = 0;
    
    for(int i = 0; i < n; i++)
        sum += x[i];
    
    return sum;
}


void printVector(std::vector<int> &x){
    
    int n = x.size();
    
    for(int i = 0; i < n; i++)
        std::cout << x[i] << " ";
        
     std::cout << std::endl;
}

