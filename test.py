# 2640. Find the Score of All Prefixes of an Array


# nums = [1,1,2,4,8,16]
# d = []
# w = []
# for i in zip(nums):
# #     d.append(i+max(d))
# #     w.append(sum(d))

#     print(i)


class A:
    def foo(self):
        print ("A")
class B(A):
    pass
class C(A):
    def foo(self):
        print ("C")
class D:
    def foo(self):
        print ("D")
class E(B, C, D):
    pass
E().foo()