# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the {{cookiecutter.license}} License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import cli_command

# TODO: Implement your own commands. The commands below are for illustration purposes only
cli_command(__name__, '{{cookiecutter.package_name}} list', 'azure.cli.command_modules.{{cookiecutter.package_name}}.custom#example_list_command')
