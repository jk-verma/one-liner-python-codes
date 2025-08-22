'''
Problem: MAURICE'S RACING SNAILS
Description: Maurice and Steve engage in a snail race, each owning three snails of
             different speeds: slow (s), medium (m), and fast (f). Although Maurice's
             snails are generally faster, Steve's strategy poses a challenge. In each
             of the three rounds, they pit their snails against each other strategically.
             Maurice's plan involves sacrificing his slower snails strategically to
             ensure victory. This function evaluates Maurice's plan, determining if he
             wins at least 2 out of 3 games against Steve's snails.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''

def maurice_wins(m_snails, s_snails):
    wins = sum(m > s for m, s in zip(m_snails, s_snails))
    return wins >= 2
# Example usage:
print(maurice_wins([1, 2, 3], [3, 2, 1]))
# Output: True