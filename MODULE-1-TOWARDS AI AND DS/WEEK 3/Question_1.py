# Question_1
import torch
import torch.nn as nn

data = torch.tensor([1.0, 2.0, 3.0])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
assert round(output[0].item(), 2) == 0.09
print(output)
