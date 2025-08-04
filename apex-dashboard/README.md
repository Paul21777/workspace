

# ApexCharts Dashboard with Monster UI and FastHTML

This project demonstrates how to create a dashboard using ApexCharts with Monster UI and FastHTML.

## Features

- Line charts, pie charts, and bar charts using ApexCharts
- Styling with Monster UI components
- FastHTML for server-rendered web application
- Dockerized for easy deployment

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/apex-dashboard.git
   cd apex-dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application locally:
```bash
python main.py
```

The application will be available at `http://localhost:5001`.

## Docker

To build and run the application using Docker:

1. Build the Docker image:
   ```bash
   docker build -t apex-dashboard .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5001:5001 apex-dashboard
   ```

The application will be available at `http://localhost:5001`.

## Project Structure

```
apex-dashboard/
├── main.py                # Main application file
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── static/                # Static files
    └── (empty)
└── templates/             # Template files
    └── (empty)
```

## License

This project is open source and available under the MIT License.

