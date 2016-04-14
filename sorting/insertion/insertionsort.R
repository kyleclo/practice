#  insertion sort

insertionSort <- function(x){
  n <- length(x)
  for(i in 2:n){
    candidate <- x[i]
    j <- i-1
    while(x[j] > candidate && j >= 1){
      x[j+1] <- x[j]
      j <- j-1
    }
    x[j+1] <- candidate
  }
  return(x)
}


x <- c(5,2,4,6,1,3)
insertionSort(x)
