#  Dataframes

##  Subsetting

### R

#### Method 1:  Passing a boolean vector into the `row` argument in the `[]` operator
```R
index <- df[,'x1'] == 5 & df[,'x2'] == 3
newDf <- df[index,]
```
- Each subcondition produces a boolean vector.
- `R` vectorizes the `&` operation between these vectors.
- Note that `df[,'colname']` can be replaced by `df$colname`, but this makes the code less flexible.

#### Method 2:  Using `subset()`
```R
newDf <- subset(df, x1 == 5 & x2 == 3)
```
- Each subcondition references the columns as variables.


### Python

#### Method 1:  Passing a boolean vector into the `[]` operator
```python
index = (df['x1'] == 5) & (df['x2'] == 3)
new_df = df[index]
```
- Each subcondition produces a boolean `Pandas.Series` object, which will execute the `&` operation elementwise.
    - This syntax also works on `numpy.ndarray` objects, but not on typical Python lists.
- The parantheses around each subcondition in Python are necessary because `&` has [precedence](https://docs.python.org/2/reference/expressions.html#evaluation-order) over `==`.
    - In R, this is [reversed](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Syntax.html).
- Using `and` instead of `&` will throw an error.

- Note that `df['colname']` can be replaced by `df.colname`, but this makes the code less flexible.
- Note that `df[index]` can be replaced by `df.loc[index]` or `df.ix[index]`.

#### Method 2:  Using `DataFrame.query()`
```python
new_df = df.query('(x1 == 5) & (x2 == 3)')
```
- Each subcondition references the columns directly.
