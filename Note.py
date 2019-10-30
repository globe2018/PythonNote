PYTHON 写入list并换行的方法
f.writelines(lists) 是不换行的写入，可用以下方法在写入时换行。

方法一：
for line in lists:
f.write(line+'\n')

方法二：
lists=[line+"\n" for line in lists]
f.writelines(lists)

方法三：
f.write('\n'.join(lists))
