
from fasthtml.common import *
from monsterui.all import *
import json

# Initialize the FastHTML app with MonsterUI theme and ApexCharts support
app, rt = fast_app(hdrs=Theme.blue.headers(apex_charts=True))

# Sample data for the dashboard
sample_data = {
    "line_chart": {
        "series": [{"name": "Sales", "data": [10, 41, 35, 51, 49, 62, 69, 91, 148]},
                   {"name": "Expenses", "data": [10, 29, 37, 36, 44, 45, 50, 58, 61]}],
        "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
    },
    "pie_chart": {
        "series": [44, 55, 13, 43, 22],
        "labels": ["A", "B", "C", "D", "E"]
    },
    "bar_chart": {
        "series": [{
            "name": "Net Profit",
            "data": [44, 55, 57, 56, 61, 58, 63, 60, 66]
        }, {
            "name": "Revenue",
            "data": [76, 85, 101, 98, 87, 105, 91, 114, 94]
        }],
        "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
    }
}

# Dashboard route
@rt
def index():
    return Titled(
        "ApexCharts Dashboard",
        Div(
            H1("Sales Dashboard", cls="text-2xl font-bold mb-4"),
            Div(
                ApexChart(
                    opts={
                        "chart": {"type": "line", "zoom": {"enabled": False}, "toolbar": {"show": False}},
                        "series": sample_data["line_chart"]["series"],
                        "xaxis": {"categories": sample_data["line_chart"]["categories"]},
                        "title": {"text": "Sales & Expenses", "align": "left"}
                    },
                    cls="max-w-xl mx-auto mb-8"
                ),
                ApexChart(
                    opts={
                        "chart": {"type": "pie", "zoom": {"enabled": False}, "toolbar": {"show": False}},
                        "series": sample_data["pie_chart"]["series"],
                        "labels": sample_data["pie_chart"]["labels"],
                        "title": {"text": "Market Share", "align": "left"}
                    },
                    cls="max-w-md mx-auto mb-8"
                ),
                ApexChart(
                    opts={
                        "chart": {"type": "bar", "zoom": {"enabled": False}, "toolbar": {"show": False}},
                        "series": sample_data["bar_chart"]["series"],
                        "xaxis": {"categories": sample_data["bar_chart"]["categories"]},
                        "title": {"text": "Net Profit & Revenue", "align": "left"}
                    },
                    cls="max-w-xl mx-auto"
                ),
                cls="space-y-6"
            ),
            cls="container mx-auto p-4"
        )
    )

# Run the application
if __name__ == "__main__":
    serve()
