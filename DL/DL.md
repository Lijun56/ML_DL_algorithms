# MLP
- perceptrons
perceptrons: perceptrons performs a weighted sum of inputs, then passes this sum through a step function, outputting either 1 (fire) or 0 (don’t fire).
- perception update rule
- SGD
  in each step, SGD randomly picks a single data point, calculates the gradient of the error with respect to the weights, and then updates the weights in the direction that reduces this error.
- Perceptron Optimization by SGD
- Perceptron is linear but we often need non-linear prediction
## what is MLP
MLPs are non-linear prediction models,composed of multiple linear layers with non-linear activations
MLPs can model complex functions, but hard to optimize. And the optimization is by a form of stochastic gradient descent

Deeper networks are subject to vanishing
gradient problems that can be partially avoided
with ReLU