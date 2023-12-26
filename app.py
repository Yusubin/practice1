from flask import Flask
from flask import request
from AI.connectdb import db_read
from AI.pos_neg import labeling,label
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dbconnect")
def execute_db_read():
    result = db_read(1)  # Execute the specific function from the module
    return f"Result: {result}"


@app.route("/posnega")
def positive_negative():
    result = labeling(1)  # Execute the specific function from the module
    return f"Result: {result}"

@app.route('/label', methods=['GET', 'POST'])
def label_review():
    if request.method == 'POST':
        title = request.form['title']  # 사용자로부터 입력된 제목을 받습니다.
        result = label(title)  # labeling 함수에 사용자 입력을 전달하여 결과를 받습니다.
        return f'The label for "{title}" is {result}'  # 결과를 출력합니다.
    return '''
        <form method="post">
            <label for="title">Enter review title:</label><br>
            <input type="text" id="title" name="title"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == "__main__":
    app.run()
