import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='exbook',
<<<<<<< HEAD
     version='0.0.3',
=======
     version='v0.0.4',
>>>>>>> 5f278494610f2ccba113e1a7ed0751d13db8d159
     author="Peng Xiong",
     author_email="xiongpengnus@gmail.com",
     description="Exercises for Python coding",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/XiongPengNUS/exbook",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
     install_requires=[
         "pandas >= 0.25.0",
         "ipython >= 7.0.0",
     ]
 )
