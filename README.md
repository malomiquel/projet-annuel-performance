
# Project Performance Testing Documentation

## Overview

This project contains performance testing scripts using Locust for a healthcare prediction API. The codebase consists of two files: a minimal README.md and a Locust test script (locustfile.py).

## Contents

1. README.md
   - A placeholder markdown file with the project title "projet-annuel-performance"

2. locustfile.py
   - The main Locust test script for performance testing the API

## Locust Test Script (locustfile.py)

### Description

The Locust test script defines a user behavior class `ApiUser` that simulates API interactions for performance testing. It includes two main tasks: checking the health of the API and making predictions.

### Tasks

1. **Health Check**
   - Sends a GET request to the health check endpoint
   - URL: `http://ec2-35-180-228-111.eu-west-3.compute.amazonaws.com:5000/health_check`

2. **Predict**
   - Sends a POST request to the prediction endpoint
   - URL: `http://ec2-35-180-228-111.eu-west-3.compute.amazonaws.com:5000/predict/patient`
   - Includes sample patient data in JSON format

### Input

The prediction task sends the following sample patient data:

```json
{
    "PRG": 100,
    "PL": 150,
    "PR": 120,
    "SK": 130,
    "TS": 140,
    "M11": 16,
    "BD2": 170,
    "Age": 30,
    "Insurance": 200
}
```

### Output

The script does not explicitly handle or process the API responses. The primary purpose is to generate load on the API endpoints for performance testing.

## Usage

To use this Locust script:

1. Ensure Locust is installed in your Python environment
2. Run the Locust command, pointing to this script
3. Access the Locust web interface to configure and start the load test
4. Monitor the performance metrics provided by Locust

## Notes

- The API appears to be hosted on an AWS EC2 instance
- The script is designed for testing a healthcare prediction API, likely for patient data analysis
- Modify the sample data in the `predict` task to test different scenarios or edge cases
- Adjust the relative frequency of tasks by adding weight parameters if needed
