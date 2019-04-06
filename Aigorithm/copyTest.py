'''深浅拷贝的比较'''
# copy：浅拷贝。只拷贝父对象，不会拷贝对象的内部的子对象,只要改变其他也会跟着变
# deepcopy：深拷贝。拷贝对象及其子对象这个不会，因为它和初始的是不同的对象
import copy

a = [1, 2, ['a', 'b']]

b = copy.copy(a)
c = copy.deepcopy(a)
print(b)
print(c)
a.append(3)
a[2].append('c')
print(b)
print(c)