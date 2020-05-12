import boto3

client = boto3.client('ec2')

#Fetching instances information with adding filter for running instances
all_data_temp = client.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}])

#getting instance id from all data fetched earlier
#reservation_temp stores list of instance_info
reservation_temp = all_data_temp['Reservations']
for i in range(len(reservation_temp)):
    instance_id = reservation_temp[i]['Instances'][0]['InstanceId']
    print(instance_id)



