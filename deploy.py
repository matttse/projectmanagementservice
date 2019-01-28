import subprocess


def deploy():

    # Set local env variables
    path = 'C:/server/htdocs/websiteDev/'
    front = path + 'frontend/'

    # mid = path + 'middleware/'
    # package = mid + 'package/function.zip'
    # function = mid + 'handle-query.py'
    # zipfile = 'fileb://' + package
    # Set AWS env variables
    s3 = 's3://projectmanagementservice/'
    # lambdaFunction = 'getQuip'
    profile = 'default'
    region = 'us-east-1'

    # Set commands
    s3_cmd = ['aws','s3','sync',front,s3,'--profile',profile]
    # lam_zip_cmd = ['7z','a',package,function]
    # lam_dep_cmd = ['aws','lambda','update-function-code','--function-name',lambdaFunction,'--zip-file', zipfile,'--profile',profile,'--region',region]
    
    print('Deploying site code to S3 Bucket ' + s3 + '...') 
    for path in execute(s3_cmd):
        print(path, end=="")
    print('S3 static site code deployed successfully.')
    
    # print('Zipping function package ' + function + '...')
    # for path in execute(lam_zip_cmd):
        # print(path, end="")

    # print('Deploying Lambda function package to ' + lambdaFunction + '...')
    # for path in execute(lam_dep_cmd):
        # print(path, end="")

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

deploy()
