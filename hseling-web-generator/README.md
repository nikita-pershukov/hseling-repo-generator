# HSELing Generator

## How to run without Docker

To run Web Application:

```bash
export HSELING_RPC_ENDPOINT=http://localhost:5000/rpc/
export PYTHONPATH=hseling-web-generator
python3 hseling-web-generator/hseling_web_generator/main.py
```

To run RPC server:

```bash
PYTHONPATH=hseling-lib-generator:hseling-api-generator python hseling-api-generator/hseling_api_generator/main.py
```

## How to run using Docker Compose

