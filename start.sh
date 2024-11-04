#!/bin/bash

# Start the Flask application with Gunicorn in the background
gunicorn -b 0.0.0.0:5000 app/main:app &
gunicorn_pid=$!

# Start the cleanup process in the background
python app/cleanup.py &
cleanup_pid=$!

wait $gunicorn_pid
wait $cleanup_pid