# Stage 0 Backend - Develop a Public API to Retrieve Basic Information

**Task**:
A simple Flask API that returns personal information in JSON format. It is part of the HNG Internship 12, Stage 0 task.

## Description

This API provides a single endpoint that returns:

- Email address
- Current date and time in ISO 8601 format
- GitHub repository URL

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/tonybnya/hng12.git
cd hng12/backend/stage_0
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip3 install -r requirements.txt
```

4. Run the application:

```bash
python3 main.py
```

## API Documentation

**Endpoint**:

- URL: `http://localhost:5000/`
- Method: `GET`
- CORS: Enabled for all origins

**Response Format**:

```json
{
    "email": "tonybnya@gmail.com",
    "current_datetime": "2023-09-08T15:30:45Z",
    "github_url": "https://github.com/tonybnya/hng12/backend/stage_0"
}
```

**Example Usage**:

Using `curl`:

```bash
curl http://localhost:5000/
```

Using JavaScript `fetch`:

```javascript
fetch('http://localhost:5003/')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Technologies Used

- Python3
- Flask
- Flask-CORS
