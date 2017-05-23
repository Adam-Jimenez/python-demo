from orm.alchemy import session
from orm.food import Food
from flask import Flask, request
import json
app = Flask(__name__)

def jsonmoica(func):
    def inner(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    inner.func_name = func.func_name
    return inner

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/food/')
@jsonmoica
def get_all_food():
    return [{'name': a.name, 'desc': a.description, 'id': a.id}
            for a in session.query(Food).all()]

@app.route('/food/add/')
@jsonmoica
def add_food():
    food = Food(name=request.args.get('name'),
                description=request.args.get('description'),
                category=request.args.get('category'))
    try:
        session.add(food)
        session.commit()
        return True
    except:
        session.rollback()
        return False

@app.route('/food/del/<foodId>')
@jsonmoica
def delete_food(foodId):
    food = session.query(Food).get(foodId)
    if food:
        try:
            session.delete(food)
            session.commit()
            return True
        except:
            session.rollback()
            return False

if __name__ == '__main__':
    app.run(port=5000)
