# HRS 

This repository contains is for HRS, including Infrastructure, Automation, and Coding Projects.

# Projects Folder Structure

 ```bash
.
├── README.md
├── automation
│   ├── README.md
│   └── gitlab-ci.yaml
├── coding
│   ├── README.md
│   └── redis_to_s3_exporter.py
└── infrastructure
    ├── README.md
    ├── infrastructure_diagram.png
    ├── main.tf
    ├── modules
    │   ├── alb
    │   │   ├── main.tf
    │   │   ├── outputs.tf
    │   │   └── variables.tf
    │   ├── ecs
    │   │   ├── main.tf
    │   │   ├── outputs.tf
    │   │   └── variables.tf
    │   ├── route53
    │   │   ├── main.tf
    │   │   ├── outputs.tf
    │   │   └── variables.tf
    │   └── vpc
    │       ├── main.tf
    │       ├── outputs.tf
    │       └── variables.tf
    ├── outputs.tf
    ├── provider.tf
    └── variables.tf

  ```

  


## Infrastructure 

This project showcases Infrastructure as Code (IaC) implementation using Terraform to automate AWS infrastructure provisioning for deploying Java-based microservices. By defining infrastructure components such as VPC, ECS, ALB, and Route 53, it ensures consistent, scalable, and repeatable deployments, enhancing efficiency and reliability in managing cloud resources.

## Automation Test

The Automation focuses on creating a CI/CD pipeline which automates the process of building, testing, and deploying containerized Java applications. It includes stages for compiling Java code, running tests, and deploying the application to various environments such as AWS Lambda, Amazon EKS, or Amazon ECS. The pipeline leverages Docker for containerization, ensuring consistency across different environments. By automating these tasks, the pipeline streamlines the software delivery process, enhances collaboration among development and operations teams, and accelerates the release cycle of Java applications.

## Coding

The Coding involves building a basic tool in Python:
The ElastiCache to S3 Data Exporter is a Python Project designed to automate the process of exporting data from Amazon ElastiCache for Redis to Amazon S3. Amazon ElastiCache is a fully managed in-memory data store service provided by AWS, while Amazon S3 is a scalable object storage service. This project aims to bridge the gap between these two services by facilitating the seamless transfer of data from ElastiCache to S3.


