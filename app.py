# -*- coding: utf-8 -*-
import os
import random
import json
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name=None)


@app.route('/grouping/', methods=['POST', 'GET'])
def proc_post_request():
    ''' 
    dispatch RPC request

    '''

    if request.method == 'POST':
        total = request.form['total']
        group = request.form['group']
        result = grouping(total, group)
        #result=search_zipcode(request.form['zipcode'])
        res = make_response(result)
        res.headers['Cache-Control'] = 'no-cache'
        return res
    else:
        return 'Please PSOT Method'

def grouping(total, group):
    '''
    全体の人数とグループ数から各グループの数を求める
    各グループにランダムに人数を配置する。

    '''
    try:
        number_total = int(total)
        number_group = int(group)
    except:
        return None
    
    number_per_group = number_total / number_group

    persons = range(1, number_total + 1)
    groups = range(1, number_group + 1)


    # create group
    group_dic = {}
    for group in groups:
        group_dic["%s" % group] = []

    random.shuffle(persons)
    for key in group_dic.keys():
        for enumrate in range(0, number_per_group):
            group_dic[key].append('%s番さん' % persons.pop())
            if not len(persons):
                break
        
    # encode json? 
    return json.dumps(group_dic)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
