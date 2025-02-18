import os
import platform
from setuptools import setup, Extension
from distutils.sysconfig import get_python_inc


# python include dir
py_include_dir = os.path.join(get_python_inc())
# cpp flags
cpp_args = ['-std=c++17']
# include directories
include_dirs = [py_include_dir, './SEAL-Python/pybind11/include', './SEAL-Python/SEAL/native/src', './SEAL-Python/SEAL/build/native/src']
# library path
#extra_objects = ['./SEAL/build/lib/libseal-3.6.a']
extra_objects = ['./SEAL-Python/SEAL/native/lib/libseal.a']
# available wrapper: src/wrapper.cpp, src/wrapper_with_pickle.cpp
wrapper_file = 'SEAL-Python/src/wrapper.cpp'

if(platform.system() == "Windows"):
    cpp_args[0] = '/std:c++latest'  # /std:c++1z
    extra_objects[0] = './SEAL-Python/SEAL/build/lib/Release/seal-3.3.2.lib'

if not os.path.exists(extra_objects[0]):
    print('Can not find the seal lib,')
    print('Compile the seal lib first or check the path.')
    exit(1)

ext_modules = [
    Extension(
        name='seal',
        sources=[wrapper_file, 'SEAL-Python/src/base64.cpp'],
        include_dirs=include_dirs,
        language='c++',
        extra_compile_args=cpp_args,
        extra_objects=extra_objects,
    ),
]

setup(
    name='seal',
    version='3.3.2',
    author='Huelse',
    author_email='huelse@oini.top',
    description='Python wrapper for the Microsoft SEAL',
    url='https://github.com/Huelse/SEAL-Python',
    license='MIT',
    ext_modules=ext_modules,
)
