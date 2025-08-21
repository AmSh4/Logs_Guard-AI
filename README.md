# Logs_Guard-AI
It is a unique, AI-driven DevOps tool designed for Linux environments. It uses machine learning to analyze server logs for anomaly detection, predicting potential failures before they occur. This predictive maintenance approach is rare in open-source tools, combining DevOps practices with AI to optimize Linux cluster management.

## Project Structure

    Logs_Guard-AI/
    ├── README.md
    ├── backend/
    │   ├── app.py
    │   ├── requirements.txt
    │   ├── ml_model.py
    │   ├── anomaly_detector.py
    │   ├── utils.py
    │   └── data_processor.py
    ├── frontend/
    │   ├── package.json
    │   ├── src/
    │   │   ├── App.js
    │   │   ├── index.js
    │   │   ├── components/
    │   │   │   ├── Dashboard.js
    │   │   │   ├── LogUploader.js
    │   │   │   └── PredictionResults.js
    │   │   └── styles/
    │   │       └── dashboard.css
    │   └── public/
    │       └── index.html
    ├── datasets/
    │   ├── sample_logs/
    │   │   ├── normal_log.txt
    │   │   ├── anomaly_log_1.txt
    │   │   ├── anomaly_log_2.txt
    │   │   └── training_data.csv
    ├── scripts/
    │   ├── ansible/
    │   │   ├── playbook_fix_server.yml
    │   │   └── inventory.ini
    │   ├── docker/
    │   │   ├── Dockerfile.backend
    │   │   └── Dockerfile.frontend
    │   └── k8s/
    │       ├── deployment-backend.yaml
    │       └── deployment-frontend.yaml
    ├── .github/
    │   └── workflows/
    │       └── ci-cd.yml
    ├── docs/
    │   ├── architecture.md
    │   └── user_guide.md
    └── LICENSE

## The tool features:
- **Frontend**: A modern React-based dashboard for uploading logs, viewing predictions, and triggering automated fixes.
- **Backend**: Python Flask API integrated with scikit-learn for ML-based anomaly detection.
- **AI Component**: A custom ML model trained on Linux syslog datasets to detect anomalies like high CPU spikes or disk errors.
- **DevOps Integration**: Ansible playbooks for automated remediation, Docker for containerization, and Kubernetes manifests for orchestration. CI/CD pipeline via GitHub Actions.
- **Datasets**: Sample Linux log files and a CSV for model training.


## Why This?
- Focuses on predictive analytics for Linux-specific issues (e.g., kernel panics, SELinux errors), which is underrepresented in tools like Prometheus or ELK stack.
- Integrates AI not just for monitoring but for proactive IaC (Infrastructure as Code) suggestions via Ansible.
- **Rare combination**: ML-driven failure prediction with automated deployment fixes in a single repo.

## Tech Stack
- **Frontend**: React.js with CSS for an attractive, responsive UI.
- **Backend**: Python 3.10+, Flask, scikit-learn.
- **ML**: Random Forest classifier for anomaly detection.
- **DevOps**: Ansible, Docker, Kubernetes, GitHub Actions.
- **Data**: Custom Linux log datasets.

## Setup and Installation
### Prerequisites
- Linux OS (tested on Ubuntu 22.04).
- Python 3.10+.
- Node.js 18+.
- Docker and Docker Compose.
- Minikube or Kubernetes cluster for full deployment.
- Ansible installed.

### Quick Start
1. Clone the repo:

       git clone
       https://github.com/yourusername/Logs_Guard-AI.git
       cd AI-DevOps-Predicton
2. Backend Setup:
   
       cd backend python -m venv venv
       source venv/bin/activate
       pip install -r requirements.txt
       python app.py
    Backend runs on `http://localhost:5000`.

3. Frontend Setup:

       cd ../frontend npm
       install npm start
   Frontend runs on `http://localhost:3000`.

4. Train ML Model:

       cd ../backend
       python ml_model.py
   
5. Docker Build:

       cd ../scripts/docker
       docker build -t backend-image -f Dockerfile.backend ../../backend
       docker build -t frontend-image -f Dockerfile.frontend ../../frontend

6. Run Docker Containers:

       docker run -d -p 5000:5000 --name aiops-backend aiops-backend:latest
       docker run -d -p 3000:3000 --name aiops-frontend aiops-frontend:latest
   
7. Kubernetes Deployment:
   
       kubectl apply -f ../../scripts/k8s/deployment-backend.yaml
       kubectl apply -f ../../scripts/k8s/deployment-frontend.yaml
9. Ansible Remediation (To automate server fixes):
        ansible-playbook -i scripts/ansible/inventory.ini scripts/ansible/playbook_fix_server.yml

## Usage
- Upload Linux logs via the dashboard.
- View AI predictions on potential failures.
- Trigger Ansible fixes automatically.

## Datasets
- `datasets/sample_logs/`: Contains normal and anomalous Linux syslogs.
- `training_data.csv`: Labeled data for ML training (features: CPU usage, error counts, etc.).

## Architecture
See `docs/architecture.md` for detailed diagrams (text-based).

## Contributing
Fork and PR! Ensure code is error-free and tested on Linux.

## License
MIT License. See `LICENSE`.
