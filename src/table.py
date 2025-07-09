import os
from flask import Flask
from schedule.views import schedule_bp
from schedule.models import db
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///theatre_schedule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SCHED_PAGETITLE'] = os.environ.get('SCHED_PAGETITLE', 'Витрина театрального расписания')

db.init_app(app)
app.register_blueprint(schedule_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    uHost = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
    uPort = int(os.getenv('FLASK_RUN_PORT', 5000))
    uDebug=os.getenv('FLASK_DEBUG', True)
    app.run(debug=uDebug,host=uHost,port=uPort)
