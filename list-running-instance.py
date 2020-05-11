import boto3        #python library for aws

ec2_obj = boto3.client('ec2')           #contain describe_instances() method
ec2_obj1 = boto3.resource('ec2')        #contain Instance() method 
result = ec2_obj.describe_instances() 
reservation = result['Reservations']    #describe_instance() returns big nested dictionary
                                        #we search dictionary for desired output

for i in range(len(reservation)):
    temp = reservation[i]
    instances = temp['Instances']
    temp = instances[0]
    instance_id = temp['InstanceId']
    instance = ec2_obj1.Instance(instance_id)
    temp_instance_state = instance.state
    if temp_instance_state['Name']=='running':
        print('Instance ID {} : {}'.format(i+1,instance_id), end="    ")
        print('Availability Zone : {}'.format(temp['Placement']['AvailabilityZone']))

