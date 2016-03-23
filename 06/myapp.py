from flask import Flask
import ConfigParser
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    env = os.environ.get("ENVIRONMENT", "devel")
    assert env in ("devel", "staging", "prod")

    cfg_file = "%s.cfg" % env
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfg_file)
    
    # set config for application
    app.config = cfg

    app.run()
