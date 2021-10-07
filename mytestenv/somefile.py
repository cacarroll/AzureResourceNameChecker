import os
# import check_name_availability
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.storage.models import (
    StorageAccountCreateParameters,
    StorageAccountUpdateParameters,
    Sku,
    SkuName,
    Kind
)

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
keyvault_client = KeyVaultManagementClient(credential, subscription_id)

storage_account_name='cstorageaccount11'
resource_group_name='python'

storage_accounts = ['ccstorage001', 'ccstorage002', 'ccstorage003']

# for sa in storage_accounts:
#     storage_client.storage_accounts.begin_create(
#         resource_group_name,
#         sa,
#         StorageAccountCreateParameters(
#             sku=Sku(name=SkuName.standard_ragrs),
#             kind=Kind.storage,
#             location='eastus2',
#             enable_https_traffic_only=True
#         )
#     )

poller = keyvault_client.vaults.begin_create_or_update(
    resource_group_name,
    'testvaultacb19',
    {
        'location': 'eastus2',
        'properties': {
            'sku': {
                'family': 'A',
                'name':'standard'
            },
            'tenantId': AZURE_TENANT_ID,
            'enabledForDeployment':'true',
            'enableRbacAuthorization':'true'
        }
    }
)

kv_result = poller.result()

print(f"Provisioned key vault {kv_result.name} in location {kv_result.location}")

keyvault_client.vaults.delete(resource_group_name,'testvaultacb19')

# storage_client.storage_accounts.check_name_availability(storage_account_name)

# storage_client.storage_accounts.check_name_availability()

# check_name_availability.storage(storage_client, 'cstorageaccount10')