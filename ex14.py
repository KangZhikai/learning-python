#--coding:utf-8--
#����һ����ͼ����
states={
        '����':'BJ',
        '���':'TJ',
        '�Ϻ�':'SH',
        '����':'CQ'}

cities={
        'BJ':'����',
        'TJ':'���',
        'SH':'�Ϻ�',
        'CQ':'����'}

cities['XM']='����'
cities['SZ']='����'

#���һЩ����
print "-"*10
print "BJ������ǣ�",cities['BJ']
print "SH������ǣ�",cities['SH']

#������д���
print "-"*10
print "�Ϻ��Ĵ����ǣ�",states['�Ϻ�']
print "����Ĵ����ǣ�",states['����']
print "���Ĵ����ǣ�",states['���']

#���ȫ���ĳ��д���
print "*"*10
for state,abberv in states.items():
    print "%s ���������� %s"%(state,abberv)

#���ȫ�����е�һЩ����
print "#"*10
for abberv,state in cities.items():
    print "%s ���д����� %s"%(abberv,state)
