from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zen_secret_777'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zenspace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Space(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), default="Mindfulness")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    spaces = Space.query.order_by(Space.created_at.desc()).all()
    return render_template('index.html', spaces=spaces)

@app.route('/add', methods=['POST'])
def add_space():
    # These strings inside .get() MUST match the 'name' attribute in HTML
    title = request.form.get('title')
    duration = request.form.get('duration')
    category = request.form.get('category')

    if title and duration:
        try:
            new_space = Space(title=title, duration=int(duration), category=category)
            db.session.add(new_space)
            db.session.commit()
        except Exception as e:
            print(f"Error: {e}")
    
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_space(id):
    space = Space.query.get_or_404(id)
    db.session.delete(space)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)