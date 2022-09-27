from flask import Flask, render_template, request
from Users import Users


a=Users()
a.Default_Users()

app=Flask(__name__)

@app.route('/api/<name>/get/users')
def hell(name):
    return a.RetUsers(n=name)

@app.route('/api/post/users')  
def post():
    return render_template('post.html')


@app.route('/api/put/users/<id>')
def put(id):
    return render_template('put.html')


@app.route('/api/delete/users/<id>')
def delete():
    return render_template('post.html')

if __name__ == '__main__':
    app.run()



