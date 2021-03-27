from Bio.Blast import NCBIWWW
import os

# 统计文件个数
path = 'D:\\blastfile\\cut'      # 输入文件夹地址
files = os.listdir(path)   # 读入文件夹
file_num = len(files)       # 统计文件夹中的文件个数

# 逐个进行blast
already_count = 0
while already_count < file_num:
    already_count += 1
    # 进行blast
    fasta_string = open("D:\\blastfile\\cut\\unigene-%s.fasta" % already_count).read()
    result_handle = NCBIWWW.qblast(
    "blastn",
    "nt",
    fasta_string,
    )

    # 保存结果
    save_file = open("D:\\blastfile\\result\\unigene-blastResult-%s.xml" % already_count, "w")
    save_file.write(result_handle.read())
    save_file.close()
    result_handle.close()

    print('unigene-%s blast已完成' % already_count)
