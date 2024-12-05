# [clf, reg]KNN(K nearest neighbor)
## how it works
map->sort->vote
[click for classifier interactive visualization](http://vision.stanford.edu/teaching/cs231n-demos/knn/)

(in regression task) map -> sort ->find mean value 

## math

Map over X_train data to find cloest element's index, y is value of that element, in KNN, it need to find k elements instead of one here

$i^* = argminDistance(X_{train}[i], x_{test})$

$y^* = y_{train}[i^*]$

## Strengths:
**Low bias** (can represent complex boundaries with sufficient data).

**No training time** since it simply stores the training data.
Simple and widely applicable.

Limitations:
**Relies on well-defined input features**.
**Slow** for predictions in its basic form, especially with large datasets