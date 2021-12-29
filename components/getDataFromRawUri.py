import kfp
import kfp.dsl as dsl
import kfp.components as components
from kfp.components import create_component_from_func


@components.create_component_from_func
def GetRawData(val: str = 'https://raw.githubusercontent.com/srafay/Machine_Learning_A-Z/master/Part%202%20-%20Regression/Section%204%20-%20Simple%20Linear%20Regression/Salary_Data.csv') -> str:
    import requests
    data = requests.get(val)
    print("Extracted Raw Data")
    return data
   
if __name__ == '__main__':
    create_component_from_func(func=GetRawData,base_image='python:slim',output_component_file='getRawData.yaml')
