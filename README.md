### Installation
```python
python -m venv venv #creating venv for Windows
---------------
python3 -m venv venv #creating venv for MacOS/Linux
---------------
venv/scripts/activate # windows
---------------
source venv/bin/activate # macOS/Linux
pip install -r requirements.txt #installing packages
py run.py #running app and creating instance folder
flask db migrate #migrating models
flask db upgrade #adding models in db


```
----------------------------------------------------
### Features
**Create secret**: Users can create a **one time **secret by entering a secret phrase for accesing his secret text. 
> Each secret is identified by a unique key .

**Encryption**: Secrets are securely encrypted via Fernet encryption method.

**One Time Access**: Each secret can only be seen once. After the secret is retrieved, it is deleted from the database permanently, preventing unauthorized future access.

**JSON Format**: There is the option to receive the secret in JSON format for easier integration with other applications.

