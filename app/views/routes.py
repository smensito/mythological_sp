from flask import Blueprint, render_template

routes = Blueprint('routes',
                   __name__,
                   template_folder='routes')


@routes.route('/home', methods=['GET'])
def homepage():
    return render_template('home.html')
