#!/usr/bin/python3
"""Checks code for pycodestyle"""
import os
import pycodestyle

def check_repo_pycodestyle(repo_path):
    style = pycodestyle.StyleGuide()
    result = style.check_files([repo_path])
    if result.total_errors == 0:
        print("No PEP8 style violations found!")
    else:
        print(f"{result.total_errors} PEP8 style violations found.")

repo_path = os.path.join(os.getcwd(), 'my_repo')
check_repo_pycodestyle(repo_path)
