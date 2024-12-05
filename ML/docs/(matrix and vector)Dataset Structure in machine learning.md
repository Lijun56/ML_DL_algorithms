# (matrix and vector) Dataset Structure in machine learning

We have a dataset$X$where:
- Each row represents a sample; each column represents a kind of feature
- $X_{nm}$ or $X_m^n$ sis a matrix of size $n\times m$, (n rows $\times$ m cols)where $n$ is the number of samples, and $m$ is the number of features.
- $x_j^i$ \: The $j$-th feature of the $i$-th sample, $j$th column of $i$th row
- $y$: The label vector, where $y^i$ represents the label of the $i$-th sample.

In summary:

$
X = \begin{bmatrix} x_1^1 & x_2^1 & \cdots & x_m^1 \\ x_1^2 & x_2^2 & \cdots & x_m^2 \\ \vdots & \vdots & \ddots & \vdots \\ x_1^n & x_2^n & \cdots & x_m^n \end{bmatrix}, \quad y = \begin{bmatrix} y^1 \\ y^2 \\ \vdots \\ y^n \end{bmatrix}
$

## Example: Iris Dataset
The dataset includes features such as:
- $x_1$: feature ,Sepal length
- $x_2$: feature ,Sepal width
- $x_3$: feature ,Petal length
- $x_4$: feature ,Petal width
- $y$: Target , Label indicating the species type (e.g., Setosa, Versicolor, Virginica)

| sample       | Sepal Length | Sepal Width | Petal Length | Petal Width | Label       |
|-----------------|--------------|-------------|--------------|-------------|-------------|
|$x^1$    | 5.1          | 3.5         | 1.4          | 0.2         | Setosa      |
|$x^2$    | 7.0          | 3.2         | 4.7          | 1.4         | Versicolor  |
|$x^3$    | 6.3          | 3.3         | 6.0          | 2.5         | Virginica   |

The dataset can be represented as a matrix $X$ in the following format:

$X^1 = \begin{bmatrix} 5.1 \\ 3.5 \\ 1.4 \\ 0.2 \end{bmatrix}$,
$(X^1)^T = \begin{bmatrix} 5.1 & 3.5 & 1.4 & 0.2 \end{bmatrix}$

with$X^T$representing the entire dataset(in transposed form, **numpy standard**):

$X^T = \begin{bmatrix} (x^1)^T \\ (x_2)^T \\ (x_3)^T \end{bmatrix}$, numpy using this way of expression

## Feature Space Representation
Each feature in $X$ can be visualized as an axis in a multidimensional space (feature space). 

Each sample corresponds to a point in this space, with coordinates defined by its feature values.

* For a 2 demension case: $\text{Feature space:}\quad (x_1, x_2)$

where each sample is a data point in the feature space.

Features can be abstract and represent data in multiple dimensions. High-dimensional feature space represents data with multiple features.

### Example: MNIST Dataset
- MNIST images: $28 \times 28$ pixels, resulting in $784$ features (one for each pixel).
- Each pixel represents a feature.
- If the image is grayscale, data size = $784$.
- For color images, data size would be larger (more features per pixel).

## Classification and Regression (Supervised Learning)

### Classification
- Goal: Predict a **label**.
- Types:
  - **Binary Classification**: Two possible labels (e.g., dog or cat, approve or reject).
  - **Multi-Class Classification**: More than two possible labels (e.g., grade classifications, letter grades like A, B, C, D).
    - Some algorithms only support binary classification.
    - Multi-class classifiers can often be adapted for binary classification and vice versa.
    - Some algorithms support both binary and multi-class classification.

### Regression
- Goal: Predict a **continuous value**, not a label.
- Examples: Stock price prediction, grade prediction, market analysis.
- Notes:
  - Some algorithms are designed exclusively for classification or regression.
  - Others are capable of performing both.

### Transfer Between Classification and Regression
- **Regression to Binary**: Regression results can be used in binary decision-making contexts.
- **Self-driving Example**: Predicting the angle of direction based on continuous data (regression).
- **Grade Example**: Converting numerical student grades to letter grades like A, B, C, D (classification).



