"""
Global service objects.
"""

# --- IMPORTS ---
from easypurchase_backend.models import Config
from easypurchase_backend.models import Health
from easypurchase_backend.models import Info
from fastapi import FastAPI


# --- CODE ---
# FastAPI app
app = FastAPI(
    title = 'Easypurchase',
    description = 'This is the general backend service of Easy Purchase'
)

# Configuration
config = Config()

# Info
info = Info(
    name = app.title,
    description = app.description,
    version = app.version,
    extra = {}
)

# System health
health = Health()
