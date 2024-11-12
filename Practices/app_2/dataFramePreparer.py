import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from customOneHotEncoder import CustomOneHotEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
# Transformador que prepara todo el DataSet llamado Pipelines y transformadores personalizados

# Construccion de un pipeline para los atributos numericos
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy = "median")),
    ('rbst_scaler', RobustScaler())
])
class DataFramePreparer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._full_pipeline = None
        self._columns = None
    def fit(self, X, y = None):
        num_attribs = list(X.select_dtypes(exclude = ['object']))
        cat_attribs = list(X.select_dtypes(include = ['object']))
        self._full_pipeline = ColumnTransformer([
            ("num", num_pipeline, num_attribs),
            ("cat", CustomOneHotEncoder(), cat_attribs),
        ])
        self._full_pipeline.fit(X)
        self._columns = pd.get_dummies(X).columns
        return self
    def transform(self, X, y = None):
        X_copy = X.copy()
        X_prep = self._full_pipeline.transform(X_copy)
        return pd.DataFrame(X_prep, columns = self._columns, index = X_copy.index)