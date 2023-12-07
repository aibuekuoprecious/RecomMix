import os
from fabric import task, Connection

# Get the absolute path to the directory containing this script
CURRENT_DIR = os.path.dirname(__file__)

# Define the paths
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/school")
BASE_DIR = os.path.join("RecomMix")
APP_DIR = os.path.join(BASE_DIR, "app")

# Define the Gunicorn service name
GUNICORN_SERVICE = "recommix"

conn = Connection(
    host='34.224.63.159',
    user='ubuntu',
    connect_kwargs={
        'key_filename': PRIVATE_KEY_PATH
    }
)

@task
def deploy(ctx):
    # Connect to the server
    with Connection("ubuntu@34.224.63.159", connect_kwargs={"key_filename": PRIVATE_KEY_PATH}) as conn:
        # Update the codebase from the Git repository
        conn.run(f"cd {BASE_DIR} && git pull origin main")

        # Install or update Python dependencies
        conn.run(f"cd {BASE_DIR} && pip install -r requirements.txt")

        # Restart Gunicorn to apply changes
        restart_gunicorn(conn)

@task
def restart_gunicorn(conn):
    # Restart Gunicorn service
    conn.sudo(f"systemctl restart {GUNICORN_SERVICE}")

