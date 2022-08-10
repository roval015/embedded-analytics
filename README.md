to run the virtual environment
- python -m venv venv
- . venv/Scripts/activate
- if it does not work, change the restriction: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

to run the existing docker image
- docker run -ip 5000:5000 embedded-analytics

to re-buld the docker image after doing some edits on the source code
- docker build -t embedded analytics .