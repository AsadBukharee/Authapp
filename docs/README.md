### Project Setup

clone the code from repository. and make sure that you are in main branch.

`git clone `

### Database setup:
you can update db env vars in respective .env file. by default its .env.dev (so just update it accordingly) you can update and use your .enc.local if needed.

if you want to create your own database just run `init_pg_db_win.bat` for windows 🪟 and `init_pg_db_lnx.sh` for ubuntu🐧.
it can ask system password, sudo to be used in ubuntu.

at this point you should have a running database instance.


### ASGI Server selection

## Choosing Between Uvicorn and Hypercorn

1. **Use Uvicorn if:**

    - You are building a FastAPI application and need high performance.
    - You are looking for a server with a large community and extensive support.
    - You need a lightweight server that is straightforward to deploy and manage.

2. Use Hypercorn if:
    - You need support for HTTP/3 or specific worker configurations.
    - You are working on an application where flexibility in server configuration is crucial.
    - You want to experiment with new protocols or features beyond HTTP/2.

**_So we will go with uvicorn for high performance and simplicity, especially because we are  using FastAPI_**