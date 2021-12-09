from collections import namedtuple

Environment = namedtuple("Environment", ["name", "host", "client_id", "client_secret"])

PROD = Environment("prod",
                   "https://aip-workspace-naurouosyq-ew.a.run.app",
                   "681596136001-74tk1j4ctaejjuh81q1jbr3bl6elf76r.apps.googleusercontent.com",
                   "gs://aliz-aip-dev-client-configs/aliz-aip-prod/desktop_client_secret.json")
DEV = Environment("dev",
                  "https://aip-workspace-izulxl7bea-ew.a.run.app",
                  "292485802342-p290dncl40lh9sgs85d16nl06uh5f5cp.apps.googleusercontent.com",
                  "gs://aliz-aip-dev-client-configs/aliz-aip-dev/desktop_client_secret.json")
LOCAL = Environment("local",
                    "http://localhost:8080",
                    "292485802342-p290dncl40lh9sgs85d16nl06uh5f5cp.apps.googleusercontent.com",
                    "gs://aliz-aip-dev-client-configs/aliz-aip-dev/desktop_client_secret.json")
ENVIRONMENTS = {
    "prod": PROD,
    "dev": DEV,
    "local": LOCAL,
}
