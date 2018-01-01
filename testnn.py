#only 3layer network
class Network:
    
    def __init__(self,num_input,num_hidden,num_out,x=np.asarray([0.5,0.1]),w,b,t=np.array([0.1,0.5])):
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
        
        out=np.dot(x,w)+b
        
        #out=[n_out]
        #for i in n_in:
        #    for j in n_out:
        #        out[j]+=w[i][j]*x[i]
                
        self.activation(n_out,out)
    
    def activation(self,out):
        out=1.0/(1.0+np.exp(-out))
        self.out=out
        
    def losfun(self):
        self.loss=(t-out)**2/2
        
    def backprop(self,):
        
        
        
        
        
                
            
            
