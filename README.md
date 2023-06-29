# ALS Progression Analysis Using Principal Tree-based Model

Welcome to the repository dedicated to our research titled "Mapping ALS Progression and Comorbidity Interactions: Insights from a Principal Tree-Based Model." We aim to shed light on the disease progression of ALS using Elastic Principle Trees.

This repository consists of a collection of Jupyter notebooks that are expected to be run in sequential order. Each notebook serves a unique purpose in the data processing pipeline and is briefly described below:

1. `transform.ipynb`: This notebook focuses on initial data preprocessing and transformation. It requires the raw data, which should be placed in the `data/` directory, to function correctly.
2. `tree.ipynb`: Here, we compute the elastic principle tree and encapsulate it within a `Networkx DiGraph`, which forms the core of our ALS progression mapping.
3. `locate.ipynb`: This notebook helps identify diseases that show an increase during state transitions, as represented by the tree edges in our model.
4. `categorize.ipynb`: Finally, based on the insights gathered from the above steps, this notebook helps categorize patients according to their disease trajectories.

These notebooks contribute to our comprehensive exploration and visualization of ALS progression and its comorbidity interactions. We hope that our research aids in improving the understanding of this devastating disease and potentially contribute to its treatment in the future.
Feel free to delve into each notebook for a closer look at our methodology and findings. For any queries or suggestions, you can reach out to us via the contact information provided.