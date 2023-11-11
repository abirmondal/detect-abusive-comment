import os
from dotenv import load_dotenv
import pandas as pd
from pandas.core.frame import DataFrame

load_dotenv()

dataset_folder = os.getenv('DATASET_FOLDER')
dataset_name = os.getenv('DATASET_NAME')
dataset_division_folder = os.getenv('DATASET_DIVISION_FOLDER')

train_set = pd.read_csv(
    './'+
    os.path.join(
        dataset_folder,
        dataset_name,
        dataset_division_folder,
        'train.csv'
    ).replace('\\', '/')
)
test_set = pd.read_csv(
    './' +
    os.path.join(
        dataset_folder,
        dataset_name,
        dataset_division_folder,
        'test.csv'
    ).replace('\\', '/')
)
val_set = pd.read_csv(
    './' +
    os.path.join(
        dataset_folder,
        dataset_name,
        dataset_division_folder,
        'val.csv'
    ).replace('\\', '/')
)

def get_dataset(val=True) -> (tuple[DataFrame, DataFrame] | tuple[DataFrame, DataFrame, DataFrame]):
    '''
    Get the dataset from the dataset folder.

    Args:
    * val(bool): If True, returns the validation set also.

    Returns:
    * train_set: Training set
    * test_set: Testing set
    * val_set: Validation set (if val=True)
    '''
    if val == False:
        return train_set, test_set
    else:
        return train_set, test_set, val_set

def get_dataset_details() -> None:
    '''
    Print the details of the dataset.

    Args:
    None

    Returns:
    None
    '''
    train_count = train_set.shape[0]
    test_count = test_set.shape[0]
    val_count = val_set.shape[0]
    total_count = train_count + test_count + val_count
    no_of_digits = len(str(total_count))
    print('Dataset Details:-')
    print('  Dataset Name: %s' % dataset_name)
    print('   Total Count: %s' % str(total_count).rjust(no_of_digits))
    print('     Train Set: %s ( %.1f%% )' %
          (str(train_count).rjust(no_of_digits), train_count/total_count*100))
    print('      Test Set: %s ( %.1f%% )' %
          (str(test_count).rjust(no_of_digits), test_count/total_count*100))
    print('Validation Set: %s ( %.1f%% )' %
          (str(val_count).rjust(no_of_digits), val_count/total_count*100))
