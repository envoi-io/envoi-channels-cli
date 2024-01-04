import sys

from envoi.cli import CliApp
from envoi.channels.cli.aws import AwsCommand

import logging

LOG = logging.getLogger(__name__)


class EnvoiChannelsCli(CliApp):
    DESCRIPTION = "Envoi Channels Command Line Utility"
    PARAMS = {
        "log_level": {
            "flags": ['--log-level'],
            "type": str,
            "default": "INFO",
            "help": "Set the logging level (options: DEBUG, INFO, WARNING, ERROR, CRITICAL)"
        },
    }
    SUBCOMMANDS = {
        'aws': AwsCommand
    }


def main():
    cli = EnvoiChannelsCli(auto_exec=False)
    return cli.run()


if __name__ == "__main__":
    sys.exit(main())
