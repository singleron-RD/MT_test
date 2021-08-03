import logging
import subprocess
import time
import os
import sys
from datetime import timedelta
from functools import wraps
from collections import defaultdict

import pandas as pd
import pysam
import argparse


def add_log(func):
    '''
    logging start and done.
    '''
    logFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    module = func.__module__
    name = func.__name__
    logger_name = f'{module}.{name}'
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    
    fileHandler = logging.FileHandler("./log.txt")
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)
    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args and hasattr(args[0], 'debug') and args[0].debug:
            logger.setLevel(10)  # debug

        logger.info('start...')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        used = timedelta(seconds=end - start)
        logger.info('done. time used: %s', used)
        return result

    wrapper.logger = logger
    return wrapper

@add_log
def gen_bam(input_bam, outdir):
    prefix = os.path.basename(input_bam).strip('.bam')
    sort_bam = f'{outdir}/{prefix}.sorted.bam'
    cmd1 = (
        f'samtools sort -@ 5 '
        f'-o {sort_bam} '
        f'{input_bam} '
    )
    gen_bam.logger.info(cmd1)
    subprocess.check_call(cmd1, shell=True)
    cmd2 = (
        f'samtools index {sort_bam}'
    )
    gen_bam.logger.info(cmd2)
    subprocess.check_call(cmd2, shell=True)
    
    return sort_bam
    
@add_log
def parse_genelist(gene_list):
    gene_dict = defaultdict(dict)
    fh = open(gene_list, 'r')
    lines = fh.readlines()
    for line in lines:
        attrs = line.strip('\n').split('\t')
        gene = attrs[0]
        contig = attrs[1]
        start = attrs[2]
        stop = attrs[3]
        gene_dict[gene]['contig'] = contig
        gene_dict[gene]['start'] = int(start)
        gene_dict[gene]['stop'] = int(stop)
        
    return gene_dict
        
def count_coverage_depth(bam_file, contig_name, start_loc, stop_loc):
    bam = pysam.AlignmentFile(bam_file)
    coverage_array = bam.count_coverage(contig=contig_name, start=start_loc, stop=stop_loc)
    coverage_df = pd.DataFrame(coverage_array).T
    coverage_df = coverage_df.rename(columns={0: 'A', 1: 'C', 2: 'G', 3: 'T'})
    miss_loci_df = coverage_df[(coverage_df['A']==0)&(coverage_df['C']==0)&
                               (coverage_df['G']==0)&(coverage_df['T']==0)]
    ref_len = stop_loc-start_loc
    mapping_len = coverage_df.shape[0]-miss_loci_df.shape[0]
    coverage = mapping_len/ref_len
    sum_bases = sum(coverage_df.sum())
    depth = sum_bases/mapping_len
    
    return format(coverage, '.3f'), format(depth, '.2f')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gene_list', help='gene list, four cols split by tab. First col is gene name, second col is chr contig, third col is gene reference start loc, fourth col is gene reference stop loc', required=True)
    parser.add_argument('--bam_file', help='Aligned bam file from featurecounts', required=True)
    parser.add_argument('--outdir', help='output dir', default='./')
    args = parser.parse_args()
    gene_list = args.gene_list
    bam = args.bam_file
    outdir = args.outdir
    sort_bam = gen_bam(bam, outdir)
    gene_dict = parse_genelist(gene_list)
    res = open(f'{outdir}/gene_sum.tsv', 'w')
    res.write('gene\tcoverage\tdepth\n')
    for gene in gene_dict:
        contig = gene_dict[gene]['contig']
        start_loc = gene_dict[gene]['start']
        stop_loc = gene_dict[gene]['stop']
        gene_coverage, gene_depth = count_coverage_depth(sort_bam, contig, start_loc, stop_loc)
        coverage_ = float(gene_coverage)*100
        res.write(f'{gene}\t{coverage_}%\t{gene_depth}\n')
    res.close()
    
if __name__ == '__main__':
    main()
    
    

    
    