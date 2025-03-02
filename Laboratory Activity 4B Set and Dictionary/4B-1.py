A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

num_elements_A_B = len(A.union(B))
print("Number of elements in A and B:", num_elements_A_B)

num_elements_B_not_A_C = len(B - (A.union(C)))
print("Elements in B not in A and C:", num_elements_B_not_A_C)

set_i = {'h', 'i', 'j', 'k'}
set_ii = {'c', 'd', 'f'}
set_iii = {'b', 'c', 'h'}
set_iv = {'d', 'f'}
set_v = {'c'}
set_vi = {'l', 'm', 'o'}

print("Set i:", set_i)
print("Set ii:", set_ii)
print("Set iii:", set_iii)
print("Set iv:", set_iv)
print("Set v:", set_v)
print("Set vi:", set_vi)