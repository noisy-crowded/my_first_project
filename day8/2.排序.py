import random
import time

class Sort:
    def __init__(self, n):
        self.len = n #排序列表的长度
        self.arr = [0] * n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0,99)

    def partition(self, left, right):
        arr = self.arr
        k = i = left
        random_pos = random.randint(left, right)  #避免陷入最坏时间复杂度
        arr[random_pos], arr[i] = arr[i], arr[random_pos]
        for i in range(left, right):
            if arr[i] < arr[right]: #分割法，如果某个值小于分隔值就交换
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_max_heap(self, pos, arr_len):
        """
        把某个子树调整为大根堆
        :param pos: 被调整的元素位置
        :param arr_len: 列表的长度
        :return:
        """
        dad = pos
        son = dad * 2 + 1
        arr = self.arr
        while son < arr_len:
            if son + 1 < arr_len and arr[son] < arr[son + 1]: #右孩子存在且左孩子小于右孩子
                son += 1
            if arr[son] > arr[dad]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = dad * 2 + 1
            else:
                break


    def heap_sort(self):
        """
        把堆调整为大根堆
        :param n:
        :return:
        """
        for i in range(self.len // 2 - 1, -1, -1):
            self.adjust_max_heap(i, self.len)
        arr = self.arr
        arr[0], arr[self.len - 1] = arr[self.len - 1], arr[0] #把堆顶元素和最后一个元素交换
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0, arr_len)
            arr[0], arr[arr_len - 1] = arr[arr_len - 1], arr[0]

if __name__ == "__main__":
    my_sort = Sort(10)
    print(my_sort.arr)
    start_time = time.time()
    # my_sort.quick_sort(0, 9)
    my_sort.heap_sort()
    end_time = time.time()
    print(f"运行时间为{end_time - start_time}")
    print(my_sort.arr)