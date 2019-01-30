# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azure_functions_devops_build.constants import LINUX_CONSUMPTION, LINUX_DEDICATED, WINDOWS, NODE, PYTHON, JAVA, DOTNET

# You need to fill in the variables with names of the resources you already have
# When you are finished setting the configs then you can run test.cmd

# The create devops objects setting sets whether the test will run create commands. The default is false
CREATE_DEVOPS_OBJECTS = False

# Specify the name of your already created devops objects
ORGANIZATION_NAME = 'ollys-hck'
PROJECT_NAME = 'cmd-test-2'
SERVICE_ENDPOINT_NAME = ORGANIZATION_NAME + PROJECT_NAME
REPOSITORY_NAME = PROJECT_NAME
BUILD_DEFINITION_NAME = PROJECT_NAME
RELEASE_DEFINITION_NAME = 'release blah'

# Do not change this from default.
POOL_NAME = 'Default'

# Specify the details of your azure functions resource
FUNCTIONAPP_NAME = 'dolk-demo-py-c'
FUNCTIONAPP_TYPE = LINUX_CONSUMPTION
FUNCTIONAPP_LANGUAGE = WINDOWS
STORAGE_NAME = 'dolkdemopyc8827'
RESOURCE_GROUP_NAME = 'dolk-demos'
