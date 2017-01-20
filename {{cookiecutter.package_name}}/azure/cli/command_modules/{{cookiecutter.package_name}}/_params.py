# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the {{cookiecutter.license}} License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azure.cli.core.commands import register_cli_argument

register_cli_argument('{{cookiecutter.package_name}}', 'required_parameter', help='You can override the help for a parameter', options_list=('--another-alias-for-required', '--req', '-r'))

