def mcp_neuron_and(x1, x2, w1, w2, theta):
    return 1 if (x1 * w1 + x2 * w2) >= theta else 0

def mcp_neuron_or(x1, x2, w1, w2, theta):
    return 1 if (x1 * w1 + x2 * w2) >= theta else 0

def mcp_neuron_not(x, w, theta):
    return 1 if (x * w) >= theta else 0

# Get user-defined weights and thresholds
print("Enter weights and threshold for AND gate:")
w1_and = int(input("w1: "))
w2_and = int(input("w2: "))
theta_and = int(input("Threshold: "))

print("\nEnter weights and threshold for OR gate:")
w1_or = int(input("w1: "))
w2_or = int(input("w2: "))
theta_or = int(input("Threshold: "))

print("\nEnter weight and threshold for NOT gate:")
w_not = int(input("w: "))
theta_not = int(input("Threshold: "))

# Test inputs
test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]
not_cases = [0, 1]
# Expected outputs
expected_and = [0, 0, 0, 1]
expected_or = [0, 1, 1, 1]
expected_not = [1, 0]

# AND Gate
print("\n--- AND Gate ---")
for i,(x1, x2) in enumerate(test_cases):
    output = mcp_neuron_and(x1, x2, w1_and, w2_and, theta_and)
    print(f"{x1} AND {x2} => {output} | Expected: {expected_and[i]}")

# OR Gate
print("\n--- OR Gate ---")
for x1, x2 in test_cases:
    output = mcp_neuron_or(x1, x2, w1_or, w2_or, theta_or)
    print(f"{x1} OR {x2} => {output}")

# NOT Gate
print("\n--- NOT Gate ---")
for x in not_cases:
    output = mcp_neuron_not(x, w_not, theta_not)
    print(f"NOT {x} => {output}")
