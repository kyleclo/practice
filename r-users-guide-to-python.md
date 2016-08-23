#  Dataframes

##  Subsetting

### R

#### Method 1:  Using `subset()`
```R
newDf <- subset(df, x1 == 5 & x2 == 3)
```
- Each subcondition references the columns as variables.
- Each subcondition produces a boolean vector.
- `R` vectorizes the `&` operation between these vectors.

#### Method 2:  Passing a boolean vector into the `row` argument in the `[]` operator
```R
index <- df[,'x1'] == 5 & df[,'x2'] == 3
newDf <- df[index,]
```
- Note that `df[,'colname']` can be replaced by `df$colname`, but this makes the code less flexible.


### Python

#### Method 1:  Passing a boolean vector into the `[]` operator
```python
index = (df['x1'] == 5) & (df['x2'] == 3)
new_df = df[index]
```
- Each subcondition produces a `Pandas.Series` object, which knows to execute the `&` operation elementwise.
    - This syntax also works on `numpy.ndarray` objects, but not on typical Python lists.
- The parantheses around each subcondition in Python are necessary because `&` has [precedence](https://docs.python.org/2/reference/expressions.html#evaluation-order) over `==`.
    - In R, this is [reversed](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Syntax.html).
- Using `and` instead of `&` will throw an error.

- Note that `df['colname']` can be replaced by `df.colname`, but this makes the code less flexible.
