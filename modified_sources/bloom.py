from prometheus_client import Gauge
from dataclasses import make_dataclass
from pterodactyl_exporter.dto.metrics import Metrics

class Bloom:

    def __init__(self):
        pass


    def add_metrics(self, metrics):
        metrics.__class__ = make_dataclass('BloomMetrics', fields=[('online_players', int, 0)], bases=(Metrics,))


    def add_gauge(self, metrics_gauge, label_names):
        metrics_gauge["online_players"] = Gauge("pterodactyl_server_online_players", "Number of players online for the server", label_names)


    def serve_metrics(self, metric_gauges, metric_name, srv_label, id_label, value, server_index):
        if metric_name == 'online_players':
            print("METRIC NAME", metric_name)
            metric_gauges[metric_name].labels(srv_label, id_label).set(value[server_index])
            print("Served Server Metrics for Mod Server")


    def get_metrics(self,srv,metrics):
        if "online_players" in metrics:
            srv["online_players"].append(metrics["online_players"])
        else:
            srv["online_players"].append(-1.0)
