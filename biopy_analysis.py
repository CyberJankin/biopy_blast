from Bio.Blast import NCBIXML

# 解析
result_handle = open("D:\\blastfile\\result\\unigene-blastResult-1.xml")
blast_record = NCBIXML.read(result_handle)

# 打印出所有大于某一特定阈值的BLAST命中结果的一些汇总信息
E_VALUE_THRESH = 0.04

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')
