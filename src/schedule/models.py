from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, index=True)
    row_type = db.Column(db.String(16), nullable=False)  # 'top' (мероприятия) или 'bottom' (спектакли)
    place = db.Column(db.String(64))  # Для спектаклей: площадка, для репетиций: место
    event_type = db.Column(db.String(16), nullable=False)  # 'performance', 'rehearsal', 'meeting'
    start_time = db.Column(db.String(5), nullable=False)  # HH:MM
    end_time = db.Column(db.String(5))  # HH:MM, время завершения мероприятия
    title = db.Column(db.String(128), nullable=False)
    stage_manager = db.Column(db.String(64))  # Помреж (только для спектакля)
    cast = db.Column(db.Text)  # Артисты и роли (только для спектакля)
    resources = db.Column(db.String(128))  # Ресурсы (только для репетиции)
    participants = db.Column(db.String(256))  # Участники (только для репетиции)
    responsible_1 = db.Column(db.String(64))  # Ответственный (только для репетиции)
    responsible_2 = db.Column(db.String(64))  # Ответственный 2 (только для репетиции)
    author = db.Column(db.String(128))  # Автор последнего изменения карточки
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
