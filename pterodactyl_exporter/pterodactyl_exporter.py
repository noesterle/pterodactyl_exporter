import argparse
import http.client
import time
import sys

from pterodactyl_exporter import config_load, http_client, http_server


def parse_args():
    parser = argparse.ArgumentParser(description="environment file")
    parser.add_argument("--config-file", default="config.yml")
    cfg_file = parser.parse_args().config_file
    if cfg_file is None:
        print("No config provided!")
        exit(1)
    return cfg_file


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    config_file = parse_args()
    config = config_load.get_config(config_file)
    mod_server = get_modified_server(config['host'])
    http_client.client_init(config, mod_server)
    http_server.init_metrics(mod_server)

    while True:
        try:
            http_client.get_server(config["server_list_type"])
            metrics = http_client.get_metrics()
            http_server.serve_metrics(metrics, mod_server)
            time.sleep(10)
        except http.client.RemoteDisconnected:
            print("API not responding!")
            time.sleep(10)
            continue


def get_modified_server(host):
    modified_server = None
    if host == 'mc.bloom.host':
        from modified_sources.bloom import Bloom as modified_server
        modified_server = modified_server()
    
    return modified_server


if __name__ == '__main__':
    main()
