# Shuffler API Integration 🚀

## 📌 Overview
This project integrates with the **Shuffler API**, providing various functionalities like:
- Fetching apps and workflows.
- Managing workflow executions.
- Secure API authentication with SSL.

## 💒 Folder Structure
```
shuffler/
│── src/
│   │── api.py         # API integration
│   │── auth.py        # Authentication logic
│   │── config.py      # Configuration settings
│   │── utils.py       # Utility functions
│── tests/             # Unit tests
│── main.py            # Run the API
│── requirements.txt   # Dependencies
│── README.md          # Documentation
```

## 🔧 Installation
```bash
git clone https://github.com/serdarzuli/shuffler-api.git
cd shuffler-api
pip install -r requirements.txt
```

## 🚀 Usage
```bash
python run.py
```

## 🧪 Running Tests
```bash
pytest tests/
```

## 🐟 API Endpoints
| Method | Endpoint | Description |
|--------|------------|-------------|
| `GET`  | `/apps` | Fetch all apps |
| `GET`  | `/workflows` | Get list of workflows |
| `GET`  | `/workflows/{workflow_id}/executions` | Get workflow executions |
| `POST` | `/workflows` | Create a new workflow |
| `POST` | `/workflows/{workflow_id}/execute` | Execute a workflow |

## 🌐 License
This project is licensed under the **MIT License**.

