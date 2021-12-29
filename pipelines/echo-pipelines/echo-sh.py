import kfp
import kfp.dsl as dsl


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

   
if __name__ == '__main__':
    # Compiling the pipeline
    kfp.compiler.Compiler().compile(file_passing_pipelines, __file__ + '.yaml')
