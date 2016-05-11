
This is my attempt to assess variants of the Quick Sort algorithm.

## General

The Quick Sort algorithm chooses a **pivot** value from among the array elements, and **divides** the array into Left and Right subarrays: 
* All elements in the Left subarray are less than the pivot
* All elements in the Right subarray are greater than the pivot
Once the array is partitioned, the Quick Sort algorithm runs again on each subarray.

Eventually, the subarrays have length 1. In this case, the Quick Sort algorithm needs not execute because a subarray of length 1 is already sorted.

## Lomuto

This is the version in which:
* We select an element to be the pivot
* We have a **single** index denoting the location of a **middle** element
* We loop over each **candidate** element and perform:
    + **Swaps** between the candidate and the middle element in order to **satisfy the subarray conditions**
    + Increments to the middle index
* We finally **swap the pivot with the middle element**, thereby correctly separating the array into Left and Right subarrays

#### Pivot must remain unmoved until the final swap

```{c++}
int x[] = {3, 1};

int pivot = x[indexStart];          // both pivot location and indexMiddle start at 0
int indexMiddle = indexStart;

for(int indexCandidate = indexStart; indexCandidate <= indexEnd; indexCandidate++){      // for candidate values [3, 1]
   
   // candidate 3 NOT LESS THAN pivot 3    ==>     indexMiddle = 0
   // candidate 1  IS LESS THAN pivot 3    ==>     indexMiddle = 1     array becomes x = [1, 3]
}

// swap pivot x[indexStart] with x[indexMiddle]   ==>     array becomes x = [3, 1]      WHICH IS INCORRECT
```

* Can't start indexMiddle at same location as pivot
* Can't allow indexMiddle to ever be at same location as pivot
        + Hence, easier to select pivot at Start or End of array
* indexCandidate can skip over pivot location since the if-condition for swap never applies

#### Middle index needs to start from one end of the array (either Start or End)

```{c++}
int x[] = {3, 2, 1};

int pivot = x[indexStart];              // pivot starts at index 0
int indexMiddle = indexStart + 1;       // indexMiddle = 1

for(int indexCandidate = indexStart + 1; indexCandidate <= indexEnd; indexCandidate++){      // for candidate values [2, 1]

    // candidate 2 IS LESS THAN pivot 3     ==>     indexMiddle = 2     array becomes x = [3, 2, 1]
    // candidate 1 IS LESS THAN pivot 3     ==>     indexMiddle = 3     array becomes x = [3, 2, 1]
}

// swap pivot x[indexStart] with x[indexMiddle]     ==>     ERROR BECAUSE indexMiddle = 3 IS OUT OF BOUNDS
```

* Error roccurs when every candidate requires a swap, thereby allowing indexMiddle to increment enough to fall out of bounds

#### Conclusion

It seems the Lomuto algorithm can work in both directions, but essentially requires:
* Pivot selected from Start or End
* indexMiddle selected from opposite end of Pivot

