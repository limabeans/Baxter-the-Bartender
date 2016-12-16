#!/usr/bin/env python
"""Kinematic function skeleton code for Prelab 3.
Course: EE 106A, Fall 2015
Written by: Aaron Bestick, 9/10/14
Used by: EE106A, 9/11/15

This Python file is a code skeleton for Pre lab 3. You should fill in 
the body of the eight empty methods below so that they implement the kinematic 
functions described in the homework assignment.

When you think you have the methods implemented correctly, you can test your 
code by running "python kin_func_skeleton.py at the command line.

This code requires the NumPy and SciPy libraries. If you don't already have 
these installed on your personal computer, you can use the lab machines or 
the Ubuntu+ROS VM on the course page to complete this portion of the homework.
"""

import numpy as np
import scipy as sp
from scipy import linalg

np.set_printoptions(precision=4,suppress=True)

def skew_3d(omega):
    """
    Converts a rotation vector in 3D to its corresponding skew-symmetric matrix.
    
    Args:
    omega - (3,) ndarray: the rotation vector
    
    Returns:
    omega_hat - (3,3) ndarray: the corresponding skew symmetric matrix
    """
    if not omega.shape == (3,):
        raise TypeError('omega must be a 3-vector')
    
    #YOUR CODE HERE
    wx,wy,wz = tuple(omega.tolist())
    omega_hat = np.array([[0,-1*wz,wy],[wz,0,-1*wx],[-1*wy,wx,0]])
    return omega_hat

def rotation_2d(theta):
    """
    Computes a 2D rotation matrix given the angle of rotation.
    
    Args:
    theta: the angle of rotation
    
    Returns:
    rot - (2,2) ndarray: the resulting rotation matrix
    """
    
    #YOUR CODE HERE
    rot = np.array([[np.cos(theta),-1*np.sin(theta)],[np.sin(theta),np.cos(theta)]]) 
    return rot

def rotation_3d(omega, theta):
    """
    Computes a 3D rotation matrix given a rotation axis and angle of rotation.
    
    Args:
    omega - (3,) ndarray: the axis of rotation
    theta: the angle of rotation
    
    Returns:
    rot - (3,3) ndarray: the resulting rotation matrix
    """
    if not omega.shape == (3,):
        raise TypeError('omega must be a 3-vector')
    
    #YOUR CODE HERE
    iden = np.identity(3)
    w_mag = np.linalg.norm(omega)
    w_hat = skew_3d(omega)
    sin_component = np.divide(np.multiply(w_hat,np.sin(w_mag*theta)), w_mag)
    cos_component = np.divide(np.multiply(np.dot(w_hat,w_hat), 1 - np.cos(w_mag*theta)), w_mag**2)
    rot = np.add(iden, np.add(sin_component, cos_component))
    return rot

def hat_2d(xi):
    """
    Converts a 2D twist to its corresponding 3x3 matrix representation
    
    Args:
    xi - (3,) ndarray: the 2D twist
    
    Returns:
    xi_hat - (3,3) ndarray: the resulting 3x3 matrix
    """
    if not xi.shape == (3,):
        raise TypeError('omega must be a 3-vector')

    #YOUR CODE HERE
    vx, vy, w = tuple(xi.tolist())
    xi_hat = np.array([[0,-1*w,vx],[w,0,vy],[0,0,0]])
    return xi_hat

def hat_3d(xi):
    """
    Converts a 3D twist to its corresponding 4x4 matrix representation
    
    Args:
    xi - (6,) ndarray: the 3D twist
    
    Returns:
    xi_hat - (4,4) ndarray: the corresponding 4x4 matrix
    """
    if not xi.shape == (6,):
        raise TypeError('xi must be a 6-vector')

    #YOUR CODE HERE
    vx,vy,vz,wx,wy,wz = tuple(xi.tolist())
    xi_hat = np.array([[0,-1*wz,wy,vx],[wz,0,-1*wx,vy],[-1*wy,wx,0,vz],[0,0,0,0]])
    return xi_hat

