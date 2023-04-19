import requests
import argparse
import os

# create an ArgumentParser object
parser = argparse.ArgumentParser()

# add multiple positional arguments
parser.add_argument("url", help="prometheus/thanos url prometheus.example.com")
parser.add_argument("filter", help="filter for metrics")

# parse the arguments
args = parser.parse_args()

def get_prometheus_metrics(prometheus_url):
    response = requests.get(
        f'{prometheus_url}/api/v1/label/__name__/values', verify=False)
    response.raise_for_status()  # Raise an exception if the request failed
# return one metric per line without quotes

    with open('metrics.txt', 'w') as file:
        for line in response.text.split(','):
            line = line.replace('"', '')
            if line.startswith(args.filter):
                print(line)
                file.write(line + '\n')


# Replace with your Prometheus server URL
prometheus_url = 'https://'+args.url+'/'
metrics = get_prometheus_metrics(prometheus_url)

# Print the list of available metrics
os.system("generate-dashboard -o frontend.json dashgen.dashboard.py")
