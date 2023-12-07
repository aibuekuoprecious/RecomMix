# fabfile.py

from fabric import task, Connection

# Define the paths
BASE_DIR = "/RecomMix"
APP_DIR = f"{BASE_DIR}/app"

# Define the Gunicorn service name
GUNICORN_SERVICE = "recommix"

@task
def deploy(ctx):
    # Connect to the server
    with Connection("root@92fcd47de30b") as conn:
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

