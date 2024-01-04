from envoi.cli import CliCommand
from envoi.channels.cli.aws.ivs import IvsCommand


class AwsCommand(CliCommand):
    DESCRIPTION = "AWS Related Commands"
    SUBCOMMANDS = {
        'ivs': IvsCommand
    }