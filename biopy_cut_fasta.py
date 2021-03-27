# 选出每条核苷酸数据，截取成单独的文件
# 1 Open
file_read = open("D:\\blastfile\\unigene-10.fasta")
file_write = open("D:\\blastfile\\unigene-0.fasta", "w") # 第0个文档应当为空

# 2 Read, Write
keyword = '>'
keyword_count = 0

while True:
    text = file_read.readline()
    keyword_count += text.count(keyword)  # count()方法计数,keyword为传入的关键字(字符串)

    if text == '':
        break

    if text.count(keyword) != 0:
        file_write.close()
        file_write = open("D:\\blastfile\\cut\\unigene-%s.fasta" % keyword_count, "w")
        file_write.write(text)
    else:
        file_write.write(text)

# 3 Close
file_read.close()
file_write.close()
print("截取完成")
