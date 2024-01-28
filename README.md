# Kivy_Linux_build_helloworld
Debug &amp; record
update in 202401, build Kivy hello-world app successifully.
setting: virtual box, ubuntu 20, anaconda.
Conda environment: python=3.8.18, buildozer=1.5.0
Cython=0.29.1,kivy=2.0.0.
requiremtns in buildozer.spec: requirements = python3==3.8.18,kivy==2.0.0
# Tips:
1. Don't install all the packages in the same time. For example: the apt-install for colab environment.
2. The python version in your virtual environment show be the same corresponding to the buildozer.spec's requirement.
3. Look for suitable Cython's version compatible for the kivy you want to use.
4. When build; the error indicate like: no proper Cython found for install --> it possible the issue from python version, not from Cython. 


