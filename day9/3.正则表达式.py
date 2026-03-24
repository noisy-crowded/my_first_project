import re

def simple_use():
    result = re.match("wangdao", "wangdao.cn")
    if result:
        print(result.group())

def single_use():
    """
    匹配单个字符
    :return:
    """
    ret = re.match(".", "M")
    print(ret.group())
    ret = re.match("t.o", "too")
    print(ret.group())
    ret = re.match("t.o", "two")
    print(ret.group())
    print('-'*50)
    #大写小写都可以
    ret = re.match("[hH]", "Hello Python")
    print(ret.group())
    ret = re.match("[hH]ello Python", "Hello Python")
    print(ret.group())
    print('-'*50)
    ret = re.match("[0-9]Hello Python", "6Hello Python")
    print(ret.group())
    ret = re.match("[0-35-9]Hello Python", "7Hello Python")
    print(ret.group())
    print('-'*50)
    # 使用\d 进行匹配
    ret = re.match(r"嫦娥\d号", "嫦娥1号发射成功")
    print(ret.group())
    ret = re.match(r"嫦娥\d号", "嫦娥2号发射成功")
    print(ret.group())
    ret = re.match(r"嫦娥\d号", "嫦娥3号发射成功")
    print(ret.group())

def multi_use():
    """
    多个字符匹配
    :return:
    """
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())
    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())
    ret = re.match("[A-Z][a-z]*", "Aabcdef")
    print(ret.group())
    print('-'*50)
    ret = re.match(r"[1-9]?[0-9]", "7")
    print(ret.group())
    ret = re.match(r"[1-9]?\d", "33")
    print(ret.group())
    ret = re.match(r"[1-9]?\d", "09")
    print(ret.group())

def start_end():
    #符合163邮箱的找出来
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for email in email_list:
        ret = re.match(r"[\w]{4,20}@163\.com", email) #匹配的字符串中出现了正则符号，需要在前面添加\n转义
        if ret:
            print("邮箱格式正确")
        else:
            print("邮箱格式不正确")

def other_func():
    """
    search findall sub split
    :return:
    """
    ret = re.search(r"\d+", "阅读次数为9999")
    print(ret.group())
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 1244")
    print(ret)
    ret = re.sub(r"\d+", "998", "python = 9973")
    print(ret)



if __name__ == '__main__':
    # simple_use()
    # single_use()
    # multi_use()
    # start_end()
    other_func()