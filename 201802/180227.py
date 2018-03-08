# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'


# 利用字符串和列表将两个通讯录文本合并为一个文本
def main():
    ftele1 = open('180227data2-TeleAddressBook.txt', 'rb')
    ftele2 = open('180227data2-EmailAddressBook.txt', 'rb')

    ftele1.readline()  # 跳过第一行
    ftele2.readline()
    lines1 = ftele1.readlines()
    lines2 = ftele2.readlines()
    print("lines1是：", lines1)
    # for line in ftele1:
    #     print(str(line.decode('gbk')))
    # print("\n《邮件簿》如下：")
    # for line in ftele2:
    #     print(str(line.decode('gbk')))


    list1_name = []
    list1_tele = []
    list2_name = []
    list2_email = []

    print("lines1是：", lines1)
    for line in lines1:  # 获取第一个文本中的姓名和电话信息
        elements = line.split()
        list1_name.append(str(elements[0].decode('gbk')))
        list1_tele.append(str(elements[1].decode('gbk')))  # 将文本读出来的bytes转换为str类型
    print("11111", list1_name)
    for line in lines2:  # 获取第二个文本中的姓名和邮件信息
        elements = line.split()
        list2_name.append(str(elements[0].decode('gbk')))
        list2_email.append(str(elements[1].decode('gbk')))
    print("22222", list2_email)
    ###开始处理###
    lines = []
    lines.append('姓名\t    电话   \t  邮箱\n')

    # 按索引方式遍历姓名列表1
    for i in range(len(list1_name)):
        s = ''
        if list1_name[i] in list2_name:
            j = list2_name.index(list1_name[i])  # 找到姓名列表1对应列表2中的姓名索引位置
            s = '\t'.join([list1_name[i], list1_tele[i], list2_email[j]])
            s += '\n'
        else:
            s = '\t'.join([list1_name[i], list1_tele[i], str('   -----   ')])
            s += '\n'
        lines.append(s)

    # 处理姓名列表2中剩余的姓名
    for i in range(len(list2_name)):
        s = ''
        if list2_name[i] not in list1_name:
            s = '\t'.join([list2_name[i], str('   -----   '), list2_email[i]])
            s += '\n'
        lines.append(s)

    print("\n新生成的数据为：")
    for line in lines:
        print(line)

    ftele3 = open('AddressBook-ref.txt', 'w')
    ftele3.writelines(lines)

    ftele3.close()
    ftele1.close()
    ftele2.close()

    print("The addressBooks are merged!")


if __name__ == "__main__":
    main()
