import torch
import numpy as np
print("This is just a test program to see if pytorch is installed")
x = torch.empty(3,2)
y= torch.ones(3,3,dtype=torch.float64)
print(x)
print("y is \n",y)
print("size of y is",y.size())

randx = torch.rand(2,2)
randy = torch.rand(2,2)
print("randx before adding randy is \n",randx)
print("randy is \n",randy)
randx.add_(randy) # Underscore at the end means in place to randx
print("randx after adding randy is\n",randx)

randx_minus_randy = torch.sub(randx,randy)
print("randx_minus_randy is \n",randx_minus_randy )

#Converting Numpy array to torch array
a = np.ones(5)
print(a)
b = torch.from_numpy(a)
print(b)

#Using GPU for storing and manipulating arrays
if torch.cuda.is_available():
    current_device = torch.device("cuda")
    print("current_device is",current_device)
    x =torch.ones(5,device=current_device)
    y = torch.ones(5)
    y = y.to(current_device)
    z = x+ y #Addition won't be performed unless the two operands are on same device
    z = z.to("cpu")
    print("z is",z)


