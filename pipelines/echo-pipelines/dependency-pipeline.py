import kfp
import kfp.dsl as dsl

import kfp.components as components

@components.create_component_from_func
def printString(val):
    print(val)

@dsl.pipeline(
  name='my-pipeline',
  description='My ML Pipeline.'
)
def file_passing_pipelines():
    step1 = dsl.ContainerOp(
        name="echo",
        image="alpine",
        command=["sh", "-c"],
        arguments=["echo Hi Kubeflow"],
    )
    step2 = printString("Hello, From component")
    step2.after(step1)

   
if __name__ == '__main__':
    # Compiling the pipeline
    kfp.compiler.Compiler().compile(file_passing_pipelines, __file__ + '.yaml')
