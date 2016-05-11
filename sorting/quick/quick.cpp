#include <iostream>
#include <vector>

void quickSortLomuto(std::vector<int>& x, const int indexStart, const int indexEnd);
void quickSortHoare(std::vector<int>& x, const int indexStart, const int indexEnd);
void printVector(std::vector<int>& x);


int main(){
    
    std::vector<int> x = {2, 5, 3, 6, 1, 4};
    
    quickSortLomuto(x, 0, x.size() - 1);
    printVector(x);
    
    std::vector<int> y = {2, 5, 3, 6, 1, 4};
    
    quickSortHoare(y, 0, y.size() - 1);
    printVector(y);
    
    return 0;
}


void quickSortLomuto(std::vector<int>& x, const int indexStart, const int indexEnd){
   
   if(indexStart < indexEnd){       // if length = 1, no need to sort further
       
       int const pivot = x[indexEnd];       // see notes: pick pivot at Start or End
       int indexMiddle = indexStart;        // see notes: indexMiddle at opposite end of pivot
       
       // skip pivot
       for(int indexCandidate = indexStart; indexCandidate < indexEnd; indexCandidate++){
           
           // move everything less than pivot to the left subarray
           if(x[indexCandidate] < pivot){
               
               int temp = x[indexMiddle];
               x[indexMiddle] = x[indexCandidate];
               x[indexCandidate] = temp;
               
               indexMiddle++;
           }
       }
       
       // swap pivot into middle
       x[indexEnd] = x[indexMiddle];
       x[indexMiddle] = pivot;
       
       // sort the subarrays
       quickSortLomuto(x, indexStart, indexMiddle - 1);
       quickSortLomuto(x, indexMiddle + 1, indexEnd);
   }
}


void quickSortHoare(std::vector<int>& x, const int indexStart, const int indexEnd){
    
    if(indexStart < indexEnd){
        
        int const pivot = x[indexStart];
        int indexLeft = indexStart;
        int indexRight = indexEnd;
        
        while(indexLeft <= indexRight){
            
            while(x[indexLeft] < pivot)
                indexLeft++;
            
            while(x[indexRight] > pivot)
                indexRight--;
            
            if(indexLeft <= indexRight){
                
                int temp = x[indexLeft];
                x[indexLeft] = x[indexRight];
                x[indexRight] = temp;
                
                indexLeft++;
                indexRight--;
            }
        }
        
        quickSortHoare(x, indexStart, indexRight);
        quickSortHoare(x, indexLeft, indexEnd);
    }
}


void printVector(std::vector<int>& x){
    
    int n = x.size();
    
    for(int i = 0; i < n; i++)
        std::cout << x[i] << " ";
    
    std::cout << std::endl;
}
