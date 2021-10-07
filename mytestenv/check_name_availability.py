#create class

# Storage Account
def storage (storage_client, storage_account_name):
    #storage_account_name = 'invalid-or-used-name'
    availability = storage_client.storage_accounts.check_name_availability(storage_account_name)
    print('The storage account account {} is available: {}'.format(storage_account_name, availability.name_available))
    print('Reason: {}'.format(availability.reason))

def key_vault (key_vault_client, RESOURCE_GROUP, key_vault_name):
    if key_vault_client.resources.check_existence(RESOURCE_GROUP, 'Microsoft.KeyVault',
                                  '',
                                  'vaults',
                                  key_vault_name,
                                  '2021-04-01'):
        print (f"Key Vault {key_vault_name} exits ")
    else:
        print (f"Key Vault {key_vault_name} NOT exits ")

# test merge / delete
# commit 2
# keyvault base name check
# 23 characters or less
# no more than 1 hypen
