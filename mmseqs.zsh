mmseqs createdb Combined_FASTA.fsa_nt marine_db
mmseqs createdb GoodContigs.txt red_queen_db
mmseqs search red_queen_db marine_db result_db tmp -s 0.8 --search-type 3 --max-accept 50

python3 contig_dict_creator.py
python3 cluster_dict_creator.py
