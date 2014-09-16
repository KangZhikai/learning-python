#--coding:utf-8--
#创建一个地图索引
states={
        '北京':'BJ',
        '天津':'TJ',
        '上海':'SH',
        '重庆':'CQ'}

cities={
        'BJ':'北京',
        'TJ':'天津',
        'SH':'上海',
        'CQ':'重庆'}

cities['XM']='厦门'
cities['SZ']='深圳'

#输出一些城市
print "-"*10
print "BJ代表的是：",cities['BJ']
print "SH代表的是：",cities['SH']

#输出城市代码
print "-"*10
print "上海的代码是：",states['上海']
print "重庆的代码是：",states['重庆']
print "天津的代码是：",states['天津']

#输出全部的城市代码
print "*"*10
for state,abberv in states.items():
    print "%s 代码代表的是 %s"%(state,abberv)

#输出全部城市的一些代码
print "#"*10
for abberv,state in cities.items():
    print "%s 城市代码是 %s"%(abberv,state)
