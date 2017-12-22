import os
import time
#  1.需要备份的文件与目录将被指定在一个列表中
source = ['"D:\\important"']
#  2.备份文件必须存储在一个主备份目录中
target_dir = 'E:\\backup'
#  3.如果目标目录不存在则创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
#  4.备份文件将被打包压缩为zip文件
#  5.将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
#  6.将当前时间作为zip文件的文件名
now = time.strftime('%H%M%S')
comment = input('Enter a comment:')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
#  如果目标目录不存在则进行创建
if not os.path.exists(today):
    os.mkdir(today)
    print('Successful create directory', today)
#  7.我们使用zip命令将文件打包
zip_command = 'zip -r -v {0} {1}'.format(target, ' '.join(source))
#  运行备份
print('zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('successful backup to', target)
else:
    print('backup FAILED')