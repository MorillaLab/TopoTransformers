# Create the conda environment
conda env create -f environment.yml

# Activate the environment
conda activate topo_lung

# Verify installation
python -c "import numpy; import pandas; import gudhi; import giotto_tda; import phate; import shap; print('All packages loaded successfully!')"
