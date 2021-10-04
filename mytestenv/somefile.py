import os
# import check_name_availability
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

subscription_id="0a7ac580-9e64-426b-a0bd-6cd969e735c3"
AZURE_TENANT_ID="72f988bf-86f1-41af-91ab-2d7cd011db47"
credential = AzureCliCredential()

# def get_credentials():
#     subscription_id = os.environ.get(
#         'AZURE_SUBSCRIPTION_ID',
#         '11111111-1111-1111-1111-111111111111')  # your Azure Subscription Id
#     credentials = ServicePrincipalCredentials(
#         client_id=os.environ['AZURE_CLIENT_ID'],
#         secret=os.environ['AZURE_CLIENT_SECRET'],
#         tenant=os.environ['AZURE_TENANT_ID']
#     )
#     return credentials, subscription_id

# credentials, subscription_id = get_credentials()

resource_client = ResourceManagementClient(credential, subscription_id)
storage_client = StorageManagementClient(credential, subscription_id)

# check_name_availability.storage('cstorageaccount10')