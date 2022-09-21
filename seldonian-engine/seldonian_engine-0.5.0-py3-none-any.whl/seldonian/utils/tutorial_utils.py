import autograd.numpy as np   # Thinly-wrapped version of Numpy
import pandas as pd

from seldonian.dataset import SupervisedDataSet
from seldonian.parse_tree.parse_tree import ParseTree


def generate_data(num_points,loc_X=0.0,loc_Y=0.0,sigma_X=1.0,sigma_Y=1.0):
    """ Generate 2D random normal data
    
    :param num_points: The number of data points to generate
    :type num_points: int

    :param loc_X: The center of the normal distribution 
        in the X dimension
    :type loc_X: float

    :param loc_Y: The center of the normal distribution 
        in the Y dimension
    :type loc_Y: float

    :param sigma_X: The standard deviation of the normal distribution 
        in the X dimension
    :type sigma_X: float

    :param sigma_Y: The standard deviation of the normal distribution 
        in the Y dimension
    :type sigma_Y: float
    """

    X =     np.random.normal(loc_X, sigma_X, num_points) # Sample x from a standard normal distribution
    Y = X + np.random.normal(loc_Y, sigma_Y, num_points) # Set y to be x, plus noise from a standard normal distribution
    return (X,Y)


def generate_clipped_data(
    num_points,
    loc_X=0.0,
    loc_Y=0.0,
    sigma_X=1.0,
    sigma_Y=1.0,
    clip_min=-3,
    clip_max=3):
    """ Generate 2D random normal data
    
    :param num_points: The number of data points to generate
    :type num_points: int

    :param loc_X: The center of the normal distribution 
        in the X dimension
    :type loc_X: float

    :param loc_Y: The center of the normal distribution 
        in the Y dimension
    :type loc_Y: float

    :param sigma_X: The standard deviation of the normal distribution 
        in the X dimension
    :type sigma_X: float

    :param sigma_Y: The standard deviation of the normal distribution 
        in the Y dimension
    :type sigma_Y: float
    """

    X =     np.random.normal(loc_X, sigma_X, num_points) # Sample x from a standard normal distribution
    Y = X + np.random.normal(loc_Y, sigma_Y, num_points) # Set y to be x, plus noise from a standard normal distribution
    Y = np.clip(Y,clip_min,clip_max)
    return (X,Y)


def make_synthetic_regression_dataset(
    num_points,
    loc_X,
    loc_Y,
    sigma_X,
    sigma_Y,
    include_intercept_term=True,
    clipped=False,
    clip_min=-3,
    clip_max=3):
    if clipped:
        X,Y = generate_clipped_data(
            num_points=num_points,
            loc_X=loc_X,
            loc_Y=loc_Y,
            sigma_X=sigma_X,
            sigma_Y=sigma_Y,
            clip_min=clip_min,
            clip_max=clip_max)
    else: 
        X,Y = generate_data(
            num_points=num_points,
            loc_X=loc_X,
            loc_Y=loc_Y,
            sigma_X=sigma_X,
            sigma_Y=sigma_Y)

    # 2. Define the metadata
    columns = columns=['feature1','label']

    # 3. Make a dataset object
    rows = np.hstack([np.expand_dims(X,axis=1),
        np.expand_dims(Y,axis=1)])
    df = pd.DataFrame(rows,columns=columns)

    dataset = SupervisedDataSet(df,
        meta_information=columns,
        label_column='label',
        include_intercept_term=include_intercept_term)

    return dataset