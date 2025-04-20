from typing import Any, Literal, Optional
from quickchart import QuickChart

from fastmcp import FastMCP

mcp = FastMCP(
    "QuickChart Server",
    instructions="Provides a tool to generate chart image URLs using QuickChart.io based on Chart.js configuration. Also provides schema information via a resource.",
    # Add dependencies required if deploying via `fastmcp install`
    dependencies=["quickchart.io>=2.0.0"],
)

@mcp.tool()
def create_chart_url(
    config: dict[str, Any],
    width: Optional[int] = None,
    height: Optional[int] = None,
    format: Optional[Literal["png", "svg"]] = "png",
    background_color: Optional[str] = None,
    device_pixel_ratio: Optional[float] = None,
    version: Optional[str] = None,
) -> str:
    """
    Generates a QuickChart URL based on a Chart.js configuration object.

    Args:
        config (dict): The Chart.js configuration object. Key fields include:
            - 'type': (string) The chart type (e.g., 'bar', 'line', 'pie').
            - 'data': (object) Contains chart data:
                - 'labels': (list[string]) Labels for the x-axis or segments.
                - 'datasets': (list[object]) Data series. Each needs:
                    - 'label': (string) Dataset name.
                    - 'data': (list[number]) Data points.
            - 'options': (object, optional) Chart customization options.
        width (Optional[int]): Width in pixels (default: 500).
        height (Optional[int]): Height in pixels (default: 300).
        format (Optional[Literal['png', 'svg']]): Image format (default: 'png').
        background_color (Optional[str]): Background color (default: '#ffffff').
        device_pixel_ratio (Optional[float]): Device pixel ratio (default: 1.0).
        version (Optional[str]): Chart.js version (e.g., '3').

    Example minimal 'config' for a bar chart:
    {
      "type": "bar",
      "data": {
        "labels": ["Jan", "Feb", "Mar"],
        "datasets": [{"label": "Sales", "data": [10, 25, 18]}]
      }
    }

    For more detailed structure examples and common options, read the resource at 'resource://chartjs-schema-info'.
    """
    qc = QuickChart()

    # setting mandatory config
    if not isinstance(config, dict):
        return "Error: 'config' parameter must be a valid dictionary (JSON object)."
    qc.config = config

    if width is not None:
        qc.width = width
    if height is not None:
        qc.height = height
    if format is not None:
        qc.format = format
    if background_color is not None:
        qc.background_color = background_color
    if device_pixel_ratio is not None:
        qc.device_pixel_ratio = device_pixel_ratio
    if version is not None:
        qc.version = version

    try:
        url = qc.get_short_url()
        return url
    except Exception as e:
        return f"Error generating QuickChart URL: {e}"


@mcp.resource(
    uri="resource://chartjs-schema-info",
    name="ChartJsSchemaInfo",
    description="Provides examples and key schema details for Chart.js configurations used by QuickChart.",
    mime_type="text/plain",
)
def get_chartjs_schema_info() -> str:
    """Returns helpful schema information and examples for Chart.js config."""
    info = 
    """
        Chart.js Configuration Structure for QuickChart:

        The main keys are 'type', 'data', and optionally 'options'.

        1.  **`type`**: string (Required)
            *   Common values: "bar", "line", "pie", "doughnut", "radar", "polarArea", "scatter", "bubble"

        2.  **`data`**: object (Required)
            *   `labels`: list[string] - Needed for axes/segments in most chart types.
                *   Example: `["Jan", "Feb", "Mar"]`
            *   `datasets`: list[object] - Each object is a data series.
                *   `label`: string (Required) - Name for the legend/tooltip.
                *   `data`: list[number | object] (Required) - The data points.
                    *   For bar/line/pie etc.: `[10, 20, 30]`
                    *   For scatter/bubble: `[{'x': 10, 'y': 20}, {'x': 15, 'y': 25}]` or `[{'x': 1, 'y': 1, 'r': 5}]` (bubble radius)
                *   `backgroundColor`: string | list[string] (Optional) - Fill color(s). Example: `"rgba(255, 99, 132, 0.2)"` or `["red", "blue", "green"]`.
                *   `borderColor`: string | list[string] (Optional) - Border color(s). Example: `"rgb(255, 99, 132)"`.
                *   `fill`: boolean | string (Optional, for line/radar) - e.g., `false` or `'origin'`.
                *   `tension`: number (Optional, for line) - Curve tension (0 for straight lines). Example: `0.1`.

        3.  **`options`**: object (Optional) - For customization.
            *   `title`: object - Example: `{ "display": true, "text": "My Chart Title" }`
            *   `legend`: object - Example: `{ "display": true, "position": "top" }` (positions: 'top', 'left', 'bottom', 'right')
            *   `scales`: object (For charts with axes like bar, line, scatter)
                *   `xAxes`: list[object] - Configuration for X axis/axes.
                *   `yAxes`: list[object] - Configuration for Y axis/axes.
                    *   Each axis object: `{ "ticks": { "beginAtZero": true }, "scaleLabel": { "display": true, "labelString": "Value" } }`
            *   `plugins`: object - For Chart.js plugins.
                *   `datalabels`: object - Example: `{ "display": true, "color": "white" }` (requires QuickChart support for the plugin)

        Example (Line Chart):
            {
            "type": "line",
            "data": {
                "labels": ["Mon", "Tue", "Wed", "Thu", "Fri"],
                "datasets": [{
                "label": "Website Views",
                "data": [120, 150, 110, 180, 160],
                "fill": false,
                "borderColor": "rgb(75, 192, 192)",
                "tension": 0.1
                }]
            },
            "options": {
                "title": { "display": true, "text": "Website Views Per Day" },
                "scales": { "yAxes": [{ "ticks": { "beginAtZero": true } }] }
                }
            }

        Example (Pie Chart):
        {
        "type": "pie",
        "data": {
            "labels": ["Red", "Blue", "Yellow"],
            "datasets": [{
            "label": "Colors",
            "data": [300, 50, 100],
            "backgroundColor": ["rgb(255, 99, 132)", "rgb(54, 162, 235)", "rgb(255, 205, 86)"]
            }]
        },
        "options": {
            "title": { "display": true, "text": "Color Distribution" }
            }
        }
    """
    return info

if __name__ == "__main__":
    mcp.run(transport='stdio')