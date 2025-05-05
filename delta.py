import numpy as np
import matplotlib.pyplot as plt

# Sigmoid activation function (used for output calculation)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Initialize input values (features) and target labels (true values)
inputs = [
    np.array([1, -2, 0, -1]),   # Input 1
    np.array([0, 1.5, -0.5, -1]), # Input 2
    np.array([-1, 1, 0.5, -1])   # Input 3
]
targets = [-1, -1, 1]  # True output values corresponding to inputs

# Initialize weights and bias randomly
weights = np.array([1.0, -1.0, 0.0, 0.5])
bias = 0.0
learning_rate = 0.01  # The step size for weight updates

# We will track the error and how the weights change over time
# epoch_errors = []  # To store error at each epoch
# weights_history = [weights.copy()]  # To store weights history
# bias_history = [bias]  # To store bias history

# Training loop: 5 iterations (epochs)
epochs = 5
for epoch in range(epochs):
    print(f"Epoch {epoch + 1}:")
    epoch_error = 0  # This will store the error for the current epoch

    # Iterate through all inputs to calculate error and update weights
    for i, xi in enumerate(inputs):
        target = targets[i]
        
        # Calculate the weighted sum (net input)
        net = np.dot(weights, xi) + bias
        
        # Apply sigmoid to get the output (predicted value)
        output = sigmoid(net)
        
        # Calculate error (difference between target and output)
        error = target - output
        epoch_error += error ** 2  # Squared error for this input

        # Update weights and bias using the error
        weights += learning_rate * error * xi
        bias += learning_rate * error

        # Print the updated values for each input
        print(f"Input: {xi}, Target: {target}, Output: {output:.2f}, Error: {error:.2f}")
        print(f"Updated weights: {weights}, Updated bias: {bias}\n")

    # Save the error and weight values for plotting later
    # epoch_errors.append(epoch_error)
    # weights_history.append(weights.copy())
    # bias_history.append(bias)

# # Plot the total error (squared error) over the epochs
# plt.figure(figsize=(10, 5))
# plt.plot(range(1, epochs + 1), epoch_errors, marker='o', color='r')
# plt.title('Error per Epoch')
# plt.xlabel('Epoch')
# plt.ylabel('Squared Error')
# plt.grid(True)
# plt.show()

# # Plot how weights change over time
# weights_array = np.array(weights_history)
# plt.figure(figsize=(10, 5))
# for i in range(weights_array.shape[1]):
#     plt.plot(range(epochs + 1), weights_array[:, i], marker='o', label=f'Weight {i + 1}')
# plt.title('Weights Adjustment Across Epochs')
# plt.xlabel('Epoch')
# plt.ylabel('Weight Value')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot how bias changes over time
# plt.figure(figsize=(10, 5))
# plt.plot(range(epochs + 1), bias_history, marker='o', color='b')
# plt.title('Bias Adjustment Across Epochs')
# plt.xlabel('Epoch')
# plt.ylabel('Bias Value')
# plt.grid(True)
# plt.show()