def homog_2d(xi, theta):
    """
    Computes a 3x3 homogeneous transformation matrix given a 2D twist and a 
    joint displacement
    
    Args:
    xi - (3,) ndarray: the 2D twist
    theta: the joint displacement
    
    Returns:
    g - (3,3) ndarray: the resulting homogeneous transformation matrix
    """
    if not xi.shape == (3,):
        raise TypeError('xi must be a 3-vector')

    #YOUR CODE HERE
    vx,vy,w = tuple(xi.tolist())
    t = theta
    p1 = (vx*(np.sin(w*t))/w) + (vy*np.cos(w*t) - vy)/w
    p2 = vx/w - (vx*np.cos(w*t))/w + (vy*np.sin(w*t))/w
    r1 = np.array([np.cos(w*t), -1*np.sin(w*t), p1])
    r2 = np.array([np.sin(w*t), np.cos(w*t), p2])
    r3 = np.array([0,0,1])
    return np.array([r1,r2,r3])



### from Angel's hw3
def exp_twist_hat(v,w):
    w1,w2,w3 = tuple(w)
    v1,v2,v3 = tuple(v)
    what = np.array([[0,-w3,w2],[w3,0,-w1],[-w2,w1,0]])
    eWhat = lambda theta: linalg.expm(what*theta)
    wxv = np.cross(w,v)
    wxv = np.array([ [wxv[0]], [wxv[1]], [wxv[2]] ])
    wNP = np.array([[w1],[w2],[w3]])
    vNP = np.array([[v1],[v2],[v3]])
    right = lambda theta: (np.eye(3)-eWhat(theta)).dot(wxv) + (wNP.dot(wNP.T)).dot(vNP)*theta
    
    def matretfunc(theta):
        wexp = eWhat(theta).tolist()
        rt = [ i[0] for i in right(theta).tolist()]
        row1 = wexp[0] + [rt[0]]
        row2 = wexp[1] + [rt[1]]
        row3 = wexp[2] + [rt[2]]
        row4 = [0,0,0,1]
        return np.array([row1,row2,row3,row4])
    return matretfunc



def homog_3d(xi, theta):
    """
    Computes a 4x4 homogeneous transformation matrix given a 3D twist and a 
    joint displacement.
    
    Args:
    xi - (6,) ndarray: the 3D twist
    theta: the joint displacement

    Returns:
    g - (4,4) ndarary: the resulting homogeneous transformation matrix
    """
    if not xi.shape == (6,):
        raise TypeError('xi must be a 6-vector')

    #YOUR CODE HERE
    
    v1,v2,v3,w1,w2,w3 = tuple(xi.tolist())
    w_mag_sq = w1**2 + w2**2 + w3**2
    hat = (exp_twist_hat([v1,v2,v3], [w1,w2,w3])(theta)).tolist()
    hat[0][3] = hat[0][3] / w_mag_sq
    hat[1][3] = hat[1][3] / w_mag_sq
    hat[2][3] = hat[2][3] / w_mag_sq
    return np.array(hat)
    # return g

def prod_exp(xi, theta):
    """
    Computes the product of exponentials for a kinematic chain, given 
    the twists and displacements for each joint.
    
    Args:
    xi - (6,N) ndarray: the twists for each joint
    theta - (N,) ndarray: the displacement of each joint
    
    Returns:
    g - (4,4) ndarray: the resulting homogeneous transformation matrix
    """
    if not xi.shape[0] == 6:
        raise TypeError('xi must be a 6xN')

    #YOUR CODE HERE
    exps = map(lambda tup: homog_3d(tup[0], tup[1]), zip(xi.T, theta.tolist()))
    res = exps[0]
    for i in range(len(exps)):
        if i==0:
            continue
        else:
            res = res.dot(exps[i])
    return res



def twist(tup):
    q,w = tup
    n_w = map(lambda x: -1*x, w)
    v = np.cross(n_w, q)
    vw = v.tolist() + w
    return np.array(vw).T

def problem1_2(arr):
    # t1,t2,t3,t4,t5,t6,t7 = tuple(arr)
    q = [ [.0635,.2598,.1188], [.1106,.3116,.3885], [.1827,.3838,.3881], [.3682,.5684,.3181], [.4417,.6420,.3177], [.6332,.8337,.3067], [.7152,.9158,.3063] ]
    
    w = [ [-.0059,.0113,.9999], [-.7077,.7065,-.0122], [.7065,.7077,-.0038], [-.7077,.7065,-.0122], [.7065,.7077,-.0038], [-.7077,.7065,-.0122], [.7065,.7077,-.0038] ]

    twists = (np.array(map(lambda tup: twist(tup), zip(q,w)))).T
    thetas = np.array(arr)
    left_hand = np.array([[1,0,0,.7957],[0,1,0,.9965],[0,0,1,.3058],[0,0,0,1]])
    return (prod_exp(twists, thetas)).dot(left_hand)
    

