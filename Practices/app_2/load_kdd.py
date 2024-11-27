import arff
import pandas as pd
import numpy as np


def load_kdd_dataset(data_path):
    """Lectura del DataSet NSL-KDD."""
    with open(data_path, 'r') as train_set:
        dataset = arff.load(train_set)
    attributes = [attr[0] for attr in dataset["attributes"]]
    return pd.DataFrame(dataset["data"], columns = attributes)