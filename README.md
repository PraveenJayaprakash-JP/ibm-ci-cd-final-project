# IBM CI/CD Final Project

A minimal Python Flask application with CI/CD pipeline implementation for IBM DevOps course.

## Project Structure

```
ibm-ci-cd-final-project/
├── service/
│   └── app.py              # Flask application with API endpoints
├── tests/
│   └── test_app.py         # Unit tests for the Flask application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .github/workflows/     # GitHub Actions CI/CD workflows
└── .tekton/              # Tekton pipeline configuration
```

## Application Overview

This is a minimal Flask web application that provides:

- **Health Check Endpoint** (`/`): Returns 'SERVICERUNNING' to indicate the service is active
- **Detailed Health Endpoint** (`/health`): Returns JSON with detailed service status

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PraveenJayaprakash-JP/ibm-ci-cd-final-project.git
   cd ibm-ci-cd-final-project
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. **Start the Flask application:**
   ```bash
   cd service
   python app.py
   ```

2. **The application will be available at:**
   - Main endpoint: http://localhost:5000/
   - Health endpoint: http://localhost:5000/health

### API Endpoints

#### GET /

Returns a simple string indicating the service is running.

**Response:**
```
SERVICERUNNING
```

#### GET /health

Returns detailed service health information in JSON format.

**Response:**
```json
{
  "status": "healthy",
  "service": "running"
}
```

## Testing

### Running Unit Tests

Run the test suite to verify application functionality:

```bash
# From project root directory
python -m pytest tests/

# Or run with unittest
cd tests
python test_app.py
```

### Test Coverage

The test suite covers:
- Health check endpoint functionality
- JSON health endpoint response
- 404 error handling for non-existent endpoints

## CI/CD Pipeline

This project includes CI/CD pipeline configurations for:

- **GitHub Actions** (`.github/workflows/`): Automated testing and deployment
- **Tekton** (`.tekton/`): Kubernetes-native CI/CD pipeline tasks

## Dependencies

See `requirements.txt` for the complete list of dependencies:

- Flask==2.3.3
- Werkzeug==2.3.7

## Development

### Project Guidelines

1. All code changes should include appropriate unit tests
2. Follow PEP 8 style guidelines for Python code
3. Update documentation when adding new features
4. Ensure all tests pass before committing changes

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Submit a pull request

## License

This project is part of the IBM DevOps course curriculum.

---

*Last updated: August 2025*
