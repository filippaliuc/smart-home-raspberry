import boto3

region = 'eu-north-1'
access_key = 'AKIAWZLJGPS3B3XAXTFB'
secret_access_key = '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'

cloudwatch = boto3.client('cloudwatch', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)