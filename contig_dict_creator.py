contig_dict = {}

with open('tsv_as_txt.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    label, member = line.strip().split('\t')
    contig = member[:member.index('_')]
    if contig in contig_dict.keys():
        contig_dict[contig].append(label)
    else:
        contig_dict[contig] = [label]

import json
with open('contig_dict.json', 'w+') as fp:
    json.dump(contig_dict, fp)

with open('contig_dict.txt', 'w+') as f:
    for key,value in contig_dict.items():
        list_str = ''
        for i in value:
            list_str += i + ','
        f.write(key + ": " + list_str + '\n')

sizes = [len(i) for i in contig_dict.values()]

from matplotlib import pyplot as plt
plt.hist(sizes)
plt.title('Number of Clusters Present in Each Contig')
plt.ylabel('Frequency')
plt.xlabel('# of Clusters')
plt.yscale('log')
plt.savefig('contig_cluster_frequency_hist.png')
