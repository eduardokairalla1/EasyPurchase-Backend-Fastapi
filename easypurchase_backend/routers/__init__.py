"""
HTTP routers.
"""

# --- IMPORTS ---
from easypurchase_backend.routers import system
from fastapi import FastAPI


# --- CODE ---
def mount(app: FastAPI) -> None:
    """
    Mount all routers on application.

    :param app: main app router

    :returns: nothing
    """
    app.include_router(system.router, tags = ['system'])
