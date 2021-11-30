#### Introduction
研究证明单细胞测序可以用于研究线粒体中的体细胞突变，并根据这些突变寻找细胞间的种系关系。
此脚本用于统计celescope标准分析后，线粒体测序样本中高频突变的分布以及比较基于转录本测序后TSNE分群与基于线粒体突变构建的进化树的对应情况

#### Conda env

    conda activate mt_lineage

#### Usage

Path: /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage


    python <script_path>/MT_lineage.py 
        --trans_directory   转录本分析路径
        --MT_directory   线粒体标准分析路径
        --outdir    输出文件路径
        --run_stat  True,统计Var,并画出HFV的heatmap图，默认False
        --run_lineage True,输入10x矩阵，进行seurat标准分析，并做出lineage tree,默认False(要执行这一步，需要输入 trans_directory)
        --germline_threshold    max_genotype_cell_number / covered_cell_number <= germline_threshold, default=0.95
        --coverage_threshold    covered_cell_number / total_cell_number >= coverage_threshold, default=0.9


eg.

统计HFV并画出AF的热图:

    python /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/MT_lineage.py \
    --MT_directory /SGRNJ03/randd/RD20081701_SCOPEv2_Dynaseq/20211019_s/S_Poly_MT_9mito_1015 \
    --outdir /Personal/fuxin/dfuxin/PROJECTS/MT_lineage/res/test_pipline/S_Poly_MT_9mito_1015 \
    --run_stat True \
    --run_lineage True \
    --germline_threshold 0.99 \
    --coverage_threshold 0.5
 
 Note:
 
 当cluster数大于16时，会报错。


