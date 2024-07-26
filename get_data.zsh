wget https://sra-download.ncbi.nlm.nih.gov/traces/wgs01/wgs_aux/VM/HT/VMHT01/VMHT01.1.fsa_nt.gz
wget https://sra-download.ncbi.nlm.nih.gov/traces/wgs01/wgs_aux/VM/HT/VMHT01/VMHT01.2.fsa_nt.gz
wget https://sra-download.ncbi.nlm.nih.gov/traces/wgs01/wgs_aux/VM/HT/VMHT01/VMHT01.3.fsa_nt.gz
wget https://sra-download.ncbi.nlm.nih.gov/traces/wgs01/wgs_aux/VM/HT/VMHT01/VMHT01.5.fsa_nt.gz

gunzip VMHT*
cat VMHT* > Combined_FASTA.fsa_nt
