# k8s_release_validator_mock_service


```commandline
├─ app/
│  ├─ main.py
│  ├─ api/
│  │  ├─ __init__.py
│  │  └─ v1/
│  │     ├─ __init__.py
│  │     └─ routes_mock.py
│  ├─ core/
│  │  ├─ __init__.py
│  │  └─ config.py
│  ├─ services/
│  │  ├─ __init__.py
│  │  └─ mock_service.py
│  └─ schemas/
│     ├─ __init__.py
│     └─ responses.py
├─ deployment/
│  ├─ Dockerfile
│  ├─ docker-compose.yml
│  └─ k8s/
│     ├─ deployment.yaml
│     └─ service.yaml
├─ tests/
│  └─ test_smoke.py
├─ requirements.txt
├─ Makefile
└─ README.md
```