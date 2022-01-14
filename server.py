from flask import Flask, render_template
app = Flask(__name__)  


@app.route('/')
@app.route('/play')
def play():
    return render_template('index.html', num = 3, color = 'blue')

@app.route('/play/<int:num>')
def playnum(num):
    if (num < 1):
        num = 1
    return render_template('index.html', num = num, color = 'blue')

@app.route('/play/<int:num>/<string:color>')
def playcolor(num, color):
    if (num < 1):
        num = 1
    return render_template('index.html', num = num, color = color)

if __name__=="__main__":     
    app.run(debug=True)  

