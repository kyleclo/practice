#include <iostream>
#include <vector>
#include <numeric>


std::vector<int> findMaxSumSubarray(std::vector<int> &x, int indexStart, int indexEnd);
std::vector<int> findMaxCrossSubarray(std::vector<int> &x, int indexStart, int indexMiddle, int indexEnd);
void printVector(std::vector<int> &x);


int main(){
    
    std::vector<int> x = {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7};
    
    std::vector<int> subX = findMaxSumSubarray(x, 0, x.size() - 1);
    
    printVector(subX);
    std::cout << std::accumulate(subX.begin(), subX.end(), 0) << std::endl;
    
    return 0;
}


std::vector<int> findMaxSumSubarray(std::vector<int> &x, int indexStart, int indexEnd){
    
    if(indexStart < indexEnd){
        
        int indexMiddle = indexStart + (indexEnd - indexStart) / 2;
    
        std::vector<int> left = findMaxSumSubarray(x, indexStart, indexMiddle);
        std::vector<int> right = findMaxSumSubarray(x, indexMiddle + 1, indexEnd);
        std::vector<int> cross = findMaxCrossSubarray(x, indexStart, indexMiddle, indexEnd);
        
        int sumLeft = std::accumulate(left.begin(), left.end(), 0);
        int sumRight = std::accumulate(right.begin(), right.end(), 0);
        int sumCross = std::accumulate(cross.begin(), cross.end(), 0);
        
        if (sumLeft > sumRight && sumLeft > sumCross)
            return left;
        
        else if(sumRight > sumLeft && sumRight > sumCross)
            return right;
        
        else
            return cross;
    }
    
    else
        return {};
}


std::vector<int> findMaxCrossSubarray(std::vector<int> &x, int indexStart, int indexMiddle, int indexEnd){

    // find max left subarray that ends at indexMiddle
    int indexMaxLeft = indexMiddle;
    int maxSumLeft = 0;
    int currentSum = 0;
    for(int i = indexMaxLeft; i >= indexStart; i--){
        
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


void printVector(std::vector<int> &x){
    
    int n = x.size();
    
    for(int i = 0; i < n; i++)
        std::cout << x[i] << " ";
        
     std::cout << std::endl;
}
