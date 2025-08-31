Modeling Human Judgments of Argumentative Discourse Quality
This repository contains the data, code, and supplementary materials for the paper "Modeling Human Judgments of Argumentative Discourse Quality: A Comparative Analysis of LLMs and Human Raters in Academic Debates," submitted to the Dialogue & Discourse journal.

### 📝 Project Overview
This research investigates the extent to which modern Large Language Models (LLMs) can replicate the complex, subjective task of evaluating argumentative discourse quality. The study conducts a systematic, multi-metric comparison between three state-of-the-art LLMs and two distinct human-derived benchmarks.

The core of this work is to explore:

The alignment of LLM-generated rankings with those from expert human judges.

The alignment of LLM rankings with the perceptions of the debate participants themselves.

The impact of different model architectures (GPT-4o, Gemini 1.5 Pro, Claude 3 Opus) and prompting strategies on the evaluation outcomes.

### 🗃️ Datasets: DEBISS and DEBISS-eval
This study leverages two key resources:

DEBISS Corpus: A previously published corpus of 16 semi-structured academic debates in Brazilian Portuguese, which includes participant self-assessment data.

DEBISS-eval: The primary contribution of this work, a new public benchmark featuring multi-faceted, granular evaluations of the DEBISS corpus from five expert human judges.

Together, these resources provide the foundation for a rigorous, multi-perspective analysis of automated discourse evaluation.

### 📂 Repository Structure
/debates: Contains the 16 .csv files with the original debate transcriptions from the DEBISS corpus.

/prompts: Contains the 4 .txt files with the full text of the prompts used in the LLM experiments.

/outputs: The target directory where the JSON results from the LLM test battery are saved.

/DEBISS-eval: Contains all data from the generation of DEBISS-eval

And the Jupyter Notebooks used to:

Process the raw human evaluation data into final ground truth ranking files.

Read and aggregate the LLM outputs.

Calculate all performance metrics and generate the final result tables.

The main Python script to run the full test battery with the three LLMs.

### 🚀 How to Replicate the Experiments

Prerequisites

Python 3.9+

### 📈 Key Findings

Our results demonstrate that LLMs can replicate the holistic quality rankings of expert judges with exceptionally high fidelity (NDCG > 0.90). We also identified distinct model "personalities": Gemini showed the strongest performance in identifying the winner chosen by judges, Claude aligned most closely with participant perceptions, and GPT-4o was the most precise in assigning the exact rank to each debater.

###🎓 Citation

If you use the resources from this work, please cite both the original DEBISS corpus paper and the present study.

For the DEBISS Corpus:


```

@inproceedings{souza2025debiss,
  title     = {{DEBISS}: A Corpus of Individual, Semi-structured and Spoken Debates},
  author    = {de Souza, Klaywert and Pereira, David and Vasconcelos, Larissa Lucena and Campelo, Cláudio Elízio Calazans},
  booktitle = {Proceedings of the Symposium in Information and Human Language Technology (STIL)},
  year      = {2025},
  publisher = {Brazilian Computer Society (SBC)},
  address   = {[Conference Location], Brazil}
}

```

For this study:

```

@article{souza2025modeling,
  title   = {Modeling Human Judgments of Argumentative Discourse Quality: A Comparative Analysis of LLMs and Human Raters in Academic Debates},
  author  = {de Souza, Klaywert Danillo Ferreira and Campelo, Cláudio Elízio Calazans},
  journal = {Dialogue \& Discourse},
  year    = {2025},
  note    = {Under review}
}

```
🙏 Acknowledgments
This work was supported by the Coordination for the Improvement of Higher Education Personnel (CAPES) and developed at the Laboratory of Applied Intelligent Computing (LACINA) at UFCG.
