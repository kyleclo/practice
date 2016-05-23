
## Proof

#### Probability of New Item staying in final set

For i = k+1 ...

P(Accept item i) = k / i
P(Don't get selected out by next item i+1) = ((i+1) - 1) / (i + 1) = i / (i + 1)
P(Don't get selected ever) = i / (i + 1)   *   (i + 1) / (i + 2)   *   ...   *   (n - 1) / n

P(Item i stays until final) = P(Accept item i) * P(Don't get selected ever) = k / n

#### Probability of Original Item staying in final set

For i = 1 ... k

P(Don't get selected out by item i) = k / i
P(Don't get selected ever) = 
