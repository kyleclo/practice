# include <iostream>
# include <vector>

//using namespace std;

void insertionSort(std::vector<int>& x);
void printVector(std::vector<int>& x);

int main(){

    std::vector<int> x = {2, 5, 3, 6, 1, 4};
    
    insertionSort(x);
    printVector(x);
    
    return 0;
}

void insertionSort(std::vector<int>& x){
    
    int n = x.size();
    
    for(int indexCandidate = 1; indexCandidate < n; indexCandidate++){
        
        int candidate = x[indexCandidate];
        int indexInsertLocation = indexCandidate - 1;
        
        while(indexInsertLocation >= 0 && x[indexInsertLocation] > candidate){
            
            x[indexInsertLocation + 1] = x[indexInsertLocation];
            indexInsertLocation--;
        }
        
        x[indexInsertLocation + 1] = candidate;
    }
}


void printVector(std::vector<int>& x){
    
    int n = x.size();
    
    for(int i = 0; i < n; i++)
        std::cout << x[i] << " ";
        
    std::cout << std::endl;
}
