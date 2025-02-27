from workouthub import db


class Users(db.model):
    # schema for the users model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    workouts = db.relationship("Workout", backref="user", cascade="all, delete", lazy=True)


    def __repr__(self):
        return self.username



class Workout(db.model):
    # schema for the workout model
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), ondelete="CASCADE"nullable=False)
    workout_name = db.Column(db.String(90), unique=True, nullable=False)
    workout_type = db.column(db.String(90), nullable=False)
    exercises = db.relationship("Exercise", backref="workout", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.username




class Exercise(db.model):
    # schema for the exercise model.
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workout.id", ondelete="CASCADE"), nullable=False)
    exercise_name = db.Column(db.String(90), unique=False, nullable=False)
    sets = db.Column(db.Integer(2), nullable=False)
    reps = db.Column(db.Integer(3), nullable=False)

     
    def __repr__(self):
        return f"#{self.exercise_name} - Sets: {self.sets} - Reps: {self.reps}"