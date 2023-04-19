from grafanalib.core import *
rows = []
panels = []

with open('metrics.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # Create a Graph object using the line as a title or other property
        panel = TimeSeries(
            title=line,
         #   dataSource='prometheus',
            targets=[
                Target(
       #             datasource='prometheus',
                    expr=line,
                ),
            ],
            unit=OPS_FORMAT,
            gridPos=GridPos(h=8, w=16, x=0, y=10),
        )  # Remove the comma here
        panels.append(panel)

dashboard = Dashboard(
    title="Python generated example dashboard",
    description="Example dashboard using the Random Walk and default Prometheus datasource",
    tags=[
        'example'
    ],
    timezone="browser",
    panels=[*panels],
).auto_panel_ids()

