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
    with Connection("root@92fcd47de30b"):
        # Navigate to the project directory
        with ctx.cd(BASE_DIR):
            # Update the codebase from the Git repository
            ctx.run("git pull origin main")

            # Install or update Python dependencies
            ctx.run("pip install -r requirements.txt")

            # Restart Gunicorn to apply changes
            restart_gunicorn(ctx)

@task
def restart_gunicorn(ctx):
    # Connect to the server
    with Connection("root@92fcd47de30b"):
        # Restart Gunicorn service
        ctx.sudo(f"systemctl restart {GUNICORN_SERVICE}")

