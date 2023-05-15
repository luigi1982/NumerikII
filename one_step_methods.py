def apply_method(phi, t0, N, a, y0, f):

    h = a/N
    u = [y0]
    for i in range(N):
        t = t0 + i*h
        u_next = u[-1] + h*phi(t, u[-1], h, f)
        u.append(u_next)

    return [t0 + i*h for i in range(N+1)], u


def second_order(a1, a2, p1, p2, h, f, t, z):

    f_val = f(t,z)
    return a1*f_val + a2*f(t+p1*h, z+p2*h*f_val)

def heun(t, z, h, f):

    return second_order(0.5, 0.5, 1, 1, h, f, t, z)

def modified_euler(t, z, h, f):

    return second_order(0, 1, 0.5, 0.5, h, f, t, z)