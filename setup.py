from setuptools import setup
import os

setup(
    name="evaluate_classification_ml",
    version="0.1.0",
    author="BELBIN BENO RM",
    author_email="belbin.datascientist@gmail.com",
    description="A comprehensive AutoML-lite framework for evaluating multiple scikit-learn classifiers with resource guarding.",
    long_description="A utility to automate the evaluation of 30+ classification models, including resource management for RAM and execution time.",
    url="https://github.com/BELBINBENORM/evaluate-classification-ml",
    py_modules=["Evaluate_Classification"],
    install_requires=[
        "pandas",
        "scikit-learn",
        "joblib",
        "psutil",
        "xgboost",
        "lightgbm",
        "catboost"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.8',
)
