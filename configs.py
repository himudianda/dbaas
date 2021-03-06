RABBITMQ_USERNAME = "rabbitmq"
RABBITMQ_PASSWORD = "rabbitmq"
RABBITMQ_SERVER = "rtp10-1-csl-troverabbitmq-001"#"rtp10-svc-4-medium01-troverabbitmq-001"#"10.207.227.135"
RABBITMQ_PORT = 5672

RABBITMQ_EXCHANGE = "trove"
RABBITMQ_TYPE = "topic"

RABBITMQ_DEFAULT_BINDING_KEY = "notifications.*"


SAMPLE_DATA_INPUT_FILE = "trove.events"
JSON_LOG_OUTPUT_FILE = "/tmp/dbaas_logs.json"
NAGIOS_LOG_OUTPUT_FILE = "/tmp/dbaas_alerts.logs"
