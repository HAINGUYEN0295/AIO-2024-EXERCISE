import torch
import torch.nn as nn

# Initialize the Softmax class


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = exp_x.sum(dim=0, keepdim=True)
        return exp_x / sum_exp_x

# Initialize the SoftmaxStable class


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True).values
        exp_x = torch.exp(x - x_max)
        sum_exp_x = exp_x.sum(dim=0, keepdim=True)
        return exp_x / sum_exp_x


# QUESTION_1
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)  # tensor([0.0900, 0.2447, 0.6652])

# QUESTION_2
data_1 = torch.Tensor([5, 2, 4])
softmax_1 = Softmax()
output_1 = softmax_1(data_1)
print(output_1)  # tensor([0.7054, 0.0351, 0.2595])

# QUESTION_3
data_2 = torch.Tensor([1, 2, 300000000])
softmax_2 = Softmax()
output_2 = softmax_1(data_2)
print(output_2)  # tensor([0., 0., nan])

# QUESTION_4
data_2 = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output_stable = softmax_stable(data_2)
print(output_stable)  # tensor([0.0900, 0.2447, 0.6652])
