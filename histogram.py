from matplotlib import pyplot as plt

with open('condensed_clusters.txt', 'r') as f:
    lines = f.readlines()

sizes = []
for line in lines:
    stripped = line.strip()
    num_str = stripped[:stripped.rindex('V') - 1]
    sizes.append(int(num_str))

print(sizes)
plt.hist(sizes)
plt.yscale('log')
plt.ylabel('Frequency')
plt.xlabel('Cluster Size')
plt.title('Cluster Size Histogram')
plt.savefig('cluster_size_histogram_FINAL')
