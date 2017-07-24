# codecrushers

Backend code for rajkot smart city hackathon by team codecrushers.

#### Server-side

* Python 3.5.2
* Django 1.11.3
* PostgreSQL

#### Setup

From inside the repository, run the following commands in the terminal:
 ```
 pyenv local 3.5.2
 virtualenv env
 pip install -r requirements/default.txt
 mv development.cfg.dist development.cfg
 pre-commit install
 pre-commit run
 ```

 Add configuration in development.cfg
