import numpy as np
import matplotlib.pyplot as plt
import random
%matplotlib inline
from IPython.core.debugger import Tracer
#only 3layer network
class Network():
    
    def __init__(self,num_input,num_hidden,num_out,x=np.asarray([[1.,2.]]),
                 t=np.array([[200.,600.]])
                 #t=np.array([[0.,0.]])
                 
                ):
        self.n_in=num_input
        self.n_hid=num_hidden
        self.n_out=num_out
        self.x=x
        self.t=t
        self.eta=0.001
        self.ini_w()
        self.ini_b()
        
    def ini_w(self):
        self.w1=np.random.rand(self.n_in,self.n_hid)
        self.w2=np.random.rand(self.n_hid,self.n_out)
        
        self.w1=np.array([[1.,2.],[3.,4.]])
        self.w2=np.array([[5.,6.],[7.,8.]])
        
    def ini_b(self):
        self.b1=np.random.rand(self.n_hid)
        self.b2=np.random.rand(self.n_out)
        
        self.b1=0
        self.b2=0
        
    def forward(self):
        
        #Tracer()()
        
        #-|=|
        self.z0=np.matmul(self.w1,self.x.transpose())
        
        #|=|
        #self.a0=self.relu(self.z0)
        self.a0=self.z0
        
        #-|=|
        self.z1=np.matmul(self.w2,self.a0)
        
        #|=|
        #self.a1=self.relu(self.z1)
        self.a1=self.z1
        
        #|=|
        #self.a1=self.softmax(self.z1)
        
        #f(| |)=|
        self.lossfun(self.a1)
    
    def activation(self,out):
        out=1.0/(1.0+np.exp(-out))
        self.out=out
        
    def relu(self,out):
        return np.maximum(out,0)
    
    def softmax(self,out):
        e_out=[np.exp(x) for x in out]
        soe=np.sum(e_out)
        a=e_out/soe
        return a
        
        
    def lossfun(self,a):
        self.loss=(self.t.transpose()-a)**2/2
        self.t_loss=np.sum(self.loss)
            
        
        
    def backprop(self):
        
        #dc/da1_last(num i) |=| |
        self.dc_da1=-1*(self.t.transpose()-self.a1)
        
        #da1/dz1(num i) |=|
        #self.da1_dz1=self.a1*(1-self.a1)
        #self.da1_dz1=np.divide(self.a1,self.a1,where=self.a1!=0)
        self.da1_dz1=np.ones([len(self.a1),1])
        
        #dz/dw2(num j) |
        self.dz1_dw2=self.a0
        
        #dc/dw2(num i*j) i| j-
        self.dc_dw2=np.array([self.dc_da1[i]*self.da1_dz1[i]*self.dz1_dw2[j]  for i in range(len(self.dc_da1)) for j in range(len(self.w2))])
        #reshape to i*j matrix to update w2
        self.dc_dw2=self.dc_dw2.reshape(len(self.dc_da1),len(self.w2))
        
        #dc_dz1(num i) |
        self.dc_dz1=self.dc_da1*self.da1_dz1
        
        #dc_da0(numj i*ixj->reduce to j) i|j-=i|*i|j- -->j|
        self.dc_da0=self.dc_dz1*self.w2
        self.dc_da0=np.sum(self.dc_da0,axis=0).reshape(len(self.w2[0]),1)
        
        #da0/dz0(num j) |=|
        #self.da0_dz0=np.divide(self.a0,self.a0,where=self.a0!=0)
        self.da0_dz0=np.ones([len(self.a0),1])
        
        #dz0/dw1(num k)|=|
        self.dz0_dw1=self.x.transpose()
        
        #dc_dw1(num j*k) j|k-
        self.dc_dw1=np.array([self.dc_da0[j]*self.da0_dz0[j]*self.dz0_dw1[k]  for k in range(len(self.x[0])) for j in range(len(self.dc_da0))])
        #reshape to j*k matrix to update w2
        self.dc_dw1=self.dc_dw1.reshape(len(self.x[0]),len(self.w1))
        
    def update_w(self):
        
        self.w2-=self.eta*self.dc_dw2
        self.w1-=self.eta*self.dc_dw1
        
    def train(self):
        
        self.forward()
        self.backprop()
        self.update_w()
        
nn=Network(2,2,2)
loss=[]
w1=[]
w2=[]
dw2=[]
for i in range(60000):
    nn.train()
    loss.append(nn.t_loss)
    
plt.subplot()
plt.plot(range(len(loss)),loss)
plt.show()
print nn.t_loss
print nn.w1
print nn.w2
print "a1",nn.a1
