import os
from mmflyer.Erbach import Erbach


def test_version():
    """Check test data file exists"""
    eb = Erbach()
    data_file = 'tests/test_data/test_model.yml'
    assert os.path.isfile(data_file)
    eb.load_model(data_file)
