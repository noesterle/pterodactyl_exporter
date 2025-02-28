from prometheus_client import Gauge
from dataclasses import field, dataclass
from pterodactyl_exporter.dto.metrics import Metrics
from typing import List

@dataclass
class BloomMetrics(Metrics):
    online_players: List[int] = field(default_factory=list)

class Bloom:

    def __init__(self):
        pass


    def add_metrics(self, metrics):
        metrics = BloomMetrics()
        return metrics


    def add_gauge(self, metrics_gauge, label_names):
        metrics_gauge["online_players"] = Gauge("pterodactyl_server_online_players", "Number of players online for the server", label_names)


    def serve_metrics(self, metric_gauges, metric_name, srv_label, id_label, value, server_index):
        if metric_name == 'online_players':
            metric_gauges[metric_name].labels(srv_label, id_label).set(value[server_index])


    def process_resources(self,metrics ,resources):
        if "online_players" in resources:
            metrics.online_players.append(resources["online_players"])
        else:
            metrics.online_players.append(-1)
