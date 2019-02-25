def handler(event, context):

    try:
        instance_id = event['instance-id']
        ec2_client = Ec2Client()
        tags = ec2_client.get_tags(instance_id)

        if tags.get('DieWithDignity') != 'True':
            return

        attributes = {f'{key}': value for key, value in tags.items()}
        attributes['instance_id'] = instance_id

    except Exception as ex:
        print("Error while running lambda: %s", str(ex))
        raise
