"""

Generate an unbiased coin toss using only a biased coin

    'unbiased_flip_using_biased_coin_naive()' implements Von Neumann method

-------------------------------------------------------------------------------

        Let Pr(Heads) = p.  Then Pr(Finish in Single Trial) = 2p(1-p)

        If we let X = number of flips to return a result,
         then X ~ Geometric(2p(1-p))
        Thus E[X] = 1 / (2p(1-p))

-------------------------------------------------------------------------------

        Alternatively:
        E[X] = {Finish in Single Trial} * Pr(Finish in Single Trial)
               + {Need to Redo + E[X]} * Pr(Need to Redo)
             = 2 * 2p(1-p) + (2 + E[X]) * (1 - 2p(1-p))
             = 1 / (2p(1-p))


Source:  http://www.eecs.harvard.edu/~michaelm/coinflipext.pdf
"""

import numpy as np


def unbiased_flip_using_biased_coin_naive():
    sample_space = ['H', 'T']

    first, second = np.random.choice(a=sample_space, size=2)

    if first != second:
        return first
    else:
        return unbiased_flip_using_biased_coin_naive()
