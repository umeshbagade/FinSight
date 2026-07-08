# FinSight

**Turns banking data into proactive business insights.**

FinSight is an AI-powered business advisor designed to help small and medium-sized enterprises (SMEs) better understand their financial health.

The platform aims to provide proactive insights such as:

- Cash flow forecasting
- Invoice payment risk detection
- Unusual expense detection
- Financial health insights
- Financing recommendations
- AI-powered business advisory

## Prerequisites

Before running the project, make sure the following are installed:

- Git
- Python 3.9 or later
- Node.js
- npm

Verify the installations:

```bash
git --version
python3 --version
node --version
npm --version
```

## Clone the Repository

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd FinSight
```

The project structure is:

```text
FinSight/
├── .github/
│   └── workflows/
│       └── backend-build.yml
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── tests/
│   ├── app.py
│   ├── pytest.ini
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

## Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install the backend dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the backend application:

```bash
python app.py
```

The Flask backend will run on:

```text
http://localhost:5000
```

Test the health endpoint:

```text
http://localhost:5000/api/health
```

Test the cash flow forecast endpoint:

```text
http://localhost:5000/api/cashflow/forecast
```

## Run Backend Tests

Make sure the virtual environment is activated.

From the `backend` directory, run:

```bash
python -m pytest
```

## Stop the Backend

Stop the Flask server using:

```text
Ctrl + C
```

Deactivate the Python virtual environment:

```bash
deactivate
```

## Frontend Setup

Open another terminal and navigate to the frontend directory:

```bash
cd FinSight/frontend
```

Install the frontend dependencies:

```bash
npm install
```

Run the frontend development server:

```bash
npm run dev
```

The frontend will usually run on:

```text
http://localhost:5173
```

Open the address shown by Vite in your browser.

## Running the Full Application

The backend and frontend must run simultaneously.

Terminal 1:

```bash
cd FinSight/backend

source .venv/bin/activate

python app.py
```

Terminal 2:

```bash
cd FinSight/frontend

npm install

npm run dev
```

The application architecture is:

```text
Browser
   │
   ▼
React + Vite
localhost:5173
   │
   │ /api/*
   ▼
Vite Development Proxy
   │
   ▼
Flask Backend
localhost:5000
```

## Frontend Commands

Run the development server:

```bash
npm run dev
```

Run ESLint:

```bash
npm run lint
```

Create a production build:

```bash
npm run build
```

## Git Workflow

Create a development branch or feature branch before making changes:

```bash
git checkout -b feature/<feature-name>
```

After making changes:

```bash
git add .

git commit -m "Describe your changes"

git push origin feature/<feature-name>
```

Create a Pull Request to merge your changes into the appropriate target branch.

Do not commit:

- Python virtual environments (`.venv`)
- `node_modules`
- `.env` files
- API keys or credentials
- Build outputs (`dist`)

## CI/CD

GitHub Actions is used to run automated backend tests for Pull Requests targeting the `main` branch.

The backend CI workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs backend dependencies.
4. Runs the test suite using `pytest`.
5. Reports the build status on the Pull Request.

## License

This project is currently intended for hackathon and demonstration purposes.