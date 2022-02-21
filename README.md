# Homomorphic PCA
This repository focuses on performing PCA on encrypted data. It uses [CKKS homomorphic scheme](https://eprint.iacr.org/2016/421.pdf) to perform computations on encrypted data.


To use this repository:

### Download Homomorphic_PCA
git clone https://github.com/pandasamanvaya/Homomorphic_PCA.git

cd Homomorphic_PCA

### Download Microsoft SEAL-Python
git clone https://github.com/Huelse/SEAL-Python.git

cd SEAL-Python

git checkout 3.3.2

### Compile Microsoft SEAL
cd SEAL

cd native/src

mkdir build

cd build

cmake ..

make


### Compile Microsoft SEAL-Python
goto SEAL-Python directory

cd ../../

cd SEAL-Python/src

python3 setup.py build_ext -i

### Compile pca.py application
 goto to Homomorphic_PCA directory
 
cd ../

python3 setup.py build

### run Homorphic_PCA

python3 pca.py

For implementing CKKS homomorphic scheme, we have used SEAL-Python(python binding for the [Microsoft SEAL library](https://github.com/microsoft/SEAL))
Dependencies required for this repository are:-
* [Seal-Python](https://github.com/Huelse/SEAL-Python)
* PIL
* sklearn

The ```read_data.py``` file supports reading of 7 datasets that were used for experimentation. The [Yale face](http://vision.ucsd.edu/content/yale-face-database) dataset has been provided in the repository. Other datasets that are supported are:-
* [Parkinsons Telemonitoring](https://archive.ics.uci.edu/ml/datasets/parkinsons)
* [Air Quality](https://archive.ics.uci.edu/ml/datasets/Air+Quality)
* [Wine Quality(both red and white)](https://archive.ics.uci.edu/ml/datasets/wine+quality)
* [MNIST](http://yann.lecun.com/exdb/mnist/)
* [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist)
