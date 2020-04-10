<h1 align="center">Applied Elasticity</h1>
<h2 align="center">Mechanical Engineering Department, Indian Institute of Technology Kharagpur</h2>

[![DOI](https://zenodo.org/badge/215966846.svg)](https://zenodo.org/badge/latestdoi/215966846)

This is a repository of Jupyter Notebook files that were used to teach the second half of the course "Applied Elasticity" (ME40605/ME60401) in Autumn, 2019. This course is taken by the 1st year postgraduate students of Mechanical Engineering with specialization in "Mechanical Systems Design". It is also taken by the students of fourth year Dual Degree with the same specialization. It is also taken by a few Ph.D. students towards completion of their course work requirements.

Since the derivation of the biharmonic equation in polar coordinates is rather long, I thought of using Jupyter Notebook and SymPy to programmatically derive the expressions. 

We followed the development of the ideas as presented in the classic "Theory of Elasticity" by Timoshenko and Goodier, 3rd edition. 

1. The first file ["Defns_and_PressureVessel.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/Defns_and_PressureVessel.ipynb) is where all the transformations from the rectangular Cartesian coordinate system to the polar coordinate system required to obtain the biharmonic equation are set up. The stresses are also transformed from the rectangular Cartesian coordinate system to the polar coordinate system. Then these defintions are used to solve the thick-walled pressure vessel problem. <br><br> Here is the binder link to launch the first file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=Defns_and_PressureVessel.ipynb)

<br>

2. The second file ["CurvedBar_PureBending.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/CurvedBar_PureBending.ipynb) addresses the problem of pure bending of a curved bar. Unlike the first file, in this second file we do not write out all the definitions to set up the biharmonic equation and the stress components in polar coordinates. Instead we copy all those definitions from the first file in a separate Python file called [polarUtilities.py](https://github.com/jeevanjyoti4/elasticity/blob/master/polarUtilities.py) and then from within "CurvedBar_PureBending.ipynb" import the contents of this separate Python file. <br><br>**Important:** If one wishes to download this file and run it locally, the [polarUtilities.py](https://github.com/jeevanjyoti4/elasticity/blob/master/polarUtilities.py) must be downloaded too and stored in the same folder. <br><br>Here is the binder link to launch the second file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=CurvedBar_PureBending.ipynb)

<br>

3. The 3rd file ["CurvedBar_HorizontalLoad.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/CurvedBar_HorizontalLoad.ipynb) addresses the problem of a curved bar with a horizontal shear load at one end with the other end clamped. This file too uses the [polarUtilities.py](https://github.com/jeevanjyoti4/elasticity/blob/master/polarUtilities.py) file. <br><br>Here is the binder link to launch the third file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=CurvedBar_HorizontalLoad.ipynb)

<br>

4. The fourth file ["Plate-CircularHole.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/Plate-CircularHole.ipynb) addresses the classic problem of a plate with a small circular hole subjected to uniaxial tensile load. This file again uses the [polarUtilities.py](https://github.com/jeevanjyoti4/elasticity/blob/master/polarUtilities.py) file.  <br><br>Here is the binder link to launch the fourth file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=Plate-CircularHole.ipynb)

5. The fifth file ["Flamant.ipynb"](https://nbviewer.jupyter.org/github/jeevanjyoti4/elasticity/blob/master/Flamant.ipynb) addresses another classic problem of a vertical point loading on an infinite half space. This file uses the [polarUtilities.py](https://github.com/jeevanjyoti4/elasticity/blob/master/polarUtilities.py) file. <br><br>Here is the binder link to launch the fifth file: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeevanjyoti4/elasticity/master?filepath=Flamant.ipynb) 
