from flask import Blueprint

main = Blueprint('main', __name__)

# Remeber to include all the other parts, or the blueprint would have no routes
from . import index
