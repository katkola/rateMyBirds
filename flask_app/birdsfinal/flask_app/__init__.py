from flask import Flask
app = Flask(__name__)

app.secret_key = 'saodngjw5i0'

@app.template_filter()
def betterdt(dttm):
    return dttm.strftime('%m/%d/%Y')