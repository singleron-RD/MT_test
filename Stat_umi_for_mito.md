### Introduction
Count the average UMI count of each gene.

### Conda env
conda activate mt_lineage

### Path

    Scrirpt:/SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/Stat_umi_for_mito.py
    Test:/SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/test_Stat_umi_for_mito

### Usage

    python <script_path>/Stat_umi_for_mito.py \
        --MT_directory  The directory of standard mitochondrial analysis.
        --trans_directory The directory of standard transcriptome analysis.
        --outdir    The directory of output files.
    
    e.g.
        python /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/Stat_umi_for_mito.py \
        --trans_directory /SGRNJ03/randd/RD20081701_SCOPEv2_Dynaseq/20211029/mito_MT_trans \
        --MT_directory /SGRNJ03/randd/RD20081701_SCOPEv2_Dynaseq/20211115/PBMC_mitoMT_7mito_1109 
        --outdir /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/test_Stat_umi_for_mito
