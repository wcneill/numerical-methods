import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import rk4 as rk


if __name__ == '__main__':

    def y_prime(y, z, t):
        return -t * y

    def z_prime(y, z, t):
        return z

    t_0 = -10
    t_n = 10
    dt = .05

    steps = int((t_n - t_0) / dt)

    y_soln = [0.0] * steps
    z_soln = [0.0] * steps
    time = np.arange(t_0, t_n, dt)

    y_soln[0] = 1.928749848e-22
    z_soln[0] = .0000453999297625

    for i in np.arange(1, steps):
        y_soln[i], z_soln[i] = rk.rungekutta4(dt, time[i - 1], (y_soln[i - 1], z_soln[i - 1]), y_prime, z_prime)

    error1 = []
    for i in np.arange(steps):
        error1.append(abs(math.e ** ((-time[i] ** 2)/2) - y_soln[i]))

    # collect solution data for plotting
    df1 = pd.DataFrame({'t': time, 'u': y_soln})
    df2 = pd.DataFrame({'t': time, 'u': z_soln})

    # collect error data for plotting
    df3 = pd.DataFrame({'t': time, 'error': error1})

    fig, ax1 = plt.subplots(figsize=(10, 6))
    color = 'tab:green'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('y(t)', color=color)
    ax1.plot('t', 'u', data=df1, color=color)
    axes = plt.gca()
    axes.set_ylim((0, 2))

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:red'
    ax2.set_ylabel('z(t)', color=color)  # we already handled the x-label with ax1
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.plot('t', 'u', data=df2, color=color)
    plt.grid(True)
    axes = plt.gca()
    axes.set_ylim((0, 2))

    fig.tight_layout()

    fig, eax = plt.subplots(figsize=(10, 6))
    color = 'tab:red'
    eax.set_xlabel('time (s)')
    eax.set_ylabel('absolute error')
    eax.plot('t', 'error', data=df3, color=color)

    plt.grid(True)
    plt.show()