# biopy_blast
使用NCBI的接口批量blast

运行环境：
python3.6
biopython包

运行顺序：
1.biopy_cut_fasta
2.biopy_blast
3.biopy_analysis

程序功能：
biopy_cut_fasta：将包含多条核苷酸序列的fasta文件切成多个只含一条序列的fasta文件
biopy_blast：将多个fasta文件使用NCBI的接口进行批量blast，结果以xml格式保存
biopy_analysis：将单个xml文件进行解析，显示有用信息
