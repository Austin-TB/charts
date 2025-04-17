from typing import Any, Dict
from quickchart import QuickChart
from mcp.server.fastmcp import FastMCP

mcp = FastMCP()
CHART_BASE = "https://quickchart.io/chart"

@mcp.resource("config://app")
def get_config() -> str:
    """config format expected by get_chart tool"""
    return """
            config: The payload to send to quickchart.io. type - dict[str, any] for simple graphs. str for complex graphs.
            example for simple graph:
                config = {
                    "type": "bar",
                    "data": {
                        "labels": ["Hello world", "Test"],
                        "datasets": [{
                            "label": "Foo",
                            "data": [1, 2]
                        }]
                    }
                }
            example for complex graph:
                        config = {
                                    "type": "bar",
                                    "data": {
                                        "labels": ["A", "B"],
                                        "datasets": [{
                                            "label": "Foo",
                                            "data": [1, 2]
                                        }]
                                    },
                                    "options": {
                                        "scales": {
                                            "yAxes": [{
                                                "ticks": {
                                                    "callback": QuickChartFunction('(val) => val + "k"')
                                                }
                                            }],
                                            "xAxes": [{
                                                "ticks": {
                                                    "callback": QuickChartFunction('''function(val) {
                                                    return val + '???';
                                                    }''')
                                                }
                                            }]
                                        }
                                    }
                                }
            """


@mcp.tool()
def get_chart(config: Dict[str, Any] | str) -> str:
    """
        Generate url for a chart using quickchart.io
        
        args:
            config: The configuration for quickchart.io.
        
        returns:
            url: The url of the chart.
    """
    qc = QuickChart()
    qc.config = config
    return qc.get_short_url()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')