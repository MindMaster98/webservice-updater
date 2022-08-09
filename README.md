# docker-service-updater
This GitHub Action provides a simple interface for the [Microservice Updater](https://github.com/MindMaster98/microservice-updater), a webservice for 
automated docker container updates and deployments.

## Parameters
The GitHub Actions offers the following parameters for customization:

* `mode` (default: `update`): The used mode of the Microservice Updater
  * valid values: `register`, `update` or `delete`
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
  ],
  "ids": {
    "0": "ID provided by the Microservice Updater after registration"
  }, ...
}
```

## Example
This example provides a GitHub Action and the according configuration file to autodeploy an instance of the [Microservice Updater](https://github.com/MindMaster98/microservice-updater). The Action requires the project secrets `UPDATER_HOST` and `API_KEY` to work properly.

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
      uses: MindMaster98/docker-service-updater@v0.1.4
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
      "image": "bigoli98/microservice-updater",
      "tag": "latest"
    }
  ],
  "ids": {
    "0": "bigoli98-microservice-updater"
  }
}
```