#-----------------------------Testing code--------------------------------------
#-------------(you shouldn't need to modify anything below here)----------------

def array_func_test(func_name, args, ret_desired):
    ret_value = func_name(*args)
    if not isinstance(ret_value, np.ndarray):
        print('[FAIL] ' + func_name.__name__ + '() returned something other than a NumPy ndarray')
    elif ret_value.shape != ret_desired.shape:
        print('[FAIL] ' + func_name.__name__ + '() returned an ndarray with incorrect dimensions')
    elif not np.allclose(ret_value, ret_desired, rtol=1e-3):
        print('[FAIL] ' + func_name.__name__ + '() returned an incorrect value')
    else:
        print('[PASS] ' + func_name.__name__ + '() returned the correct value!')

if __name__ == "__main__":
    print('Testing...')

    #Test skew_3d()
    arg1 = np.array([1.0, 2, 3])
    func_args = (arg1,)
    ret_desired = np.array([[ 0., -3.,  2.],
                            [ 3., -0., -1.],
                            [-2.,  1.,  0.]])
    array_func_test(skew_3d, func_args, ret_desired)

    #Test rotation_2d()
    arg1 = 2.658
    func_args = (arg1,)
    ret_desired = np.array([[-0.8853, -0.465 ],
                            [ 0.465 , -0.8853]])
    array_func_test(rotation_2d, func_args, ret_desired)

    #Test rotation_3d()
    arg1 = np.array([2.0, 1, 3])
    arg2 = 0.587
    func_args = (arg1,arg2)
    ret_desired = np.array([[-0.1325, -0.4234,  0.8962],
                            [ 0.8765, -0.4723, -0.0935],
                            [ 0.4629,  0.7731,  0.4337]])
    array_func_test(rotation_3d, func_args, ret_desired)

    #Test hat_2d()
    arg1 = np.array([2.0, 1, 3])
    func_args = (arg1,)
    ret_desired = np.array([[ 0., -3.,  2.],
                            [ 3.,  0.,  1.],
                            [ 0.,  0.,  0.]])
    array_func_test(hat_2d, func_args, ret_desired)

    #Test hat_3d()
    arg1 = np.array([2.0, 1, 3, 5, 4, 2])
    func_args = (arg1,)
    ret_desired = np.array([[ 0., -2.,  4.,  2.],
                            [ 2., -0., -5.,  1.],
                            [-4.,  5.,  0.,  3.],
                            [ 0.,  0.,  0.,  0.]])
    array_func_test(hat_3d, func_args, ret_desired)

    #Test homog_2d()
    arg1 = np.array([2.0, 1, 3])
    arg2 = 0.658
    func_args = (arg1,arg2)
    ret_desired = np.array([[-0.3924, -0.9198,  0.1491],
                            [ 0.9198, -0.3924,  1.2348],
                            [ 0.    ,  0.    ,  1.    ]])
    array_func_test(homog_2d, func_args, ret_desired)

    #Test homog_3d()
    arg1 = np.array([2.0, 1, 3, 5, 4, 2])
    arg2 = 0.658
    func_args = (arg1,arg2)
    ret_desired = np.array([[ 0.4249,  0.8601, -0.2824,  1.7814],
                            [ 0.2901,  0.1661,  0.9425,  0.9643],
                            [ 0.8575, -0.4824, -0.179 ,  0.1978],
                            [ 0.    ,  0.    ,  0.    ,  1.    ]])
    array_func_test(homog_3d, func_args, ret_desired)

    #Test prod_exp()
    arg1 = np.array([[2.0, 1, 3, 5, 4, 6], [5, 3, 1, 1, 3, 2], [1, 3, 4, 5, 2, 4]]).T
    arg2 = np.array([0.658, 0.234, 1.345])
    func_args = (arg1,arg2)
    ret_desired = np.array([[ 0.4392,  0.4998,  0.7466,  7.6936],
                            [ 0.6599, -0.7434,  0.1095,  2.8849],
                            [ 0.6097,  0.4446, -0.6562,  3.3598],
                            [ 0.    ,  0.    ,  0.    ,  1.    ]])
    array_func_test(prod_exp, func_args, ret_desired)

    print('Done!')