a = 'text'
b = 'testing'
''' text
' 0 1
t 1 
e 2
s 3
t 4
i 5
n 6
g 7
'''
b_list =[0, 1, 2, 3, 4, 5, 6, 7]

i = 0; j = 1
temp = b_list[i]
b_list =[1, 1, 2, 3, 4, 5, 6, 7]
i = 1; j = 1
a = b_list[j-1] +1 , b[j]+1, temp + 1 if a[i] != b[j] else temp
temp = b_list[j]
