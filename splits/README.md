# Split Manifest for Nested Cross-Validation

## Overview
This directory contains the split assignments for the 5-fold nested cross-validation used in the study.

## Files
- `split_manifest.csv`: Complete manifest with all patients and their fold assignments
- `split_summary.csv`: Summary counts by fold

## Manifest Columns
- `patient_id`: Anonymous patient identifier
- `outcome`: 0 = survivor, 1 = non-survivor
- `outer_fold`: Outer fold number (1-5) for test set assignment
- `inner_fold`: Inner fold number (1-3) for validation set assignment within training data
- `train_val_test`: Overall assignment type
- `fold_X_assignment`: Assignment for each specific fold (train/validation/test)

## Usage
To reproduce the exact splits:
```python
import pandas as pd
manifest = pd.read_csv('split_manifest.csv')

# For fold 1 test set
test_fold1 = manifest[manifest['fold_1_assignment'] == 'test']

# For fold 1 training set
train_fold1 = manifest[manifest['fold_1_assignment'] == 'train']

# For fold 1 validation set
val_fold1 = manifest[manifest['fold_1_assignment'] == 'validation']
```
