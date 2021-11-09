### Introduction

Compute the mean UMI count for each gene.

### Conda env

    conda activate mt_lineage

### Path

    /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage

### Usage

    Rscript <script_path>/meanCount_per_gene.R \
        --rds   Seurat object in rds format.
        --outdir    Directory of output files, current directory by default.

    e.g.
    Rscript /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/meanCount_per_gene.R \
    --rds   /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/res/20211029_mito/Poly_MT_11mito_102/Poly_MT_11mito_102.rds \
    --outdir    /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/res/20211029_mito/Poly_MT_11mito_102
