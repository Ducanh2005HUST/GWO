from gwo import GWO
from mgwo import mGWO
from problem_comm import fitness_comm
from utils_plot import plot_history

def main():
    print("=== Running GWO ===")
    score_gwo, best_gwo, hist_gwo = GWO(
        fitness=fitness_comm,
        num_wolves=30,
        dim=1,
        max_iter=60,
        lb=0,
        ub=5
    )

    print("=== Running mGWO ===")
    score_mgwo, best_mgwo, hist_mgwo = mGWO(
        fitness=fitness_comm,
        num_wolves=30,
        dim=1,
        max_iter=60,
        lb=0,
        ub=5
    )

    print("Best solution GWO:", best_gwo)
    print("Best solution mGWO:", best_mgwo)
    print("GWO fitness:", score_gwo)
    print("mGWO fitness:", score_mgwo)

    # Plot convergence
    plot_history(hist_gwo, hist_mgwo)

if __name__ == "__main__":
    main()
