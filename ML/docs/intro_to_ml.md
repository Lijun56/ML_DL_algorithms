# Intro to Machine learning
## train 
 $\theta^* = argminLoss(f(X; \theta),y)$

in model($f(X; \theta)$), we input feature x_train and parameter $\theta$ to get y_predict, and together with y_train, target value, we put them into loss function. from there we adjust the parameter value try to minimize the loss function value. 

## predict
$y_pred = f(x_t, \theta)$
get y_predict by input x_test, and parameter to trained model
- in classification task :
  - y ouput as class or category in KNN
  - output as probability and used to determine 1|0 in logistic regression
- in regression task:
  - output as continous value(height, weight...)  

## Evaluation
| Metric   | Ideal For                          |
|----------|------------------------------------|
| Accuracy | Balanced classes                   |
| RMSE     | Regression (sensitive to large errors) |
| Precision| Reducing false positives           |
| Recall   | Reducing false negatives           |
| F1 Score | Balanced precision & recall        |
| AUC-ROC  | Discrimination on imbalanced data  |
### 1. Error and Accuracy
- **Error Rate**: Proportion of incorrect predictions.
- **Accuracy**: Proportion of correct predictions.
- **Use Case**: Good for balanced data but may be misleading for imbalanced datasets.

### 2. Root Mean Squared Error (RMSE) – For Regression
- **Formula**: $\text{RMSE} = \sqrt{\frac{1}{N} \sum (y - \hat{y})^2}$
- **Interpretation**: Measures the average magnitude of prediction errors, penalizing larger errors.
- **Use Case**: Regression tasks, especially when large errors are particularly impactful.

### 3. [Classification]Precision and Recall – For 
- **Precision**: \( \frac{TP}{TP + FP} \) – Focuses on accuracy of positive predictions.
  - *Use Case*: When false positives are costly.
- **Recall**: \( \frac{TP}{TP + FN} \) – Focuses on capturing all actual positives.
  - *Use Case*: When false negatives are costly.

### 4. F1 Score – Balancing Precision and Recall
- **Formula**: \( F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision + Recall}} \)
- **Interpretation**: Harmonic mean of precision and recall.
- **Use Case**: When a balance of precision and recall is desired.

### 5. [Classification]Area Under the ROC Curve (AUC-ROC) 
- **ROC Curve**: Plots True Positive Rate (Recall) vs. False Positive Rate.
- **AUC**: Area under the ROC curve, ranging from 0 to 1 (higher is better).
- **Use Case**: For assessing model discrimination, especially on imbalanced data.


## whole process
1.	**Define** Training, Validation, and Test Sets pairs:
    * The **training** set teaches the model.
    * The **validation** set is for fine-tuning the model.
    * The **test** set evaluates the final model’s performance.
2. **Select** Candidate **Models** and **Hyperparameters**: Hyperparameters are settings for the model that we adjust before training (like choosing the oven temperature and baking time).
3.	**Evaluate** Models:
Train and Validate: Train each candidate model on the training set and evaluate on the validation set.
Select the Best Model: The model with the best performance on the validation set is selected.
4.	**Final Testing**: Once the best model is chosen, we test it on a new dataset (test set) to see if it generalizes well to unseen data.
5.	**Cross-Validation**: Sometimes, instead of one validation set, we split data into multiple subsets to check if our model performs well across various data configurations.



## supervised and unsupervised

supervised training of model means the model requires labeled data during training
- for example: 

  •	k-NN and Naïve Bayes are supervised models because they require labeled data.
	•	k-Means is an unsupervised model because it doesn’t need labeled data.
















