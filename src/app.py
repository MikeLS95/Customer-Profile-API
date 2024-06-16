from init import app

@app.route('/')
def index():
    return 'Customer Travel Profile API.'
