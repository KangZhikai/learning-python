#--coding:UTF-8--
print """
        在你前面有一间房子，在房子里面有三个房间分别是1号门，2号门,3号门,
   你有三个选择，分别选择三个不同的们在这三个门里面分别有着不同的东西。 
    """

door=raw_input(">")

if door=="1":
    print "在这个房间内有三个盒子，颜色分别是红色，蓝色，绿色，"
    print "这三个盒子中有一个盒子是有一把钥匙的，你通过该钥匙，"
    print "可以打开其他两个房间中的一个然后其他两个房间中的一个盒子，"
    print "你打开的盒子会有一些礼品要送给你，祝你好运"
    
    box=raw_input("请输入盒子颜色")
    
    if box=="红色":
        print "对不起，这里什么也没有！"
    elif box=="蓝色":
        print "恭喜你拿到了3号房间的钥匙"
    elif box=="绿色":
        print "你也许可以去2号房间看看"
    else:
        print "抱歉，你什么也没有做。"

elif door=="2":
    print "欢迎来到2号房间，这个房间是一个死亡房间，除非你在以下选项中进行选择，"
    print "请记住你只有两次机会"
    print "Apple"
    print "Banana"
    print "Orange"
    
    intimes=1
    choices=raw_input("请输入选项:")
    
    while intimes<2:
        if choices=="Apple":
            print "恭喜你，成功逃出2号房间"
            break
        elif choices=="Banana" or choices=="Orange":
            print "对不起，输入失败，请从新输入"
            choices_again=raw_input("请再次输入")
            if choices_again=="Apple":
                print "恭喜你，成功逃出2号房间"
                break
        else:
            print "请输入正确的选项"
        intimes=intimes+1
    else:
        print "超过输入次数！"
else:
    print "这是三号房间"