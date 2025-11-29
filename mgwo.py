import numpy as np

def mGWO(fitness, num_wolves=20, dim=2, max_iter=50, lb=-10, ub=10):
    wolves = np.random.uniform(lb, ub, (num_wolves, dim))
    alpha = beta = delta = None
    alpha_score = beta_score = delta_score = np.inf
    history = []

    for t in range(max_iter):
        for i in range(num_wolves):
            score = fitness(wolves[i])
            if score < alpha_score:
                delta_score, delta = beta_score, beta
                beta_score, beta = alpha_score, alpha
                alpha_score, alpha = score, wolves[i].copy()
            elif score < beta_score:
                delta_score, delta = beta_score, beta
                beta_score, beta = score, wolves[i].copy()
            elif score < delta_score:
                delta_score, delta = score, wolves[i].copy()

        a = 2 * np.exp(-(4 * t / max_iter))

        for i in range(num_wolves):
            r1, r2 = np.random.rand(), np.random.rand()
            A1 = 2*a*r1 - a
            C1 = 2*r2
            X1 = alpha - A1 * abs(C1 * alpha - wolves[i])

            r1, r2 = np.random.rand(), np.random.rand()
            A2 = 2*a*r1 - a
            C2 = 2*r2
            X2 = beta - A2 * abs(C2 * beta - wolves[i])

            r1, r2 = np.random.rand(), np.random.rand()
            A3 = 2*a*r1 - a
            C3 = 2*r2
            X3 = delta - A3 * abs(C3 * delta - wolves[i])

            wolves[i] = (X1 + X2 + X3) / 3
            wolves[i] = np.clip(wolves[i], lb, ub)

        history.append(alpha_score)

    return alpha_score, alpha, history
