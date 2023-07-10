import requests
import json
from os import environ
import sys


def generate_id(config: dict):
    if config['mode'] == 'dockerfile':
        return config['image'].replace('/', '-')
    else:
        return '-'.join(config['url'].lower().replace('//', '').split('/')[1:]).replace('.git', '')


# load service configuration
with open(environ['CONFIG_FILE']) as f:
    initialization_configuration = json.load(f)

# load microservice updater configuration
host = environ['UPDATER_HOST']
api_key = environ['API_KEY']

# for each service configuration
for i, service in enumerate(initialization_configuration['services']):
    service['API-KEY'] = api_key
    service_id = generate_id(service)

    # read all related files and add them to the payload
    if 'files' in service:
        for file in service['files']:
            with open(f'{environ["SETUP_PATH"]}/{service["files"][file]}') as f:
                service['files'][file] = f.read()

    check = requests.get(f'{host}/service/{service_id}', verify=False)

    # register new service
    if not check.ok:
        response = requests.post(f'{host}/service', json=service, headers={'Content-Type': 'application/json'},
                                 verify=False)

        # registration successful
        if response.ok:
            print(f'service {i} registered successfully.', response.text)
        # registration failed
        else:
            print(f'registration of service {service_id} failed:', response.text)
            sys.exit(-1)
    else:
        # update service
        response = requests.post(f'{host}/service/{service_id}', json=service,
                                 headers={'Content-Type': 'application/json'}, verify=False)

        # update initiated successfully
        if response.ok:
            print(f'service {service_id} update initiated successfully.', response.text)
        # update initiation failed
        else:
            print(f'service {service_id} update failed.', response.text)
            sys.exit(-2)
