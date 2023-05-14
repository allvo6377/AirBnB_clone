#!/usr/bin/python3
"""
method for the models directory
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
