# import numpy as np

with open('tsv_as_txt.txt', 'r') as f:
    detailed = f.readlines()

# with open('condensed_clusters.txt', 'r') as f:
#     condensed = f.readlines()

# num_clusters = 502235 # wc -l condensed_clusters.txt
# num_contigs = 201476 # grep \> ~/FASTA_datasets/Combined_fasta.fsa_nt | wc -l 

# for line in condensed:
#     cluster_size, cluster_label = line.strip().split(' ')
#     cluster_size = int(cluster_size)

cluster_dictionary = {}

for line in detailed:
    label, member = line.strip().split('\t')
    if label in cluster_dictionary.keys():
        cluster_dictionary[label].append(member)
    else:
        cluster_dictionary[label] = [member]

with open('cluster_dictionary.txt', 'w+') as f:
    for key, value in cluster_dictionary.items():
        list_str = ''
        for i in value:
            list_str += i + ','
        f.write(f'{key}: {list_str}\n')
