
class Perceptron:
    def __init__(self, learning_rate=1, epochs=4):
        self.lr = learning_rate
        self.epochs = epochs
        self.w1 = float(input("Enter initial weight w1: "))
        self.w2 = float(input("Enter initial weight w2: "))
        self.bias = float(input("Enter initial bias: "))

    def activation(self, y_in):
        if y_in > 0:
            return 1
        elif y_in < 0:
            return -1
        else:
            return 0

    def train(self, data):
        for epoch in range(1, self.epochs + 1):
            print(f"\nEpoch {epoch}")
            errors = 0
            for i in range(len(data)):
                (x1, x2), target = data[i]
                # x1, x2, target = data.iloc[i]
                y_in = x1 * self.w1 + x2 * self.w2 + self.bias
                output = self.activation(y_in)

                if output != target:
                    self.w1 += self.lr * target * x1
                    self.w2 += self.lr * target * x2
                    self.bias += self.lr * target
                    errors += 1

                print(f"x1={x1}, x2={x2}, target={target}, output={output}, w1={self.w1}, w2={self.w2}, bias={self.bias}")

            if errors == 0:
                print("Training converged early.")
                break

    # def plot_boundary(self, data):
    #     plt.figure()
    #     for i in range(len(data)):
    #         x1, x2, target = data.iloc[i]
    #         color = 'green' if target == 1 else 'red'
    #         plt.scatter(x1, x2, c=color)

    #     x_vals = np.linspace(-2, 2, 100)
    #     if self.w2 != 0:
    #         y_vals = -(self.w1 * x_vals + self.bias) / self.w2
    #         plt.plot(x_vals, y_vals, color='blue')

    #     plt.xlabel('x1')
    #     plt.ylabel('x2')
    #     plt.title('Perceptron Decision Boundary')
    #     plt.grid()
    #     plt.show()

# Example use
if __name__ == "__main__":
    # Example: AND-like gate with -1 and 1
    data = [
    ([1, 1], 1),
    ([1, -1], 1),
    ([-1, 1], 1),
    ([-1, -1], -1)
]

    model = Perceptron()
    model.train(data)
    #model.plot_boundary(data)

# data = pd.DataFrame({
#         'x1': [1, 1, -1, -1],
#         'x2': [1, -1, 1, -1],
#         'target': [1, 1, 1, -1]
#     })