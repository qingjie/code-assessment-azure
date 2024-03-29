import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
import sys


def create_client():
    try:
        return ResourceManagementClient(*get_credentials())
    except Exception:
        print('Unauthorized.')
        sys.exit(1)


def get_credentials():
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

    credentials = ServicePrincipalCredentials(
        client_id=os.environ["AZURE_CLIENT_ID"],
        secret=os.environ["AZURE_CLIENT_SECRET"],
        tenant=os.environ["AZURE_TENANT_ID"])

    return credentials, subscription_id