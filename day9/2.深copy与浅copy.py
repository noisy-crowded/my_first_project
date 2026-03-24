import copy

def use_list_copy():
    """
    使用列表的copy,即浅拷贝
    :return:
    """
    a = [1, 2, 3]
    b = a
    b[0] = 10
    print(a)
    #直接赋值与浅拷贝不一样
    c = a.copy()
    c[0] = 20
    print(a)

def use_copy():
    """
    使用copy包中的copy
    :return:
    """
    a = [1, 2, 3]
    b = copy.copy(a)
    b[0] = 10
    print(id(a))
    print(id(b))
    print(a)
    print(b)

def use_copy2():
    """
    copy是浅copy,只copy第一层
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c---{c}')
    print(f'd---{d}')

def use_deepcopy():
    """
    递归去copy,不管有多少层，都会创建空间，把数据拿进来
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c---{c}')
    print(f'd---{d}')


if __name__ == '__main__':
    # use_list_copy()
    # use_copy()
    # use_copy2()
    use_deepcopy()