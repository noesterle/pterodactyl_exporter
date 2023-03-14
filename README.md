# Pterodactyl Exporter

This is an extendable Pterodactyl metrics exporter for Prometheus forked from [LEONS2's pterodactyl_exporter](https://github.com/LOENS2/pterodactyl_exporter).
This is designed to not only support Pterdactyl API but also support modified versions of the Pterodactyl API.
The implementation of the Pterdactyl API used by the application is determined by the value of `host` in `config.yml`.

### Supported Pterodactyl API Implementations
- [Pterdactyl](https://pterodactyl.io/)
- [Bloom](https://bloom.host/)

### Please use the Discussion for Support rather than the Issues.

A python script that exports performance metrics from Pterodactyl Panel 1.x via the Client API, converts the data to the correct format and provides a prometheus target.

This can be used for time series monitoring of Pterodactyl game servers and visualization with Grafana.

Feel free to try this script and submit an issue if needed.

# How to build and use Docker Image

### What you need:

 * Bash
 * Docker
 * Docker Compose (optional)

There are scripts in `docker/` to assist with building, running, and deploying a docker image.
This all requires docker to be installed, which can be verified by running `docker --version` and seeing a valid version and build number, such as `Docker version 20.10.21, build 20.10.21-0ubuntu1~22.04.2`.
Once Docker is installed correctly, verify it can run images as containers by following the [Whalesay](https://hub.docker.com/r/docker/whalesay/) tutorial.

### Build

To build a docker image, be in the `pterodactyl_exporter` folder and run `bash docker/docker-build.sh`.
Verify a new image is build by running `docker images`.
For other scripts, note the `IMAGE ID`.

### Run

To run the image in a container, run `bash docker/docker-run.sh <IMAGE ID>`.
Verify the container is running by using the command `docker ps`, a new container should appear with the entered `IMAGE ID`.

To view the statistics gathered by the containerized application, open your web browser and go to `0.0.0.0:9531`.
Statistics should appear and update periodically.

### Push

To push the image, run `bash docker/docker-push.sh -i <IMAGE ID> [-l] [-n VERSION NUMBER] [-h] [-v]`.
Add the `-h` flag to print help output.

Once an image is pushed, `docker/docker-compose.yml` can be used to pull and run the image in a container.
The statistics can be viewed the same way as running a locally built image.

# How to install

#### What you need:

 * Linux server (should run on Windows as well, but is only tested in a linux environment)
 * Prometheus
 * Python (3.10)
 * Pterodactyl client API key (service account with read only is recommended)

## Run as service

#### Installed as user "prometheus":

 - To install with pip:
```
pip install pterodactyl-exporter
```
 - Create directory `pterodactyl_exporter`.
 
 - Create the config file `config.yml` in that directory (set the values as needed, it's recommended to use https):
 
 ```yml
host: panel.example.com
api_key: APIKEY_APIKEYAPIKEYAPIKEY
https: true
ignore_ssl: false
server_list_type: owner
 ```

 - Create systemd service `/etc/systemd/system/pterodactyl_exporter.service`:
```
[Unit]
Description=Prometheus Server
After=network-online.target

[Service]
User=prometheus
Restart=on-failure
ExecStart=pterodactyl_exporter \
--config-file=/home/prometheus/pterodactyl_exporter/config.yml

[Install]
WantedBy=multi-user.target
```

 - Enable and start the service.
 
 - Add a job configuration:
 
 ```yml
 - job_name: 'pterodactyl_exporter'
    static_configs:
      - targets: ['localhost:9531']

 ```

 - To get the Grafana dashboard, import id `16575`. Alternatively download the JSON file from the releases.
 
 #### To show and hide servers from being monitored, just remove the read permission of the service account on that Server
 
## Run with Docker

 - Create a folder named `pterodactyl_exporter`
 
 - Download the config file from GitHub:
 ```
 curl -fsSL -o config.yml https://raw.githubusercontent.com/noesterle/pterodactyl_exporter/master/config.example.yml
 ```
 - Create a folder named `docker`
 
 - Download the `docker-compose.yml` into that folder:
 ```
 curl -fsSL -o docker-compose.yml https://raw.githubusercontent.com/noesterle/pterodactyl_exporter/master/docker/docker-compose.yml
 ```
 - Run the container:
 ```
 docker-compose up -d
 ```
 
## Run manually

#### Only meant for testing purposes, not recommended for production use!

 - Clone the project:
```
git clone https://github.com/noesterle/pterodactyl_exporter.git
```
 - Change to the cloned directory
 - Run with python:
```
python -m pterodactyl_exporter.pterodactyl_exporter --config-file=config.example.yml
```

# Troubleshooting

You can view the output with (Time is UTC):

```
sudo journalctl -u pterodactyl_exporter.service -b --since "2024-12-14 13:45:27"
```

Post any stacktraces as an Issue.

##

With special thanks to @grimsi for helping me with docker.

&copy; LOENS2 2022
