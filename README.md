# Script
- path: /SGRNJ03/randd/zhouxin/mt_test

- script: mt_depth.py, new_coverage.py

# Feature

  - split aligned *.bam file.
  - caculate every gene coverage.
 
# input:
  - `--bam_file`, aligned bam file with CB tag.
  - `--gene_list`, which contains four columns. First col is gene name, second col is gene chromosome, third col is gene start locus, fourth col is gene stop locus. Separated by TAB.
  - `--barcodes`, barcodes file, one barcode occupied one line.

# output:
 - gene_sum.tsv, three columns. First col is gene name, second col is gene coverage, third col is mean depth for each base in gene.
 - *.sorted.bam, sorted bam file.
