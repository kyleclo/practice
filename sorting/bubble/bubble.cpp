# include <iostream>
# include <vector>

void bubbleSort(std::vector<int>& x);
void printVector(std::vector<int>& x);

int main(){

    std::vector<int> x = {2, 5, 3, 6, 1, 4};
    
    bubbleSort(x);
    printVector(x);
    
    return 0;
}

void bubbleSort(std::vector<int>& x){
    
    int n = x.size();
    
    for(int indexEnd = n; indexEnd > 0; indexEnd--){
        
        bool swapped = false;
        
        for(int indexLeft = 0; indexLeft < indexEnd; indexLeft++){
            
            if(x[indexLeft] > x[indexLeft + 1]){
                
                int temp = x[indexLeft];
                x[indexLeft] = x[indexLeft + 1];
                x[indexLeft + 1] = temp;
                
                swapped = true;
            }
        }
        
        if(swapped == false)
            break;
    }
}

void printVector(std::vector<int>& x){

    int n = x.size();
    
    for(int i = 0; i < n; i++)
        std::cout << x[i] << " ";
    
    std::cout << std::endl;
}
