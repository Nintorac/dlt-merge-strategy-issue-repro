#!/bin/bash

# Create the MinIO bucket
./mc mb minio/repro

# Run the Python script
python repro.py
