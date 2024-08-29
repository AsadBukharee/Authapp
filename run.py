import sys
import os
import uvicorn

def load_env(environment):
    env_file = f"env/.env.{environment}"
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Environment file {env_file} not found.")

    with open(env_file) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            key, value = line.strip().split("=", 1)
            os.environ[key] = value

def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py [env]")
        sys.exit(1)

    env = sys.argv[1]
    if not env:
        env = 'dev'
    load_env(env)

    # Directly call uvicorn.run() to start the FastAPI app
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",   # or your desired host
        port=8000,        # or your desired port
        reload=True
    )

if __name__ == "__main__":
    main()
