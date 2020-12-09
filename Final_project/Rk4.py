import numpy as np



def solver(h,t,x,f):
    """
    Solve a first degree system of equations using
    runge-kutta of 4th order
    
    
    Parameters
    ----------
    h : float
        grid spacing.
    x : array_like
        one dimension
    f : func
        ODE system
    
    """
    
    k1=h*f(t,x)
    k2=h*f(t+h/2,x+k1/2)
    k3=h*f(t+h/2,x+k2/2)
    k4=h*f(t+h,x+k3)
    
    return x+(k1+2*k2+2*k3+k4)/6.
