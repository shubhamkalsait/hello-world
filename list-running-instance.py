import boto3

client = boto3.client('ec2')

#getting all regions 
regions = client.describe_regions()['Regions']
for region in regions:
    get_reg_name = region['RegionName']

#creating client object for each region
    client = boto3.client('ec2',region_name = get_reg_name)

#getting running instances
    instances_info = client.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}])['Reservations']

#printing runing instance's id
    for instance in instances_info:
        instance_id = instance['Instances'][0]['InstanceId']
        print("Region:  ",get_reg_name,end="  |  ")
        print('Instance Id: ',instance_id)