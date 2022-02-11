import os
import boto3

#Modify the values below to configure the function
s3_template_url = '' #Input the S3 url for the template as a string. Example format: 'https://bucketname.s3.region.amazonaws.com/path/to/json-or-yaml-template'
stack_name = 'my-cloudformation-stack-name' #Name of the stack
capabilities = ['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM', 'CAPABILITY_AUTO_EXPAND'] #Explicit stack capabilities declaration

def lambda_handler(event, context):
    print("Launching CloudFormation stack:")
    launch_stack()
  
def launch_stack():
    cfn_client = boto3.client('cloudformation') #Create a CloudFormation boto3 client
    
    try:
        #Create the stack according to the configuration on lines 5-7
        stackdata = cfn_client.create_stack(
            StackName=stack_name,
            TemplateURL=s3_template_url,
            Capabilities=capabilities
        )
    except Exception as e:
        print(str(e))
