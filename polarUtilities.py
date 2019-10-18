import sympy as sp

r, theta = sp.symbols('r, theta')

f = sp.Function('f')(r,theta)


def delr_delx():
    return sp.cos(theta)
    
def delr_dely():
    return sp.sin(theta)

def deltheta_delx():
    return -sp.sin(theta)/r

def deltheta_dely():
    return sp.cos(theta)/r



def del_delx(f):
    return delr_delx()*sp.diff(f,r,1) + deltheta_delx()*sp.diff(f,theta,1)

def del_dely(f):
    return delr_dely()*sp.diff(f,r,1) + deltheta_dely()*sp.diff(f,theta,1)

def del2_delx2(f):
    return del_delx(del_delx(f))


def del2_dely2(f):
    return del_dely(del_dely(f))


def polarLaplacian(f):
    return (del2_delx2(f)+del2_dely2(f)).simplify()


def polarbiharmonic(f):
    return polarLaplacian(polarLaplacian(f))


def sigma_xx(f):
    return del2_dely2(f)

def sigma_yy(f):
    return del2_delx2(f)

def sigma_xy(f):
    return -del_delx(del_dely(f))
    
def sigma_rect(f):
    return sp.Matrix([[sigma_xx(f), sigma_xy(f)],[sigma_xy(f), sigma_yy(f)]])
    

Q = sp.Matrix([[sp.cos(theta), sp.sin(theta)],[-sp.sin(theta), sp.cos(theta)]])


def sigma_polar(f):
    return Q*sigma_rect(f)*(Q.T)


def sigma_rr(f):
    return (sigma_polar(f)[0,0]).simplify().expand()

def sigma_tt(f):
    return (sigma_polar(f)[1,1]).simplify().expand()

def sigma_rt(f):
    return (sigma_polar(f)[0,1]).simplify().expand()

def sigma_tr(f):
    return (sigma_polar(f)[1,0]).simplify().expand()
