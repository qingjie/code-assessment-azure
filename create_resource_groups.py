import argparse
from client import create_client

default_group_params = {
    'location': 'westus'
}

def parse_argument():
    parser = argparse.ArgumentParser(description='Resource group creation script.')
    parser.add_argument('quantity', type=int, help='The quanity of resource groups to be created.')

    args = parser.parse_args()
    return args.quantity


if __name__ == "__main__":
    # Pass argments
    quantity = parse_argument()

    # Initialize the client
    client = create_client()

    # Create
    for i in range(quantity):
        group_name = f'RG-{i}'
        print(f'Creating resource group {group_name}...', end='')
        group = client.resource_groups.create_or_update(group_name, default_group_params)
        print(f'Done [{group.id}]')