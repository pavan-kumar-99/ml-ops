import kfp
import kfp.dsl as dsl
import kfp.components as components
from kfp.components import create_component_from_func

dataset_op = components.load_component_from_url(
    'https://raw.githubusercontent.com/pavan-kumar-99/ml-ops/master/components/getRawData.yaml'
)

@components.create_component_from_func
def SplitTrainTest():
    from sklearn.model_selection import train_test_split
    dataset_csv_op = dataset_op().output
    dataset = pd.read_csv(dataset_csv_op)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
    return X_train
   
if __name__ == '__main__':
    create_component_from_func(func=SplitTrainTest,base_image='python:slim',output_component_file='./components/test-train.yaml')
