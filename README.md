<h1 align="center">Applied Elasticity</h1>
<h2 align="center">Mechanical Engineering Department, Indian Institute of Technology Kharagpur</h2>

[![DOI](https://zenodo.org/badge/215966846.svg)](https://zenodo.org/badge/latestdoi/215966846)

This is a repository of Jupyter Notebook files that are used to teach the second half of the course "Applied Elasticity" (ME40605/ME60401) in the Autumn Semester. This course is taken by the 1st year postgraduate students of Mechanical Engineering with specialization in "Mechanical Systems Design". It is also taken by the students of fourth year Dual Degree with the same specialization. It is also taken by a few Ph.D. students towards completion of their course work requirements.

Since the derivation of the biharmonic equation in polar coordinates is rather long, I thought of using Jupyter Notebook and SymPy to programmatically derive the expressions. 

## 2D Elasticity in Polar Coordinates

We follow the development of the ideas as presented in the classic "Theory of Elasticity" by Timoshenko and Goodier, 3rd edition. 

* The file ["PolarCoordinates_Definitions.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/PolarCoordinates_Definitions.ipynb) is where all the transformations from the rectangular Cartesian coordinate system to the polar coordinate system required to obtain the biharmonic equation are set up. The stresses are also transformed from the rectangular Cartesian coordinate system to the polar coordinate system. <br><br> Here is the binder link to launch this file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=PolarCoordinates_Definitions.ipynb)

<br>

* The functions defined in the file ["PolarCoordinates_Definitions.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/PolarCoordinates_Definitions.ipynb) are collected in [polarUtilities.py](https://github.com/jeevanjyoti4/elasticity/blob/master/polarUtilities.py). These definitions will be invoked in the subsequent files by importing `polarUtilities`. 

<br>

* The file ["Axisymmetric_PressureVessel.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/Axisymmetric_PressureVessel.ipynb) addresses the set-up of axisymmetric problems with particular focus on the solution of the thick-walled pressure vessel problem. This file uses the [polarUtilities.py](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/polarUtilities.py) file. <br><br> Here is the binder link to launch this file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=Axisymmetric_PressureVessel.ipynb) 

<br>


* The file ["CurvedBar_PureBending_onlystress.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/CurvedBar_PureBending_onlystress.ipynb) addresses the problem of pure bending of a curved bar. This file uses the [polarUtilities.py](https://github.com/jeevanjyoti4/elasticity/blob/master/polarUtilities.py) file. <br><br>Here is the binder link to launch this file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=CurvedBar_PureBending_onlystress.ipynb)



<!--
<br>

* The file ["CurvedBar_HorizontalLoad.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/CurvedBar_HorizontalLoad.ipynb) addresses the problem of a curved bar with a horizontal shear load at one end with the other end clamped. This file too uses the [polarUtilities.py](https://github.com/jeevanjyoti4/elasticity/blob/master/polarUtilities.py) file. <br><br>Here is the binder link to launch the third file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=CurvedBar_HorizontalLoad.ipynb)

<br>

* The fourth file ["Plate-CircularHole.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/Plate-CircularHole.ipynb) addresses the classic problem of a plate with a small circular hole subjected to uniaxial tensile load. This file again uses the [polarUtilities.py](https://github.com/jeevanjyoti4/elasticity/blob/master/polarUtilities.py) file.  <br><br>Here is the binder link to launch the fourth file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=Plate-CircularHole.ipynb)

5. The fifth file ["Flamant.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/Flamant.ipynb) addresses another classic problem of a vertical point loading on an infinite half space. This file uses the [polarUtilities.py](https://github.com/jeevanjyoti4/elasticity/blob/master/polarUtilities.py) file. <br><br>Here is the binder link to launch the fifth file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=Flamant.ipynb) 
   
-->
