import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.stats import norm
from scipy.integrate import quad
from numpy import *
from random import *
from math import *
from random import *
from math import *


n=275
a_x=0.1
a_y= -3.3
gamma2_x=14.44
gamma2_y=4.7
r_xy=0.74 
alfa=0.01

#gamma2_x=6.76
gamma_x = sqrt(gamma2_x)
#n = 350
#a_x = 2.2
#a_y=-5.4
#gamma2_y=1.75
gamma_y = sqrt(gamma2_y)
#r_xy=0.12

#alfa = 0.001
y=0.99

x1 = [0 for i in range(n)]
x2 = [0 for i in range(n)]

Y_x = [0 for i in range(n)]
Y_y = [0 for i in range(n)]

#матрица перехода В
b11=sqrt(gamma2_x)
b12=0
b21=r_xy/b11
b22=sqrt(gamma2_y-(r_xy**2)/gamma2_x)

# Генерация последовательности псевдослучайных чисел в соответствии с нормальным законом распределения выполняется
#  с помощью метода random.normalvariate(mu, sigma)

input = open(r"C:\Users\Ksenia\terver1.txt", "r")
for i in range(n):
    x1[i] = double(input.readline())
for i in range(n, 2*n):
    x2[i-n] = double(input.readline())
input.close()

text = open(r"C:\Users\Ksenia\output1.txt","w")

#for i in range(n):
    #for j in range(2):
#        X[i][0]=x1[i]
#        X[i][1]=x2[i]

#print(str(X));

#input = open(r"C:\Users\Ksenia\terver1.txt", "r")
#for i in range(n):
#    xi[i] = double(input.readline())
#input.close()
#text = open(r"C:\Users\Ksenia\output1.txt","w")

##########################################
text.write("\n")
ex = 0
for i in range(n):#выборочное среднее
    ex += x1[i] 
ex/=n
text.write("mx1= " + str(ex)+"\n")

ey = 0
for i in range(n):#выборочное среднее
    ey += x2[i] 
ey/=n
text.write("my1= " + str(ey)+"\n")


def calculate_variance(X, ex): #выборочная дисперсия
  dx = 0
  for i in range(n):
      dx += (X[i]-ex)**2
  dx/=n
  return dx

dx = calculate_variance(x1, ex)
dy = calculate_variance(x2,ey)

text.write("dx1= " +str(dx)+"\n" + "dy1= "+str(dy))


text.write("\n")
text.write("mx= " + str(a_x)+"\n")
text.write("dx= "+str(gamma2_x)+"\n")
text.write("my= " + str(a_y)+"\n")
text.write("dy= "+str(gamma2_y)+"\n")

R_xy=0
for i in range (n):
    R_xy+=(x1[i]-ex)*(x2[i]-ey)
R_xy/=n

r_xy1 = R_xy/sqrt(dx*dy)
text.write("r_xy1= "+str(r_xy1)+"\n")

###################################
#3.2
#1)
#количество интервалов
Nx = floor(1+ 3.32*log(n, 10)) + 1
Ny = floor(1+ 3.32*log(n, 10)) + 1
text.write("\n"+"Nx= "+str(Nx)+"\n"+"Ny="+str(Ny))


ux=(max(x1)-min(x1))/Nx
text.write("> ")
for i in range (Nx+1):
    text.write(str(min(x1)+ux*i)+"\n")

uy=(max(x2)-min(x2))/Ny
for i in range (Ny+1):
    text.write(str(min(x2)+uy*i)+"\n")

####################################3

Nx_=4
Ny_=4

#v_ij [Nx_]= {44, 21, 12,17 ,,76,9}
v_ij = [ [44, 21, 12,17], [27, 15, 13, 12], [30, 15,16,15],[34,20,28,31] ]
vk_xPosle =[94, 67,76, 113]
vk_yPosle =[135, 71,69, 75]

hi2=0

for i in range(Nx_):
    for j in range(Ny_):
        hi2+=(((v_ij[i][j]-(vk_xPosle[i]*vk_yPosle[j])/n)**2)/(vk_xPosle[i]*vk_yPosle[j]))
hi2*=n

#for i in range(Nx_):
#    for j in range(Ny_):
#        hi2+=((v_ij[i][j]**2)/(vk_xPosle[i]*vk_yPosle[j]))
#hi2*=n
#hi2-=n
text.write("hi2: "+str(hi2)+"\n")

#hi2(1-alfa);(Nx_)(Ny_)
#n=3*3=9 => 
#p=1-alfa=0.999

hi2_stat=27.877
text.write("hi2_stat: "+str(hi2_stat)+"\n")

if abs(hi2)>=hi2_stat:
    text.write("гипотезу отвергают\n")
else:
    text.write("гипотезу принимают\n")

#значимость коэфф корреляции
#t(1-alfa)/2(n-2) = t (0.9995)(2)
t=3.291

T = (r_xy1*sqrt(n-2))/sqrt(1-r_xy1**2)

text.write("t" + str(t) +"\n"+ "T"+ str(T))

if abs(T)>=t:
    text.write("зависимы\n")
else:
    text.write("независимы\n")

#3.3
#Y_emp_ur=r_xy1*dy/dx*(x-ex)+ey
#X_emp_ur=r_xy1*dx/dy*(y-ey)+ex