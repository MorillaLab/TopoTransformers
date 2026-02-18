# TopoAttention
[![License](https://img.shields.io/badge/License-GPLv3-green)](https://choosealicense.com/licenses/gpl-3.0/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/MorillaLab/TopoAttention/)
  
[Tran-Dinh et al. **Early Identification of High-Risk Individuals for Mortality after Lung Transplantation: A Retrospective Cohort Study with Topological Feature Engineering**. 2025. *medRxiv*.](https://www.medrxiv.org/content/10.1101/2025.10.01.25337124v1)👁️

Lung transplantation remains the only definitive treatment for patients with end-stage respiratory failure; however, it is burdened by a substantial risk of post-operative mortality. Current risk stratification methods, such as the Lung Transplant Risk Index, offer limited predictive performance and interpretability. This study introduces a novel predictive model based on topological transformers to assess mortality risk following lung transplantation. The objective is to improve predictive accuracy by capturing complex temporal patterns in clinical data while ensuring model interpretability to inform clinical decisions. 

A retrospective cohort study was conducted using clinical data from lung transplant recipients. The model integrates both static and time-dependent clinical variables through a transformer-based architecture that incorporates topological features derived from patients’ temporal trajectories. Model performance was compared to established methods using a held-out test set. The evaluation metrics included accuracy, sensitivity, specificity, and the area under the receiver operating characteristic curve. Model interpretability was assessed using Shapley Additive explanations to identify and rank the most influential predictors of mortality.

The proposed model demonstrated superior predictive performance compared to the Lung Transplant Risk Index and other benchmark models. On the test dataset, it achieved an accuracy of 87.4%, sensitivity of 84.1%, and specificity of 89.6%. The model consistently outperformed existing approaches across different subgroups, including age, underlying disease, and transplant type. Shapley-based interpretability analysis revealed that dynamic variables such as early post-operative oxygenation trends, immunosuppressive load, and inflammatory markers were among the most critical contributors to mortality risk.

The integration of topological features within a transformer-based framework significantly enhances the prediction of post-transplant mortality risk. By offering both improved predictive power and model transparency, this approach supports more precise and personalised risk stratification in lung transplantation. These findings highlight the potential of topological transformers as a valuable tool in the broader context of precision medicine and clinical decision support.


</div>

![TopoTransformers Schema](https://github.com/MorillaLab/TopoTransformers/blob/main/Figure_1.png)

<!-- ============================================== -->
<div align="left">
  <h1 id="citation">🎈 Citation</h1>
  <hr style="height: 3px; background: linear-gradient(90deg, #EF8E8D, #5755A3); border: none; border-radius: 3px;">
</div>

If you find TopoAttention model helpful, please cite us.

```bibtex
@article {Tran-Dinh2025.10.01.25337124,
	author = {Tran-Dinh, Alexy and Atchade, Enora and Tanaka, Sébastien and Lortat-Jacob, Brice and Castier, Yves and Mal, Hervé and Messika, Jonathan and Mordant, Pierre and Montravers, Philippe and Morilla, Ian},
	title = {Early Identification of High-Risk Individuals for Mortality after Lung Transplantation: A Retrospective Cohort Study with Topological Transformers},
	elocation-id = {2025.10.01.25337124},
	year = {2025},
	doi = {10.1101/2025.10.01.25337124},
	publisher = {Cold Spring Harbor Laboratory Press},
	URL = {https://www.medrxiv.org/content/early/2025/10/03/2025.10.01.25337124},
	eprint = {https://www.medrxiv.org/content/early/2025/10/03/2025.10.01.25337124.full.pdf},
	journal = {medRxiv}
}

```
