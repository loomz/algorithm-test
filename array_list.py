# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, lis):
        print("list = %s" % lis)

    def test_num(self):
        a = 3
        a, b = 1, a
        print("a=%s, b=%s" % (a, b))

    def test_num2(self):
        a = 3
        a = 1
        b = a
        print("a=%s, b=%s" % (a, b))

    def test_num3(self):
        print(5 % 2)

if __name__ == '__main__':
    lis = [1, 2, 3, 4, 5]
    lis.append(6)
    print(lis)
    lis.pop()
    print(lis)
    print(type(lis))
    for i in lis:
        print(i)
