# Model Card: Topological Lung Transplantation Mortality Predictor

## Model Details
- **Model Name**: TopoAttention-v1.0
- **Version**: 1.0.0
- **Date**: March 1, 2025
- **Model Type**: Multi-Layer Perceptron with topological feature extraction
- **Input Features**: 76 (49 clinical + 27 topological)
- **Output**: Probability of 1-year mortality (0-1)

### Architecture
```python
{
    "input_dim": 76,
    "hidden_layers": [64, 32],
    "activation": "ReLU",
    "output_activation": "Sigmoid",
    "dropout": 0.2,
    "l2_regularization": 0.01,
    "optimizer": "Adam (lr=0.001)",
    "batch_size": 32,
    "epochs": 200,
    "early_stopping_patience": 10
}
