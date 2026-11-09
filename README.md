## Running both services

Use two Codespaces terminals. Start the Product Service first.

**Terminal 1 — Product Service, port 8001**

```bash
uvicorn product_service.main:app --host 0.0.0.0 --port 8001 --reload
```

This serves `GET /products/{product_id}`. Product 1 is the Laptop (899.0). Product 2 is the Mouse (25.0).

**Terminal 2 — user API, port 8000**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## PRODUCT_SERVICE_URL

`PRODUCT_SERVICE_URL` is the base URL of the Product Service. `app/product_client.py` reads it from the environment. The default is `http://127.0.0.1:8001`.

A call for product 1 goes to `{PRODUCT_SERVICE_URL}/products/1`. With the default, that is `http://127.0.0.1:8001/products/1`.

Set it in Terminal 2 before starting the user API if the Product Service is not on that address:

```bash
export PRODUCT_SERVICE_URL=http://127.0.0.1:8001
```

## GET /api/products/{product_id}

This route is on the user API (port 8000). It calls the Product Service with HTTPX and returns that product.

```bash
curl http://127.0.0.1:8000/api/products/1
```

```json
{"id": 1, "name": "Laptop", "price": 899.0}
```

| Status | When |
|---|---|
| 200 | That product id exists |
| 404 | The Product Service has no product with that id |
| 503 | The Product Service is not running, or the connection fails |