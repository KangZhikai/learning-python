#--coding:utf-8--
#找到该文件中的字母
file=open('date.txt')
ans=''
tmp=file.read()

for c in tmp:
    if c.isalpha():
        ans+=c
print ans