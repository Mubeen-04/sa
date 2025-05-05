import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Dot product of two lists
def dot_product(a, b):
    return sum(ai * bi for ai, bi in zip(a, b))

# Initialize input values (features) and target labels
inputs = [
    [1, -2, 0, -1],     # Input 1
    [0, 1.5, -0.5, -1], # Input 2
    [-1, 1, 0.5, -1]    # Input 3
]
targets = [-1, -1, 1]  # True output values

# Initialize weights and bias
weights = [1.0, -1.0, 0.0, 0.5]
bias = 0.0
learning_rate = 0.01

# Training loop
epochs = 5
for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}:")
    epoch_error = 0

    for i, xi in enumerate(inputs):
        target = targets[i]

        # Weighted sum (net input)
        net = dot_product(weights, xi) + bias

        # Activation output
        output = sigmoid(net)

        # Error calculation
        error = target - output
        epoch_error += error ** 2

        # Update weights and bias
        for j in range(len(weights)):
            weights[j] += learning_rate * error * xi[j]
        bias += learning_rate * error

        # Output progress
        print(f"Input: {xi}, Target: {target}, Output: {output:.2f}, Error: {error:.2f}")
        print(f"Updated weights: {weights}, Updated bias: {bias:.4f}")
