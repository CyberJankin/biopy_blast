# biopy_blast
使用NCBI的接口批量比对核苷酸序列

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

解析的结果：  
解析的结果可以分为三大类，调用不同的类可以得到相应的信息：descriptions、 alignments、 multiple_alignment。其中 descriptions 和 alignments 都是以 list 的形式来存储数据的。  
· descriptions 下面有四个信息： title、 score、 e、 num_alignments，分别对应数据库中匹配上的序列的标题、匹配的得分、匹配的 e-value、以及多序列比对的数目。  
· aligments 下面有三个信息： title、 length、 hsps，分别对应数据库中匹配上的序列的标题、匹配的长度、其中 hsps 是 list 格式的对象，里面储存了 query 和数据库中序列匹配的具体信息，包括匹配得分、 gap 等信息，详细的内容在后面的图片里。  
· multiple_alignment 是多序列比对的结果，里面只储存了 alignment 的信息。有了这些具体的方法，在处理 blast 的结果时就不需要写额外的脚本了，只需要提取相关的记录然后进行具体操作就可以了。

