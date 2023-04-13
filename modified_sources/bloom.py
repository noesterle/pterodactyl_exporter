from prometheus_client import Gauge

class Bloom:

    def __init__(self):
        self.online_players = None

    def add_srv_keys(self, srv):
        srv['online_players'] = []

    def add_gauge(self, label_names):
        self.online_players = Gauge("pterodactyl_server_online_players", "Number of players online for the server", label_names)

    def serve_metrics(self, srv_label, id_label, metrics, server_index):
        self.online_players.labels(srv_label, id_label).set(metrics["online_players"][server_index])

    def get_metrics(self,srv,metrics):
        if "online_players" in metrics:
            srv["online_players"].append(metrics["online_players"])
        else:
            srv["online_players"].append(-1.0)
