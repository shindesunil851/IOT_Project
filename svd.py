import numpy

x=[70000,58000,49000,38000]
y=[169,119,94,86]

van=numpy.vander(x)
# print(van)

z=numpy.zeros((4,2))
p=0
q=0
for i in range(2,4):
    for j in range(0,4):
        z[j][p]=van[j][i]
    p=p+1

#print(z)

u,s,vh=numpy.linalg.svd(z,full_matrices=True)

#print(vh)
s_inv=numpy.linalg.inv(numpy.diag(s))
u_trans=numpy.transpose(u)
vh_trans=numpy.transpose(vh)
#print(s_inv)

prod1=vh_trans.dot(s_inv)

# a_inv=prod1.dot(u_trans)

#print(u)

mpsi_z=numpy.linalg.pinv(z)

#print(mpsi_z.dot(z))

a=mpsi_z.dot(y)[0]
b=mpsi_z.dot(y)[1]
print(a,b)