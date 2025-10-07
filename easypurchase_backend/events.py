"""
Startup and shutdown event handlers.
"""

# --- IMPORTS ---
from easypurchase_backend import routers
from easypurchase_backend.app import health
from fastapi import FastAPI


# --- CODE ---
def on_startup(app: FastAPI) -> None:
    """
    Initialize the service on startup.
    """
    # Mount routers
    routers.mount(app)

    # Set app health as OK
    health.status = 'OK'


def on_shutdown(app: FastAPI) -> None:  #pylint: disable=W0613
    """
    Run on service shutdown.
    """
    pass
