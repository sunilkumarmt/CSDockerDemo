# Render Docker Welcome Lab

A minimal web application for teaching Docker deployments on Render without installing Docker on the instructor's computer.

## Files

- `app.py` — serves a welcome page, reads `WELCOME_MESSAGE`, `APP_VERSION`, and `PORT` environment variables.
- `Dockerfile` — packages the app into a Docker image.

## Deploy on Render

1. Create a new public GitHub repository, e.g. `render-docker-welcome-lab`.
2. Upload `app.py` and `Dockerfile` to the repository root.
3. In Render Dashboard, choose **New → Web Service** and connect that GitHub repository.
4. Set **Language/Runtime** to **Docker** and the Dockerfile path to `Dockerfile` if Render asks.
5. Select the **Free** instance type, name the service, and create/deploy it.
6. Wait for the deploy to finish, then open the generated `https://<service-name>.onrender.com` URL.

No build command or start command is required; Render uses the Dockerfile.

## Environment variables for classroom use

In the Render service's **Environment** settings, add:

- `WELCOME_MESSAGE` = `Hi, welcome to the Computing Systems Lab!`
- `APP_VERSION` = `v1`

Save/apply the changes. Render will restart or redeploy the service as applicable. Refresh the public URL to see the updated message.

## Demonstrating a new image version

1. Edit `app.py` in GitHub (change the default welcome text or other page content).
2. Commit the change to the deployed branch.
3. Render auto-deploys from the connected repository when auto-deploy is enabled.
4. Follow the deploy in Render's **Events/Deploys** view and then refresh the same URL.

For a simple configuration-only change, changing the Render environment variable is quicker; for a source/image change, edit `app.py` and deploy again.

## Notes

- The application binds to `0.0.0.0` and reads Render's `PORT` environment variable (default `10000`).
- `/health` returns `ok` for a simple health check.
- Render Free web services spin down after 15 minutes without inbound traffic and may take about a minute to wake up.
- Free Render web services do not provide SSH or dashboard shell access, so you cannot run `docker ps`, `docker stop`, or `docker rm` on the hosted machine. Use deploys and rollbacks to demonstrate lifecycle changes.
- This demo is public. Do not put secrets, personal data, or administrative functionality in it.
