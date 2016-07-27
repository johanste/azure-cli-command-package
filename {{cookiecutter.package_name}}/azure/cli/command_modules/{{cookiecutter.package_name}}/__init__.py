#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
# Add command module logic to this package.

from azure.cli.commands import cli_command

# By importing azure.cli.commands.parameters, we get all the goodness from global parameter
# names and validation (including statement completion) 
from azure.cli.commands.parameters import * 

def example(my_required_arg, my_optional_arg='MyDefault'):
    '''Returns the params you passed in.
    :param str my_required_arg: The argument that is required
    '''
    result = {'a': my_required_arg, 'b': my_optional_arg}
    return result

def example_with_resourcegroup(resource_group_name):
    '''By using the well-known parameter name resource_group_name, you
    will see that you can use -g/--resource-group as the parameter
    name, and (if you are using bash), you get statement completion
    for resource group names - if you have logged in to Azure
    '''
    return dict(name=resource_group_name)

# Register the commands with the CLI     
cli_command('{{cookiecutter.package_name}} example', example)
cli_command('{{cookiecutter.package_name}} examplewithresourcegroup', example_with_resourcegroup)
