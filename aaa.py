#only 3layer network
class Network():
    
    def __init__(self,num_input,num_hidden,num_out,x=np.asarray([0.5,0.1]),t=np.array([0.1,0.5])):
        self.n_in=num_input
        self.n_hid=num_hidden
        self.n_out=num_out
        self.x=x
        self.t=t
        
    def ini_w(self):
        self.w1=np.random.rand(self.n_in,self.n_hid)
        self.w2=np.random.rand(self.n_hid,self.n_out)
        
    def ini_b(self):
        self.b1=np.random.rand(self.n_hid)
        self.b2=np.random.rand(self.n_out)
        
    def forward(self,x,w,b):
        
        self.out0=np.dot(self.x,self.w0)+b
        
        #out=[n_out]
        #for i in n_in:
        #    for j in n_out:
        #        out[j]+=w[i][j]*x[i]
                
        self.a=self.activation(n_out,out)
        
        self.out1=np.dot(self.a,self.w1)
    
    def activation(self,out):
        out=1.0/(1.0+np.exp(-out))
        self.out=out
        
    def lossfun(self):
        self.loss=(self.t-out)**2/2
        self.tloss=0
        for i in loss:
            self.tloss+=i
            
        
        
    def backprop(self):
        
        #dc/da_last(num i)
        dc_da1=self.t-self.a1
        
        #da_dz(num i)
        da_dz1=self.out1*(1-self.out1)
        
        #dz_da_second(num j)
        dz_dw2=self.a0
        
        #dc/dw2(num i*j)
        dc_dw2=[dc_da1[i]*da_dz1[i]*dz_dw2[j] for i in range(len(dc_da1)) for j in range(len(self.w2))]
        
        #reshape to j*i matrix to update w2
        dc_dw2=dc_dw2.reshape(len(self.w2),len(dc_da1))
        
        #dz/da2(num_i*j->reduce to j) da1/da2=da1/dz1*dz1/da2
        dc_da2=self.w2.transpose()*da_dz1*dc_da1
        dc_da2=np.sum(dc_da2,axis=1)
        
        #da3/dz2(num j) sigma_out(1-out)
        da_dz2=self.out0(1-self.out0)
        
        #dz/dw1_first(num j*k)
        dz_dw1=self.x
        
        #dc/dw1(num j*k)
        dc_dw1=[dc_da2[j]*da_dz2[j]*dz_dw1[j,k] for j in range(len(dc_da2)) for k in range(len(dz_dw1[0]))]       
