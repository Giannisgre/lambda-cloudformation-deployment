# lambda-cloudformation-deployment

Lambda function for CloudFormation stack deployment from an S3 bucket.

You need to provide the URL for the template located in an S3 bucket, the desired stack name and to modify the explicit stack capabilities declaration.

**Important:** You must make sure that your lambda function has the required permissions for the resources and actions of the CloudFormation template.

## Capabilities

The possible values are **CAPABILITY_IAM**, **CAPABILITY_NAMED_IAM** and **CAPABILITY_AUTO_EXPAND**.
For more information, see [AWS documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html#API_CreateStack_RequestParameters)


