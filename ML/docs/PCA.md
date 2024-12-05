# PCA(embedding) and Clustering
PCA and clustering address two distinct but related challenges in data analysis
* PCA or embedding is one of  demensionality reduction technique, reducing the number of features, capturing the most important patterns in a few dimensions.
* Clustering is grouping similar data points (K-means)

PCA reduced dimension by linear projection
  * preserve variance of data points 
  * not preseve local connectivity structure or discriminative infomation

Other demensionality reduction methods
  - MDS: preserve pairwise distances
  - IsoMap: MDS but using a graph-based distance
  - t-SNE: preserve a probabilistic distribution of
  neighbors for each point (also focusing on closest
  points)
  - UMAP: incorporates k-nn structure, spectral
  embedding, and more to achieve good embeddings
  relatively quickly