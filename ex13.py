#--coding:UTF-8--
print """
        ����ǰ����һ�䷿�ӣ��ڷ�����������������ֱ���1���ţ�2����,3����,
   ��������ѡ�񣬷ֱ�ѡ��������ͬ������������������ֱ����Ų�ͬ�Ķ����� 
    """

door=raw_input(">")

if door=="1":
    print "��������������������ӣ���ɫ�ֱ��Ǻ�ɫ����ɫ����ɫ��"
    print "��������������һ����������һ��Կ�׵ģ���ͨ����Կ�ף�"
    print "���Դ��������������е�һ��Ȼ���������������е�һ�����ӣ�"
    print "��򿪵ĺ��ӻ���һЩ��ƷҪ�͸��㣬ף�����"
    
    box=raw_input("�����������ɫ")
    
    if box=="��ɫ":
        print "�Բ�������ʲôҲû�У�"
    elif box=="��ɫ":
        print "��ϲ���õ���3�ŷ����Կ��"
    elif box=="��ɫ":
        print "��Ҳ�����ȥ2�ŷ��俴��"
    else:
        print "��Ǹ����ʲôҲû������"

elif door=="2":
    print "��ӭ����2�ŷ��䣬���������һ���������䣬������������ѡ���н���ѡ��"
    print "���ס��ֻ�����λ���"
    print "Apple"
    print "Banana"
    print "Orange"
    
    intimes=1
    choices=raw_input("������ѡ��:")
    
    while intimes<2:
        if choices=="Apple":
            print "��ϲ�㣬�ɹ��ӳ�2�ŷ���"
            break
        elif choices=="Banana" or choices=="Orange":
            print "�Բ�������ʧ�ܣ����������"
            choices_again=raw_input("���ٴ�����")
            if choices_again=="Apple":
                print "��ϲ�㣬�ɹ��ӳ�2�ŷ���"
                break
        else:
            print "��������ȷ��ѡ��"
        intimes=intimes+1
    else:
        print "�������������"
else:
    print "�������ŷ���"