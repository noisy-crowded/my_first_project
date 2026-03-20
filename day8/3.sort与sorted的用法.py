#sort和sorted的区别在于，sort会改变原来对象，sorted会排好后创建一个新的对象
my_list = "This is a test string from Andrew".split()
print(my_list)

def change_lower(str_name):
    return str_name.lower()

#可以传递一个比较规则的函数
print(sorted(my_list))
print(sorted(my_list, key = change_lower)) #改变规则，按小写排


print('-' * 50)
student_tuples = [
    ("john", 'A', 15),
    ("jane", 'B', 12),
    ("dave", 'C', 10)
]
#lambda表达式就是匿名函数，提高编写效率，增加阅读速度
print(sorted(student_tuples, key = lambda x : x[1]))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__更方便，可以返回非字符串类型
        :return:
        """
        return repr((self.name, self.grade, self.age))

student = Student("John", 'A', 23)
print(student)
