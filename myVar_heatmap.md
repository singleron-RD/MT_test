### Introduction

Plot heatmap for allele frequency of custom variations in specific cells.

### Conda env

    conda activate mt_lineage

### Path

    Script: /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage
    Test: /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/test_myVar_heatmap

### Usage

    Rscript <script_path>/myVar_heatmap.R \
        --MT_directory  The directory of standard mitochondrial analysis.
        --rds   The seurat object of TSNE/UMAP obtained afterseurat analysis of the corresponding transcript.
        --outdir    The directory of output files.
        --myvar File of custom variation list(VID), required.
        --mycell    File of custom cell list(CID), default all.
    
    e.g.
        Rscript /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/myVar_heatmap.R \
        --MT_directory /SGRNJ03/randd/RD20081701_SCOPEv2_Dynaseq/20211029_mito/mito_MT_11mito \
        --rds /Personal/fuxin/dfuxin/PROJECTS/MT_lineage/res/20211029_mito/mito_MT_11mito/mito_MT_11mito.rds \
        --outdir /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/test_myVar_heatmap \
        --myvar /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/test_myVar_heatmap/var.list
