import httpx 
from fastapi import Depends, FastAPI, HTTPException 
from app.product_client import get_product_fetcher 
app = FastAPI(title="Lab 5")
  
@app.get("/api/products/{product_id}") 
def get_remote_product( 
    product_id: int, 
    product_fetcher=Depends(get_product_fetcher), 
): 

    try: 
        return product_fetcher(product_id) 
    except httpx.HTTPStatusError as exc: 
        if exc.response.status_code == 404: 
            raise HTTPException(404, "Product not found") from exc 
    except httpx.RequestError as exc: 
        raise HTTPException(503, "Product service unavailable") from exc