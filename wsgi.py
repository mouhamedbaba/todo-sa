import sys
from constant import DEBUG

project_home = "/"

if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from app import app


if __name__ == "__main__":
    app.run(debug=DEBUG)