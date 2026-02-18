"""Verify that all required packages are installed correctly"""

import sys
import importlib

required_packages = [
    'numpy',
    'pandas',
    'scipy',
    'sklearn',
    'statsmodels',
    'matplotlib',
    'seaborn',
    'plotly',
    'gudhi',
    'phate',
    'giotto_tda',
    'shap',
    'imblearn',
    'xgboost',
    'lightgbm',
    'catboost',
    'jupyter',
    'tqdm',
    'joblib',
    'yaml',
    'optuna',
    'missingno',
    'yellowbrick',
    'dython'
]

print("Checking environment...\n")
all_good = True

for package in required_packages:
    try:
        module = importlib.import_module(package)
        version = getattr(module, '__version__', 'unknown')
        print(f"✅ {package:20} {version}")
    except ImportError as e:
        print(f"❌ {package:20} NOT FOUND - {e}")
        all_good = False

print("\n" + "="*50)
if all_good:
    print("✅ All packages installed successfully!")
else:
    print("❌ Some packages are missing. Please check the errors above.")
print("="*50)
