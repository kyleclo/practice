#  binary search

binarySearch <- function(x, input, start, end){
  if(end < start){
    return(NULL)
  }
  
  else{
    middle <- start + floor((end - start) / 2)
    
    if(x[middle] < input) return(binarySearch(x, input, start, middle - 1))
    else if(x[middle] > input) return(binarySearch(x, input, middle + 1, end))
    else return(middle)
  }
}

x <- c(5,2,4,6,1,3)
binarySearch(x, 5, 1, length(x))
binarySearch(x, 3, 1, length(x))
binarySearch(x, 7, 1, length(x))
