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
