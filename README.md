# xrayPyExamplesLambda

AWS  [X-Ray](https://aws.amazon.com/xray/) is a service that helps developers debug, instrument, and performance tune applications.
This example demostrates how to use the AWS [X-Ray SDK] (http://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python.html) for Python. to instrument a "mock" application.

## Introduction

First, add two directives to your Python source code

```python
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch
```

Second, install the required depedency

```bash
pip install aws-xray-sdk
pip3 install aws-xray-sdk
```

Third, wrap sections of your code in subsegements like this:

```python
subsegment = xray_recorder.begin_subsegment('subsegment_name')

# code here...

xray_recorder.end_subsegment()
```
## Testing

Lambda functions can be invoked either Asynchronously or Synchronously. To invoke your Lambda function in Async mode specify the --invocation-type flag Event:

```bash
aws lambda invoke --function-name xrayPyTest --invocation-type Event out.txt
```
This X-Ray Trace shows a Lambda function running in Async mode for the first time, with a Cold Start. Notice the Dwell time under AWS::Lambda and the overall duration was just under 800ms.
![Async Cold start](media/Async-cold.png)

This X-Ray Trace shows a Lambda function runnning when Warm. Notice the overall duration was under 350ms.
![Async Cold start](media/Async-warm.png)

To invoke your function in Sync, remove the --invoication-type flag, it will default to RequestResponse

```bash
aws lambda invoke --function-name xrayPyTest  out.txt
```

This X-Ray trace shows a Lambda function running in Sync mode for the first time, with a Cold Start. Notice the Initialization record under AWS::Lambda::Function and overall function duration of 1.3s.
![Sync Cold start](media/Sync-cold.png)

This X-Ray trace shows a Lambda function running when Warm. Notice there is no Initialization and the function runs under 550ms.
![Sync Warm start](media/Sync-warm.png)

## Resources
