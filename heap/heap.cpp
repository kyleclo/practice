#include <iostream>
#include <vector>
#include <algorithm>


class BinaryMaxHeap{
    private:
    
        // storage
        std::vector<int> heap;
        
        // for indexing
        int getParentIndex(int indexNode){ return (indexNode - 1) / 2; }
        int getLeftIndex(int indexNode) { return 2 * indexNode + 1; }
        int getRightIndex(int indexNode) { return 2 * indexNode + 2; }
        
        // utility
        void maxHeapify(int indexRoot);             // corrects root given heap subtrees
        void buildMaxHeap(std::vector<int> &x);     // converts unordered vector to heap
        
    public:
    
        // constructor
        BinaryMaxHeap(){};
        BinaryMaxHeap(std::vector<int> &x) { buildMaxHeap(x); }
        
        // get basic info
        int getSize() { return heap.size(); }
        int getMax() { return heap.front(); }
        
        // change structure
        void extractMax();
        void insert(int element);
        void modifyKey(int indexNode);
        
        // utility
        void print();
        std::vector<int> sort();
};


int main(){
    
    std::vector<int> x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    BinaryMaxHeap y(x);
    
    return 0;
}



void BinaryMaxHeap::maxHeapify(int indexRoot){
    
    int indexLeft = getLeftIndex(indexRoot);
    int indexRight = getRightIndex(indexRoot);
    
    int indexLimit = (heap.size()-1)/2;
    
    int keyRoot = heap.at(indexRoot);
    int keyLeft = heap.at(indexLeft);
    int keyRight = heap.at(indexRight);
    
    std::vector<int> keys = {keyRoot, keyLeft, keyRight};
    int keyMax = *std::max_element( keys.begin() , keys.end() );  // max_element returns iterator
    
    if(keyMax == keyRoot | indexLeft >= indexLimit | indexRight >= indexLimit)
        return;
    
    else if(keyMax == keyLeft){
        
        std::swap( heap.at(indexRoot) , heap.at(indexLeft) );
        maxHeapify( indexLeft );
    }
    
    else{
        
        std::swap( heap.at(indexRoot) , heap.at(indexRight) );
        maxHeapify( indexRight );
    }
}


void BinaryMaxHeap::buildMaxHeap(std::vector<int> &x){
    
    heap = x;
    for(int i = (heap.size()-1)/2; i >= 0; i--)
        maxHeapify(i);
}


