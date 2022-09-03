#!/usr/bin/python3
""" Module for Base """

import uuid
from datetime import datetime
from uuid import uuid4
import models
import json

format_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Basemodel class """
    def __init__(self, *args, **kwargs):

