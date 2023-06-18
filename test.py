import boto3

# Create a CloudWatch client
region = 'eu-north-1'
access_key = 'AKIAWZLJGPS3B3XAXTFB'
secret_access_key = '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'
cloudwatch = boto3.client('cloudwatch', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

def send_metrics_to_cloudwatch(temperature, humidity):
    # Define the namespace for your metrics
    namespace = 'MyApp/Metrics'


    # Define the metric data
    metric_data = [
        {
            'MetricName': 'Temperature',
            'Dimensions': [
                {
                    'Name': 'Location',
                    'Value': 'LivingRoom'
                },
            ],
            'Unit': 'None',
            'Value': temperature
        },
        {
            'MetricName': 'Humidity',
            'Dimensions': [
                {
                    'Name': 'Location',
                    'Value': 'LivingRoom'
                },
            ],
            'Unit': 'None',
            'Value': humidity
        },
    ]

    # Send the metric data to CloudWatch
    response = cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=metric_data
    )

    # Check the response for errors
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('Metrics sent successfully.')
    else:
        print('Error sending metrics to CloudWatch.')

# Usage example
temperature_value = 25.0  # Replace with your temperature value
humidity_value = 60.0  # Replace with your humidity value
send_metrics_to_cloudwatch(temperature_value, humidity_value)
