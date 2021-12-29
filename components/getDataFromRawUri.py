import kfp
import kfp.dsl as dsl
import kfp.components as components
from kfp.components import create_component_from_func


@components.create_component_from_func
def GetRawData(val):
    import requests
    data = requests.get(val)
    print("Extracted Raw Data")
    return data
   
if __name__ == '__main__':
    create_component_from_func(func=GetRawData,base_image='python:slim',output_component_file='getRawData.yaml')
