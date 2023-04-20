[![Lint+Test](https://github.com/gfarcas/dashboard-kickstart/actions/workflows/python-app.yml/badge.svg)](https://github.com/gfarcas/dashboard-kickstart/actions/workflows/python-app.yml)
# Dashboard Kickstart 

This is a Python script to fetch and filter Prometheus/Thanos metrics and generate a dashboard file (`frontend.json`) using the filtered metrics.

NOTE: the script creates the panels with the default datasource set in grafana. If you want them created with a different datasource you can edit the `dashgen.dashboard.py` file and add a `datasource="Prometheus"` key to the Targets list. More details on grafanalib https://grafanalib.readthedocs.io/en/stable/getting-started.html#generating-dashboards
## Requirements

- Python 3.6 or higher
- `requests` library
- `argparse` library
- `grafanalib` library

Install the required libraries using the following command:

`pip install -r requirements.txt`

## Usage

1. Make sure you have Python 3.6 or higher installed.
2. Install the required libraries (if you haven't already).
3. Run the script using the command below, replacing `PROMETHEUS_URL` and `FILTER` with appropriate values.

`python metrics.py PROMETHEUS_URL FILTER`

- `PROMETHEUS_URL`: The URL of your Prometheus/Thanos server (e.g., `prometheus.example.com`).
- `FILTER`: The filter you want to apply to the fetched metrics (e.g., `http`).

Example:

`python metrics.py prometheus.example.com http`

This command will fetch metrics from the specified Prometheus/Thanos server, filter them based on the lines that start with the provided filter, and save the filtered metrics in a `metrics.txt` file.

4. The script will also generate a dashboard file named `frontend.json` by running `dashgen.dashboard.py` using the filtered metrics.

## Output

- `metrics.txt`: A file containing the filtered metrics, one per line.
- `frontend.json`: A dashboard file generated using the filtered metrics.

## Notes

- The script disables SSL/TLS verification when making requests to the Prometheus/Thanos server. This is not recommended for production environments. To enable SSL/TLS verification, remove the `verify=False` argument in the `requests.get()` function call.
