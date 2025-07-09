from flask import Blueprint, render_template, current_app
from datetime import date, timedelta

schedule_bp = Blueprint('schedule', __name__)

def get_mock_schedule():
    today = date.today()
    days = [today + timedelta(days=i) for i in range(7)]
    # Моковые данные для тестовой витрины
    schedule = []
    for idx, d in enumerate(days):
        # Верхняя строка: репетиции и собрания
        top = []
        if idx == 0:
            top.extend(
                (
                    {
                        "event_type": "rehearsal_group",
                        "place": "Большая сцена",
                        "resources": "Свет, Звук",
                        "title": "Гамлет",
                        "rehearsals": [
                            {
                                "start_time": "10:00",
                                "end_time": "",
                                "participants": "ВСЕ ЗАНЯТЫЕ, кроме Чурбакова",
                                "responsible_1": "А. Марин",
                                "responsible_2": "В. Левшина",
                            },
                            {
                                "start_time": "11:30",
                                "end_time": "13:00",
                                "participants": "Полицеймако, Иванов",
                                "responsible_1": "А. Марин",
                                "responsible_2": "",
                            }
                        ],
                        "author": "testuser",
                    },
                    {
                        "event_type": "meeting",
                        "place": "",
                        "resources": "",
                        "start_time": "14:00",
                        "end_time": "",
                        "title": "Сбор труппы",
                        "participants": "",
                        "responsible_1": "",
                        "responsible_2": "",
                        "author": "testuser",
                    },
                )
            )
        elif idx == 1:
            top.append({
                "event_type": "rehearsal",
                "place": "МРЗ",
                "resources": "костюмы.видео.грим. свет. остальное",
                "start_time": "11:00",
                "end_time": "13:30",
                "title": "Ревизор",
                "participants": "Козлова, Орлов",
                "responsible_1": "В. Орлов",
                "responsible_2": "Е. Козлова",
                "author": "testuser",
            })
        elif idx == 2:
            top.append({
                "event_type": "rehearsal",
                "place": "Реп. зал",
                "resources": "ЗВУК,СВЕТ",
                "start_time": "12:00",
                "end_time": "14:00",
                "title": "Танцевальная репетиция",
                "participants": "Все занятые в танцах",
                "responsible_1": "М.С. Плесецкая",
                "responsible_2": "",
                "author": "testuser",
            })
        # Нижняя строка: спектакли
        bottom = []
        if idx == 0:
            bottom.append({
                "event_type": "performance",
                "place": "Большая сцена",
                "start_time": "19:00",
                "end_time": "21:30",
                "title": "Гамлет",
                "stage_manager": "С. Иванова",
                "cast": "Гамлет — Петров, Офелия — Козлова, Полоний — Орлов",
                "author": "testuser",
            })
        if idx == 1:
            bottom.extend(
                (
                    {
                        "event_type": "performance",
                        "place": "Чердак сатиры",
                        "start_time": "18:00",
                        "end_time": "20:00",
                        "title": "Ревизор",
                        "stage_manager": "А. Смирнова",
                        "cast": "Городничий — Сидоров, Хлестаков — Иванов",
                        "author": "testuser",
                    },
                    {
                        "event_type": "performance",
                        "place": "Большая сцена",
                        "start_time": "20:00",
                        "end_time": "22:00",
                        "title": "Мастер и Маргарита",
                        "stage_manager": "В. Орлов",
                        "cast": "Мастер — Петров, Маргарита — Козлова",
                        "author": "testuser",
                    },
                )
            )
        if idx == 2:
            bottom.append({
                "event_type": "performance",
                "place": "Прогресс",
                "start_time": "17:00",
                "end_time": "19:00",
                "title": "Эксперимент",
                "stage_manager": "М. Хоров",
                "cast": "Актёры — труппа театра",
                "author": "testuser",
            })
        schedule.append({'date': d, 'top': top, 'bottom': bottom})
    return schedule

@schedule_bp.route("/schedule")
def show_schedule():
    # Для тестовой страницы используем моковые данные
    schedule = get_mock_schedule()
    return render_template("schedule.html", schedule=schedule, config=current_app.config)

@schedule_bp.route("/")
def print_ok():
    return "ok"
