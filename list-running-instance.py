import boto3

client = boto3.client('ec2')

#getting all regions 
regions = client.describe_regions()['Regions']
for reg in regions:
    get_reg_name = reg['RegionName']

    #creating client object for each region
    client = boto3.client('ec2',region_name = get_reg_name)

    #getting running instances
    instances_info = client.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}])['Reservations']

    #printing runing instance's id
    for ins in instances_info:
        instance_id = ins['Instances'][0]['InstanceId']
        print("Region:  ",get_reg_name,end="  |  ")
        print('Instance Id: ',instance_id)

        #stop running instances
        #resource = boto3.resource('ec2',region_name=get_reg_name)
        #instance = resource.Instance(instance_id)

        #instance.stop()
        client.stop_instances(InstanceIds=[instance_id])
    