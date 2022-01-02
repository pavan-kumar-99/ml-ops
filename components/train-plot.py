import kfp
import kfp.dsl as dsl
import kfp.components as components
from kfp.components import create_component_from_func

traintest_op = components.load_component_from_url(
    'https://raw.githubusercontent.com/pavan-kumar-99/ml-ops/master/components/test-train.yaml'
)

@components.create_component_from_func
def TrainPlot():
    from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix, mean_squared_error, mean_absolute_error, explained_variance_score
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    plt.scatter(X_train, y_train, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title('Salary vs Experience (Training set)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.show()

    plt.plot(y_pred, y_test)

    plt.scatter(X_test, y_test, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title('Salary vs Experience (Test set)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.show()

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    evs = explained_variance_score(y_test, y_pred) 


    metrics = {"mse":mse,
            "mae":mae,
            "evs":evs
    }

    print(X_train)
    print(params)
    print(metrics)
   
if __name__ == '__main__':
    create_component_from_func(func=TrainPlot,base_image='python:slim',output_component_file='./components/train-plot.yaml')
