## Architecture Overview
- *Frontend*: React app connects to backend API.
- *Backend*: Flask handles requests, runs ML model.
- *ML*: Scikit-learn model predicts anomalies from log features.
- *DevOps*: Docker containers deployed via K8s, fixed with Ansible.
- Flow: Upload log -> Extract features -> Predict -> Display -> Trigger fix.
