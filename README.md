# docker-service-updater
This GitHub Action provides a simple interface for the [Microservice Updater](https://github.com/MindMaster98/microservice-updater), a webservice for 
automated docker container updates and deployments.

## Parameters
The GitHub Actions offers the following parameters for customization:

* `config_file` (default: `service_config/service_config.json`): relative path to the configuration file
* `setup_path` (default: `service_config/files`): relative to the path containing files used to copy into Docker containers
* `updater_host`: host of the Microservice Updater instance (e. g. `https://localhost:8443`)
* `api_key`: API-KEY of the Microservice Updater instance (e. g. `"1234"`)

## Configuration file
```json
{
  "services": [
    {
      valid payload for the Microservice Updater
    }, ...
  ]
}
```

## Example
This example provides a GitHub Action and the according configuration file to autodeploy an instance of the [Microservice Updater](https://github.com/WSE-research/microservice-updater). The Action requires the project secrets `UPDATER_HOST` and `API_KEY` to work properly.

### GitHub Action
```yaml
name: Docker Image CI

on:
  push:
    # use default branch
    branches: [ master ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    # Required to access configuration
    - uses: actions/checkout@v3
    
    # Initializing update process with default settings
    - name: Init update
      uses: WSE-research/docker-service-updater@v0.2.0
      with:
        updater_host: ${{ secrets.UPDATER_HOST }}
        api_key: ${{ secrets.API_KEY }}
```

### Configuration file at `service_config/service_config.json`
```json
{
  "services": [
    {
      "mode": "dockerfile",
      "port": "10001:9000",
      "image": "wseresearch/microservice-updater",
      "tag": "latest"
    }
  ]
}
```
