# [clf,Reg]Naïve Bayes

## how it works
find weather the email is spam basde on word 'dear'
   - $P(spam|'dear') = \frac{P('dear'|spam) * P(spam)}{P('dear')}$ 
1. find **prior probabilities**: P(spam) and P(not spam)
2. calculate **conditional probabilities** P(word|spam) and P(word|not spam) 
3. apply bayes theorem to predict class 
    1. $P(spam|'dear')= {P('dear'|spam) * P(spam)}$
    2. $P(not spam|'dear') = {P('dear'|not spam) * P(not spam)}$
    3. the email is spam if $P(spam|'dear')> $P(not spam|'dear')$
## math
$y^* = \arg \max_y \,P(x_i | y) \, P(y) = \arg \max_y\sum_iP(x_i|y) + logP(y)$
1. bayes theorem: find weather the email is spam basde on word 'dear'
   - $P(spam|'dear') = \frac{P('dear'|spam) * P(spam)}{P('dear')}$ 
   - refer to (https://www.youtube.com/watch?v=O2L2Uv9pdDA)
2. maximizing logP(x,y) is equivalent to maximizing P(x,y) and often much easier
## strength 
1. effective in small limited data: The model can often generalize well by relying on prior probabilities and conditional probabilities for each feature, even without a large dataset
2. fast training and prediction
## limitation
- independence assumption, which is why it's naive
Naïve Bayes assumes that features are independent, which is rarely true in practice. 
  - for example, naive bayes email classifier assume words are indepent and only focus on single word but ignore languages do have different grammars
- limited modeling powder
