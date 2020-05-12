import boto3

ec2 = boto3.client('ec2')

all_regions = ec2.describe_regions()['Regions']
for region in all_regions:
    reg=region['RegionName']
    client = boto3.client('ec2',region_name=reg)
    volume= client.describe_volumes(Filters=[{'Name':'status','Values':['available']}])['Volumes']
    for vols in volume:
        print(vols['AvailabilityZone'])
        client.delete_volume(VolumeId=vols['VolumeId'])
        

