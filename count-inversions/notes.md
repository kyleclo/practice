

## Problem

#### Ranking items

Suppose we have items A, B, C, D, E, F.  These were listed in order of decreasing **rank**, where item A has the highest rank and item F has the lowest rank.

When asked to provide their personal ranking of these items, our participant provides the array:
```{c++}
int x[] = {2, 5, 3, 6, 1, 4};
```

This means the participant ranks the items:
* E has rank 1
* A has rank 2
* ...
* D has rank 6

#### Inversions

An **inversion** occurs when:
* Object *i* is ranked above Object *j* according to some Ranking
* But Object *j* is ranked above Object *i* according to a different Ranking

Two sets of rankings are typically compactly represented by a single array:
* One Ranking is represented by the **index position** in the array
    + For example, position 0 corresponds to the Rank 1 item; position 1 to the Rank 2 item; and so on
* The other Ranking is represented by the **array values**
    + In our earlier example, the first item was given Rank 2; the second item was given Rank 5; and so on

Then we can identify an inversion occurs when:
* A pair of indices **i** and **j** are such that **i < j**
* But their array values **x[i]** and **x[j]** are such that **x[i] > x[j]**
    
For example, item B is in Position 1 but given Rank 5.  Item C is given Position 2 but given Rank 3.  Since item B has a lower index but a higher array value than item C, the items B and C are inverted.  We denote this **5-3**.

## Algorithm

This algorithm is basically a slight augmentation of the Merge Sort algorithm.

#### Brute Force

The brute force method is to simply find all **n choose 2** pairs of items and check whether the item ranks are inverted.  This is slow.

#### Divide and Conquer

First, suppose you divided the array into Left and Right subarrays and were able to know the number of inversions **within** each subarray.  Then the **total number of inversions** is equal to the number of inversions **within** each subarray **plus** the number of inversions **between** the subarrays.

#### Counting within subarrays

With enough divisions, we end up with subarrays of length 1.  There are **zero inversions for arrays of only one element**. Hence their returned counts are **zero**.

#### Counting between subarrays

The true inversion counting takes place when we count inversions between subarrays.

See this example:

```{c++}
int left[] = {2, 5, 3};

int right[] = {6, 1, 4};    // left-right inversions: 2-1, 5-1, 5-4, 3-1 

int right[] = {1, 4, 6};    // left-right inversions: 2-1, 5-1, 5-4, 3-1
```

We see that the order is important when counting inversions **within** a subarray, but **order doesn't matter when it comes to counting between subarrays**.  

#### Why sort if order doesn't matter?

Notice in the example above, we need to compare:
* 2 versus 6, 1, and 4
* 5 versus 6, 1, and 4
* 3 versus 6, 1, and 4

This gives us the correct number of inversions, but is the same as the brute force method because we're essentially comparing every possible pair of items.

**The goal is to skip some comparisons.** What if we were to sort the subarrays?

```{c++}
int left[] = {2, 3, 5};
int right[] = {1, 4, 6};
```

* Notice that 1 is to the right of 2, 3, and 5.  This contributes 3 inversions to the total count.
* And notice that 4 is to the right of 5.  This contributes 1 inversion to the total count.

If we maintain a sorted order, we merely need to execute the **Merge** step and increment the total inversion count by **the number of remaining values in the Left subarray** whenever we **merge a value in the Right subarray**.

This allows us to count the number of inversions between subarrays in **linear time**.
