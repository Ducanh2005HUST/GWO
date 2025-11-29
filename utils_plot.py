import matplotlib.pyplot as plt

def plot_history(history_gwo, history_mgwo):
    plt.figure(figsize=(7,5))
    plt.plot(history_gwo, label="GWO", linewidth=2)
    plt.plot(history_mgwo, label="mGWO", linewidth=2)
    plt.xlabel("Iteration")
    plt.ylabel("Fitness (best)")
    plt.title("Convergence Curve")
    plt.grid(True)
    plt.legend()
    plt.show()
