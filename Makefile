.PHONY: install train evaluate shap clean help

help:
	@echo "TopoAttention - available commands:"
	@echo "  make install    Install Python dependencies"
	@echo "  make train      Train the model"
	@echo "  make evaluate   Evaluate on test set"
	@echo "  make shap       Run SHAP interpretability analysis"
	@echo "  make clean      Remove cached outputs"

install:
	pip install -r requirements.txt

train:
	python code/train.py --config code/config.yaml

evaluate:
	python code/evaluate.py \
		--model Models/best_model.pt \
		--split splits/test_split.csv

shap:
	jupyter nbconvert --to notebook --execute \
		Analysis/shap_analysis.ipynb \
		--output Analysis/shap_analysis_executed.ipynb

splits:
	jupyter nbconvert --to notebook --execute \
		splitting_Models.ipynb \
		--output splitting_Models_executed.ipynb

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
