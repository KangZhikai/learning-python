#--coding:utf-8--
#�ҵ����ļ��е���ĸ
file=open('date.txt')
ans=''
tmp=file.read()

for c in tmp:
    if c.isalpha():
        ans+=c
print ans