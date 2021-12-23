# Project Notes

## Optimize hyperparameters

In command line

```bash
mlflow run . \
-P steps=train_random_forest \
-P hydra_options="modeling.max_tfidf_features=10,15,30 modeling.random_forest.max_features=0.1,0.33,0.5,0.75,1 -m" 
```