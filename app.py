import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name=None)


@app.route('/grouping/', methods=['POST', 'GET'])
def proc_post_request():
    """ 
    dispatch RPC request

    """
    if request.method == 'POST':
        total = request.form['total']
        group = request.form['group']
        result = grouping(total, group)
        #result=search_zipcode(request.form['zipcode'])
        return result
    else:
        return 'Please PSOT Method'

def grouping(total, group):
    '''
    '''
    return "%s,%s" %(total,group)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
