# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the {{cookiecutter.license}} License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Add command module logic to this package.

def load_params(command):
    import azure.cli.command_modules.{{cookiecutter.package_name}}._params

def load_commands():
    import azure.cli.command_modules.{{cookiecutter.package_name}}.commands