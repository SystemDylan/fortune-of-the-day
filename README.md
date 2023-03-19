# Fortune of the Day

A simple Python Flask web application designed to showcase proficiency in AWS technologies and Terraform configuration/management.

## Features

- Built using the Python Flask framework and leveraging multiple AWS services
- Connects to an Amazon DynamoDB table using the Python 'boto3' SDK library
- Retrieves a random "fortune" from the table on each page load using `random.choice()`
- Hosted on an AWS EC2 instance created from a custom, replicable Amazon Linux AMI based on an EBS snapshot
- Utilizes an Auto Scaling group with a Simple Scaling policy, maintaining a minimum of 2 instances and a maximum of 4 instances based on CPU utilization
- Elastic Load Balancer (ELB) handles load balancing across multiple availability zones and acts as a reverse proxy, accepting connections on port 80 and routing to port 5000, where the Flask app listens
- Entire application state created and managed using Terraform
- Terraform configuration file for ELB/ASG automatically deploys a Route 53 CNAME DNS record pointing to the ELB's DNS name
- Access the web app at http://fortune.systemdylan.com/

## SQL Fortune of the Day

- A rebuilt version of the 'fortune of the day' python flask app. Uses a locally hosted MySQL DB instead of an Amazon Dynamo DB
- The application now contacts a SQL database over an Ipsec VPN facilitated between a pfsense firewall and an aws vpc virtual private gateway. All aws vpc and vpc infrastructure was generated and is managed with terraform. The terraform scripts for the environment can be viewed at my terraform-aws repo: https://github.com/SystemDylan/terraform-aws

## Upcoming Features

- SSL certificate implementation
