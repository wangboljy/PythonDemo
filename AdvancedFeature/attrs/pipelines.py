from attrs import pipelineconf
import sys

__import__("handlers")

pipeline = pipelineconf.conf

input_pool = [1, 2, 3]

for handlerName in pipeline:
    handler = getattr(sys.modules["handlers"], handlerName)
    input_pool = handler(input_pool)

print(input_pool)
