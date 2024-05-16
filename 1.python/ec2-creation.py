import boto3

# Configure AWS credentials (replace with your actual credentials)
access_key_id = "YOUR_ACCESS_KEY_ID"
secret_access_key = "YOUR_SECRET_ACCESS_KEY"
region_name = "YOUR_REGION_NAME"  # e.g., "us-east-1"

# Create a boto3 EC2 client
ec2_client = boto3.client(
    "ec2",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    region_name=region_name
)

# Define the EC2 instance configuration
image_id = "ami-0123456789abcdef0"  # Replace with the desired AMI ID
instance_type = "t2.micro"  # Choose the appropriate instance type
count = 1  # Number of instances to create

# Create the EC2 instance(s)
try:
  response = ec2_client.run_instances(      # run_instances - is a method in this 
      ImageId=image_id, #run_instances method creates one or more EC2 instances based on the provided configuration.
      InstanceType=instance_type,
      MinCount=count,
      MaxCount=count
  )

  # Print instance information
  for instance in response["Instances"]:
      print(f"Instance ID: {instance['InstanceId']}")
      print(f"State: {instance['State']['Name']}")
      print("-" * 20)

except Exception as e:
  print(f"Error creating EC2 instance: {e}")


# Explanation:

# Import the boto3 library: This library provides Python interfaces for interacting with various AWS services, including EC2.
# Configure AWS Credentials: Replace the placeholders with your actual AWS access key ID and secret access key.
# Create an EC2 Client: This line creates a client object to interact with the EC2 service.
# Define EC2 Instance Configuration:
# image_id: Replace with the ID of the Amazon Machine Image (AMI) you want to use.
# instance_type: Choose the appropriate instance type based on your resource requirements.
# count: Specify the number of instances you want to create.
# Create the EC2 Instance(s):
# The run_instances method creates one or more EC2 instances based on the provided configuration.
# Handle Errors: The code includes a try-except block to catch potential exceptions during instance creation and print an error message.
# Print Instance Information: The code iterates through the response from run_instances and prints the instance ID and state for each created instance.
# Important Notes:

# Security: This code snippet focuses on creating an EC2 instance. Remember to configure security groups and other access rules appropriately for your instance.
# Best Practices: Refer to the AWS documentation for best practices on creating and managing EC2 instances: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html
# Cost: Launching EC2 instances incurs charges. Ensure you have a proper billing plan in place.