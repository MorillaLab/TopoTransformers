#!/usr/bin/env python3
"""
Main entry point for lung transplantation mortality prediction analysis
"""

import argparse
import yaml
import numpy as np
import pandas as pd
from pathlib import Path
import joblib
import warnings
warnings.filterwarnings('ignore')

def parse_args():
    parser = argparse.ArgumentParser(description='Run topological lung transplantation analysis')
    parser.add_argument('--config', type=str, default='config.yaml', help='Configuration file')
    parser.add_argument('--synthetic', action='store_true', help='Use synthetic data')
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    parser.add_argument('--cv-folds', type=int, default=5, help='Number of CV folds')
    parser.add_argument('--quick', action='store_true', help='Quick run (fewer iterations)')
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Override with command line arguments
    if args.seed:
        config['data']['random_seed'] = args.seed
    if args.cv_folds:
        config['data']['cv_folds'] = args.cv_folds
    
    # Set random seed
    np.random.seed(config['data']['random_seed'])
    
    print("=" * 60)
    print("TOPOLOGICAL LUNG TRANSPLANTATION ANALYSIS")
    print("=" * 60)
    print(f"Configuration: {config['model']['type']} model")
    print(f"Random seed: {config['data']['random_seed']}")
    print(f"CV folds: {config['data']['cv_folds']}")
    print("=" * 60)
    
    # Create output directories
    Path(config['output']['figures_dir']).mkdir(parents=True, exist_ok=True)
    Path(config['output']['tables_dir']).mkdir(parents=True, exist_ok=True)
    Path(config['output']['models_dir']).mkdir(parents=True, exist_ok=True)
    Path(config['output']['supplementary_dir']).mkdir(parents=True, exist_ok=True)
    
    # Your analysis code here
    # This would import and run your actual analysis modules
    
    print("\n✅ Analysis complete!")
    print(f"Results saved to: outputs/")

if __name__ == "__main__":
    main()
