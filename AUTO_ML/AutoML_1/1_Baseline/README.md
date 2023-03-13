# Summary of 1_Baseline

[<< Go back](../README.md)


## Baseline Classifier (Baseline)
- **n_jobs**: -1
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

0.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.552173 |  nan        |
| auc       | 0.5      |  nan        |
| f1        | 0.388332 |    0.216757 |
| accuracy  | 0.24095  |    0.216757 |
| precision | 0.24095  |    0.216757 |
| recall    | 1        |    0.216757 |
| mcc       | 0        |    0.216757 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.552173 |  nan        |
| auc       | 0.5      |  nan        |
| f1        | 0.388332 |    0.216757 |
| accuracy  | 0.24095  |    0.216757 |
| precision | 0.24095  |    0.216757 |
| recall    | 1        |    0.216757 |
| mcc       | 0        |    0.216757 |


## Confusion matrix (at threshold=0.216757)
|                  |   Predicted as <=50K |   Predicted as >50K |
|:-----------------|---------------------:|--------------------:|
| Labeled as <=50K |                    0 |                4634 |
| Labeled as >50K  |                    0 |                1471 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
