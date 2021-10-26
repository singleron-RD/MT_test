#### Conda env

Path:/SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage/mt_lineage_r41.yml

    根据yml文件创建环境：conda env create -f  file.yml
    根据yml文件更新环境：conda env update <env_name> -f file.yml


#### Usage

Path: /SGRNJ03/randd/user/fuxin/PROJECTS/MT_lineage/MT_lineage


    python <script_path>/MT_lineage.py 
        --trans_directory   转录本分析路径
        --MT_directory   线粒体标准分析路径
        --outdir    输出文件路径
        --run_stat  Ture,统计Var,并画出HFV的heatmap图，默认False
        --run_lineage Ture,输入10x矩阵，进行seurat标准分析，并做出lineage tree,默认False(要执行这一步，需要输入 trans_directory)


eg.

统计HFV并画出AF的热图:

    python MT_lineage.py \
    --MT_directory /SGRNJ03/randd/RD20081701_SCOPEv2_Dynaseq/20211019_s/S_Poly_MT_9mito_1015 \
    --outdir /Personal/fuxin/dfuxin/PROJECTS/MT_lineage/res/test_pipline/S_Poly_MT_9mito_1015 \
    --run_stat True


