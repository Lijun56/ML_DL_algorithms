# entropy
$
H(X) = -\sum_{x} P(X = x) \log_2 P(X = x)
$

- measure of uncertainty or randomness in variable X
- Intuition: Imagine you’re trying to guess the outcome of a random event, like flipping a coin. If it’s a fair coin, you’re pretty uncertain because it could be either heads or tails, which gives high entropy. If it’s a trick coin that always lands heads, there’s no uncertainty; you know the outcome in advance, giving low entropy.
# specific conditional entropy
$
H(X|Y=y) = -\sum_{x} P(X = x|Y = y) \log_2 P(X = x|Y = y)
$
- measure uncertainty of X Given Y as particular value

# Conditional entropy
$
H(X|Y) = -\sum_{y} H(X|Y = y) P(Y = y)
$
measure expected uncertainty of X given Y
# infomation gain I(X|Y)
$I(X|Y) = H(X) - H(X|Y)$
meansure how much knowing Y would reduce my uncertainty in X