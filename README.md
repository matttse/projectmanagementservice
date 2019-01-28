# Project Management Service

Visit Production at [Project Management Service](http://projectmanagementservice.s3-website-us-east-1.amazonaws.com/index.html)

[Python](https://www.python.org/downloads/) and the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) for using the deploy

Approved keys can deploy to the site code to the bucket using:
```
s3 sync [LOCAL-PATH] s3://projectmanagementservice/
```