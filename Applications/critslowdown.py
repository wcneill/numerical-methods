from Applications import vfield as vf


def crit_slow(t, x):
    return -x**3


def exp_decay(t, y):
    return -y


# graph an ODE modelling critical slow down (has discontinuities in it's second derivative)
vf.vf_grapher(crit_slow, 0., 10., .001, 10.)

# graph an ODE modelling exponential decay (compare to critical slowdown)
vf.vf_grapher(exp_decay, 0., 10., .001, 10.)

