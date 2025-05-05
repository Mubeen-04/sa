import numpy as np
import matplotlib.pyplot as plt

# McCulloch-Pitts Neuron for AND, OR, and NOT gates
def mcp_neuron_and(x1, x2):
    w1, w2 = 1, 1
    theta = 2
    return 1 if (w1 * x1 + w2 * x2) >= theta else 0

def mcp_neuron_or(x1, x2):
    w1, w2 = 1, 1
    theta = 1
    return 1 if (w1 * x1 + w2 * x2) >= theta else 0

def mcp_neuron_not(x1):
    w1, theta = -1, 0
    return 1 if (w1 * x1) >= theta else 0

# XOR using MCP Neuron (XOR = (A AND NOT B) OR (NOT A AND B))
def mcp_neuron_xor(x1, x2):
    not_x1 = mcp_neuron_not(x1)
    not_x2 = mcp_neuron_not(x2)
    and1 = mcp_neuron_and(x1, not_x2)
    and2 = mcp_neuron_and(not_x1, x2)
    return not_x1, not_x2, and1, and2, mcp_neuron_or(and1, and2)

# Test cases
test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Table for initial values and NOT results
print("\n Initial and NOT Results ")
print("Input 1 | Input 2 | NOT x1 | NOT x2")
print("----------------------------------")
for x1, x2 in test_cases:
    not_x1, not_x2, _, _, _ = mcp_neuron_xor(x1, x2)
    print(f" {x1} | {x2} | {not_x1} | {not_x2}")

# Table for AND outputs
print("\n AND Gate Intermediate Results")
print("AND(x1, NOT x2) | AND(NOT x1, x2)")
print("---------------------------------")
for x1, x2 in test_cases:
    _, _, and1, and2, _ = mcp_neuron_xor(x1, x2)
    print(f" {and1} | {and2}")

# Table for XOR results
print("\n XOR Gate Final Results")
print("Input 1 | Input 2 | XOR Output")
print("-------------------------------")
for x1, x2 in test_cases:
    _, _, _, _, xor_output = mcp_neuron_xor(x1, x2)
    print(f" {x1} | {x2} | {xor_output} ")

# Visualization
x1_vals = [point[0] for point in test_cases]
x2_vals = [point[1] for point in test_cases]
outputs = [mcp_neuron_xor(x1, x2)[4] for x1, x2 in test_cases]

plt.figure(figsize=(6, 6))
plt.scatter(x1_vals, x2_vals, c=outputs, cmap='coolwarm', s=100, edgecolors='blue')
plt.xlabel("x1 (Input 1)")
plt.ylabel("x2 (Input 2)")
plt.title("XOR Gate Visualization")
plt.xticks([0, 1])
plt.yticks([0, 1])
plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)
plt.grid(True)
plt.show()