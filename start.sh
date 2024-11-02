#!/bin/bash

# Start the Flask application with Gunicorn in the background
gunicorn -b 0.0.0.0:5000 main:app &
gunicorn_pid=$!

# Start the cleanup process in the background
python cleanup.py &
cleanup_pid=$!

wait $gunicorn_pid
wait $cleanup_pid