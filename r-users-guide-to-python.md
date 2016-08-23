#  Dataframes

##  Subsetting via column names

### R
Each subcondition produces a boolean vector, and `R` vectorizes the `&` operation
```R
newDf <- subset(df, x1 == 5 & x2 == 3)
```

### Python
Each subcondition produces a `Pandas.Series` object, which knows to execute the `&` operation elementwise.  This syntax also works on `numpy.ndarray` objects, but not on typical Python lists.
```python
new_df <- df[df, (x1 == 5) & (x2 == 3)]
```

### Notes
- The parantheses around each subcondition in Python are necessary because `&` has [precedence](https://docs.python.org/2/reference/expressions.html#evaluation-order) over `==`.  In R, this is [reversed](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Syntax.html).
- In Python, using `and` instead of `&` will throw an error.

##  Subsetting via boolean index

### R
Create a boolean vector and pass it into the `row` argument in the `[]` operator.
```R
index <- df[,'x1'] == 5 & df[,'x2'] == 3
newDf <- df[index,]
```

or compactly
```R
newDf <- df[df[,'x1'] == 5 & df[,'x2'] == 3,]
```

Note that `df[,'colname']` can be replaced by `df$colname`

### Python
```python

```
