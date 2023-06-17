# inputs = [[input, weight]]
inputs = [[1.3, 3.3], [3.5, 2.5], [5.1, 1.1], [2.4, 2.4]]
bias = 3

output = bias
for i in inputs:
    output += i[0] * i[1]

print("Inputs: " + str(inputs))
print("Bias: " + str(bias))
print("Output: " + str(output))
