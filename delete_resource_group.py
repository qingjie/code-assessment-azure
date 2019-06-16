import argparse
from client import create_client
import sys

def parse_argument():
    parser = argparse.ArgumentParser(description='Resource group deletion script.')
    parser.add_argument('index', type=int, help='The index of resource group to be removed.')

    args = parser.parse_args()
    return args.index

if __name__ == "__main__":
    # Pass argments
    index = parse_argument()
    group_name = f'RG-{index}'

    # Initialize the client
    client = create_client()

    if not client.resource_groups.check_existence(group_name):
        print(f'Resource group {group_name} could not be found.')
        sys.exit(-1)
    
    # Remove
    print(f'Deleting resource group {group_name}...', end='')
    client.resource_groups.delete(group_name)
    print(f'Done')