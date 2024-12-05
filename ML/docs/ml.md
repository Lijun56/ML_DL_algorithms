### Todo
# [intro_ml](intro_to_ml.md)

# [bias-variance trade off](/ML/bias-vairance%20trade%20off.md)


# [clf,reg]KNN(K nearest neighbor)

# [clf]LogReg

# [clf,Reg]Naïve Bayes





# 11/10
1. a regression tree is a type of decision tree specifically designed for regression problems, with different splitting criteria and outputs tailored to continuous target variables.
   1. regression tree spliting mechanism:	Splits data based on features to minimize the variance or mean squared error (MSE) of the target variable in each node.
   2. Q4. What is the regression tree minimizing? X are the input features and Y are the target values: (Conditional Variance of Y given X and the tree model)
2. linear classifier
   1. linear SVM
   2. log Reg
   3. Naive Bayes classifier (on binary features)
   4. perceptrons
3. Q6. Which of these is most easily adapted to new training examples?
   1. 1NN 
   2. (not the answer) Naive bayes is second easiliest( Naive
Bayes with binary features is very fast to update as well, as the probability counts can be
updated eficiently.)
4. Q7. Which of these is always able to achieve minimal error on the trainingset?
   1. 1NN
   2. decision tree
5. Q2. Why might using sigmoid activation in a many-layer network cause optimization diﬃculties?
   1. because With a long chain of gradients that are less than 1, the gradient becomes vanishingly small
   2. so the Deeper networks are subject to vanishing gradient problems that are reduced (but not eliminated) with ReLU activations
6. CNNs are powerful for encoding local patterns with translation invariance and use pooling to effectively expand the receptive field, allowing them to**capture larger patterns** with **fewer parameters** than fully connected layers.
   1. Convolutions allow CNNs to detect patterns regardless of their location in the image, providing translation invariance. This means that a feature detected in one part of the image will still be recognized if it appears in another location.Convolutional Neural Networks (CNNs) are designed to capture spatial hierarchies in data, making them effective for tasks where local patterns are important, such as image recognition.
   2. Pooling layers, like max-pooling or average-pooling, reduce the spatial dimensions of the feature maps, which in turn increases the receptive field of subsequent layers. By pooling, each unit in the feature map covers a larger area of the input, effectively “seeing” a larger portion of the image. This allows the network to capture more context, making it possible to recognize larger patterns formed by smaller ones.
7.  Why were neural networks less effective than other approaches for many years? (select any major factors)
    1.  Deep networks were difficult to optimize due to the **vanishing gradient problem**
    2.  **Most datasets were not big enough** to properly fit / benefit from deep networks
    3.  Deep learning requires much **more computation** than most other methods to be effective
8.  **Bottleneck layers and convolutional layers** mainly provide a benefit in reducing the number of parameters. **ReLU and Skip connections** improve the gradient flow, and **Batch Normalization** stabilizes training.
9.  Adam is generally considered an **improvement** over SGD+Momentum for most deep learning applications, as it **requires less tuning**, is more robust to different types of data, and often leads to faster and more stable convergence. However, SGD+Momentum can still be effective, particularly in simpler tasks or when tuning resources are available, and it’s sometimes preferred for fine-tuning models due to its more predictable behavior.
    1.  “Compute the gradient of the weights wrt the loss”
	2.	“Momentum encourages large changes in directions with consistent gradient”
	3.	“Normalize each weight’s update by the moving average magnitude of its past gradients”

    The key ideas behind Adam are combining momentum (to encourage movement in consistent directions) and adaptive scaling of step sizes (adjusting step sizes based on recent gradients). These mechanisms help Adam adapt to different kinds of loss landscapes, making it particularly effective for many machine learning tasks.
10. Important Parameters for Training a Deep Model

	1.	Model Specification:
	•	This involves defining the architecture of the model, such as the number and types of layers (e.g., convolutional layers, dense layers), and the activation functions used in each layer. Imagine planning the layout for a building; you need a blueprint specifying what goes where. Similarly, the model specification lays out the structure of the neural network, which fundamentally influences how it learns and processes information.
	2.	Number of Epochs:
	•	An epoch is a full pass through the entire training dataset. Setting the number of epochs determines how many times the model sees the data during training. Think of it like repetition in practice; the more you repeat, the better you might get, but there’s a point where over-repetition can lead to diminishing returns (overfitting). Hence, choosing the right number of epochs is essential to balance learning and avoiding overfitting.
	3.	Batch Size:
	•	This is the number of samples the model processes before updating its internal parameters. Using a batch size is like working on a small set of problems before pausing to adjust your strategy. Larger batch sizes make training more stable, but they also require more memory and can lead to slower updates. Smaller batch sizes allow more frequent updates but might make training noisier.
	4.	Learning Rate/Schedule:
	•	The learning rate controls how large a step the model takes in the direction suggested by the optimizer for each update. A schedule can adjust this rate during training to make learning more efficient. Think of the learning rate like the sensitivity of a steering wheel; if it’s too high, you might overshoot the path, but if it’s too low, you take forever to get there. A schedule helps the model start with bigger steps and take smaller steps as it gets closer to an optimal solution.
	5.	Loss Function(s):
	•	The loss function is what the model is trying to minimize during training. It calculates the error between the model’s predictions and the actual target values. Choosing the correct loss function is like choosing the right metric for success. For instance, in a classification problem, cross-entropy loss might be appropriate, while for a regression task, mean squared error is more suitable.
    6. Why “Target Validation Error Rate” is Not Essential Before Training
       1. While it’s good to have a goal for validation error, this isn’t a parameter you set directly for the model. It’s more of a metric to evaluate performance after training. It’s like aiming for a specific exam score — you don’t set it beforehand; you measure it after you complete your preparation.、
 11. Compute Loss must come before Compute Gradients so that the model knows what it’s trying to minimize (the loss) before determining the directions (gradients) for updating the weights.
 12. Data Augmentation helps reduce variance by increasing the diversity of the training data, making the model more robust and better at generalizing to unseen data.
 13. I've trained a classifier on ImageNet and want to adapt it to classify models of cars. I have 5 examples each of 100 car models. What is a good strategy for adaption
     1.  Freeze the encoder and train a linear classification layer (linear probe) on the car dataset
     2.  Given the small number of samples, a linear classifier on features from a pre-trained model is likely to be most effective
 14. I've trained a classifier on ImageNet and want to adapt it to classify models of cars. I have 100 examples each of 100 car models. What is a good strategy for adaption?
     1.  Fine-tune the model on the car dataset
     2.  Given a moderate number of examples, fine-tuning is likely to be more effective.
11. The learning rate is the most sensitive parameter in fine-tuning with SGD and momentum because it directly controls the step size of updates.The learning rate is the most sensitive parameter in fine-tuning with SGD and momentum because it directly controls the step size of updates.
12. Character Tokenization: Ensures a unique representation for every string by treating each character as a separate token
    1.  Subword Tokenization: Provides a unique representation by splitting text into commonly used subwords but falls back to characters when necessary.
    2.  Word Tokenization: Limited by a fixed vocabulary and may use an unknown token for out-of-vocabulary words, which does not provide unique representations for all strings
13. 
    1.  Attention is flexible and allows for connections across the entire input sequence but does not enforce an inherent neighborhood structure. It’s mostly linear in computation but doesn’t depend strictly on input order without positional encoding.
    2.  Convolution is spatially structured, utilizing the same weights across positions (weight sharing) and relying on the neighborhood structure, which is essential for detecting spatially local features.
    3.  Linear layers connect every input to every output individually without assuming any neighborhood structure, and the computation is entirely linear.
