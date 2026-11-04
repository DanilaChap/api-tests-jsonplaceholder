# ApiTests for JSONPlaceholder
Automated tests for the REST API at https://jsonplaceholder.typicode.com

## What is covered
- GET
- POST
- PUT
- DELETE
- Positive and negative tests
- Parametrisation
- Fixture

## Tech stack
- Python
- pytest
- requests
- ruff

## How to run
1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the tests:

   ```bash
   python -m pytest -v
   ```
   