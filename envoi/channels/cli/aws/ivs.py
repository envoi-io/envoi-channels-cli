import json

from envoi.cli import CliCommand
from envoi.channels.aws.ivs import create_channel


class CreateChannel(CliCommand):
    DESCRIPTION = "Amazon IVS Create Channel"
    PARAMS = {
        "channel_name": {
            "required": True
        },
        "authorized": {
            "type": bool,
            "default": False
        },
        "channel_type": {
            "choices": ['BASIC', 'STANDARD', 'ADVANCED_SD', 'ADVANCED_HD'],
            "default": 'BASIC'
        },
        "insecure_ingest": {
            "action": "store_false",
            "default": True
        },
        "latency_mode": {
            "choices": ['NORMAL', 'LOW'],
            "default": 'NORMAL'
        },
        "recording_configuration_arn": {
            "type": str,
            "required": False
        },
    }

    def run(self, opts=None):
        if opts is None:
            opts = self.opts
        response = create_channel(**vars(opts))
        if 'channel' in response:
            response_to_print = response['channel']
        else:
            response_to_print = response

        print(json.dumps(response_to_print, indent=4))


class IvsCommand(CliCommand):
    DESCRIPTION = "Amazon IVS"
    SUBCOMMANDS = {
        "create-channel": CreateChannel
    }
