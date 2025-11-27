"""
Data Preprocessing Script
Task 1: Data Preprocessing

This script cleans and preprocesses the scraped reviews data.
- Handles missing values
- Normalizes dates
- Cleans text data
"""
import os
import sys
import pandas as pd
from datetime import datetime 
from config import DATA_PATHS
import re