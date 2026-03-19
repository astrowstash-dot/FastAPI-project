from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import route_predict, routes_auth
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handler

app = FastAPI(title="Car Price Prediction API")

# link middleware
app.add_middleware(LoggingMiddleware)

# link endpoints
app.include_router(routes_auth.router, tags= ["Auth"])
app.include_router(route_predict.router, tag= ["Prediction"])

# Monetring using prometheus

Instrumentator().instrument(app).expose(app)

# add exception handler 

register_exception_handler(app)


