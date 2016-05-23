#include <iostream>
#include <vector>

void printVector(std::vector<int>& x);
void selectionSort(std::vector<int>& x);


int main(){
    
    std::vector<int> x = {2, 5, 3, 6, 1, 4};
    
    selectionSort(x);
    printVector(x);
    
    return 0;
}


void selectionSort(std::vector<int>& x){
    
    int n = x.size();
    
    for(int indexSlot = 0; indexSlot < n - 1; indexSlot++){
        
        int indexMin = indexSlot;
        
        // find min among remaining values
        for(int indexMinCandidate = indexMin + 1; indexMinCandidate < n; indexMinCandidate++)
            if(x[indexMinCandidate] < x[indexMin])
                indexMin = indexMinCandidate;
                
        // swap min into slot
        int temp = x[indexSlot];
        x[indexSlot] = x[indexMin];
        x[indexMin] = temp;
    }
}

void printVector(std::vector<int>& x){
    
    int n = x.size();
    
    for(int i = 0; i < n; i++)
        std::cout << x[i] << " ";
    
    std::cout << std::endl;
}
