
def extract_data(filePos):
    import pandas as pd
    import numpy as np

    pdData = pd.read_csv(filePos)
    data = pdData.to_numpy()
    return data
