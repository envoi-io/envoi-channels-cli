import boto3


def create_channel(**kwargs):
    client = boto3.client('ivs')

    authorized = kwargs.get('authorized', None)
    channel_name = kwargs.get('channel_name', None)
    channel_type = kwargs.get('channel_type', 'BASIC')
    insecure_ingest = kwargs.get('insecure_ingest', None)
    latency_mode = kwargs.get('latency_mode', 'NORMAL')
    recording_configuration_arn = kwargs.get('recording_configuration_arn', None)

    create_channel_args = {
        "type": channel_type,
        "latencyMode": latency_mode
    }

    if channel_name is not None:
        create_channel_args['name'] = channel_name

    if authorized is not None:
        create_channel_args['authorized'] = authorized

    if insecure_ingest is not None:
        create_channel_args['insecureIngest'] = insecure_ingest

    if recording_configuration_arn:
        create_channel_args['recordingConfigurationArn'] = recording_configuration_arn

    # authorized=True | False,
    # insecureIngest=True | False,
    # latencyMode='NORMAL' | 'LOW',
    # name='string',
    # preset='HIGHER_BANDWIDTH_DELIVERY' | 'CONSTRAINED_BANDWIDTH_DELIVERY',
    # recordingConfigurationArn='string',
    # tags={
    #     'string': 'string'
    # },
    # type='BASIC' | 'STANDARD' | 'ADVANCED_SD' | 'ADVANCED_HD'
    response = client.create_channel(**create_channel_args)
    return response


def delete_channel(**kwargs):
    ...


def update_channel(**kwargs):
    ...
