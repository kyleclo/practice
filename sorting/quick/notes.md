
This is my attempt to assess variants of the Quick Sort algorithm.

## General

The Quick Sort algorithm chooses a **pivot** value from among the array elements, and **divides** the array into Left and Right subarrays: 
* All elements in the Left subarray are less than the pivot
* All elements in the Right subarray are greater than the pivot
Once the array is partitioned, the Quick Sort algorithm runs again on each subarray.

Eventually, the subarrays have length 1. In this case, the Quick Sort algorithm needs not execute because that subarray would be already sorted.

## Lomuto

This is the version in which:
* We select an element to be the pivot
* We have a **single** index denoting the location of a **middle** element
* We loop over each **candidate** element (other than the pivot) and perform:
    + Swaps between the middle element and the candidate element
    + Increments to the middle index
* We finally **swap the pivot with the middle element**, thereby correctly separating the array into Left and Right subarrays

#### Pivot should remain unmoved until the final swap into the middle index

```{c++}
int x[] = {3, 1};

int pivot = x[indexStart];          // both pivot location and indexMiddle start at 0
int indexMiddle = indexStart;

for(int indexCandidate = indexStart; indexCandidate <= indexEnd; indexCandidate++){      // for candidates values [3, 1]
   
   // candidate 3 NOT LESS THAN pivot 3    ==>     indexMiddle = 0
   // candidate 1  IS LESS THAN pivot 3    ==>     indexMiddle = 1     array becomes x = [1, 3]
}

// swap pivot x[indexStart] with x[indexMiddle]   ==>     array becomes x = [3, 1]      WHICH IS INCORRECT
```
