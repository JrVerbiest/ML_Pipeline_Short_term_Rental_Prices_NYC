# Best model

**Optimize hyperparameters**

In command line run:

```bash
mlflow run . \
-P steps=train_random_forest \
-P hydra_options="modeling.max_tfidf_features=10,15,30 modeling.random_forest.max_features=0.1,0.33,0.5,0.75,1 -m" 
```



**My Best Model**

![best_model](/home/joeri/Documents/GitHub/nd0821-c2-build-model-workflow-starter/images/best_model.png)

| Metric |           |
| ------ | --------- |
| r2     | 0.549351  |
| mea    | 33.416015 |

