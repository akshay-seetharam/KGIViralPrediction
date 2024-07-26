# KGIViralPrediction
This repository contains all the code that ended up being useful for predicting novel viruses as part of my research work at Keck Graduate Institute in the summer of 2024.

Dependencies:
- mmseqs2 (for clustering)
- prodigal (for gene finding)
- matploblib (for post-processing with .ipynb, otherwise unnecessary)

Order of battle:
1. get_data.zsh
2. prodigal.zsh
3. mmseqs.zsh
4. contig_dict_creator.py
5. cluster_dict_creator.py
6. Notebooks
