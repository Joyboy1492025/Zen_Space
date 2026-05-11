# ZenSpace - Focus Session Manager

A beautiful, minimalist web application for managing focused work sessions and mindfulness breaks. ZenSpace helps you stay productive with customizable timers, dark mode, and a serene glassmorphism interface.

## ✨ Features

- **Create Focus Sessions**: Set custom duration and categories for your work sessions
- **Real-time Timer**: Visual countdown with large, easy-to-read display
- **Multiple Categories**: Organize sessions by Productivity, Mindfulness, or Rest
- **Dark Mode**: Toggle between light and dark themes for comfortable use
- **Audio Notification**: Get alerted when your session ends
- **Session Management**: View all your sessions and delete completed ones
- **Glassmorphism UI**: Modern, elegant design with smooth transitions
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository** (if not already done):
```bash
git clone https://github.com/Joyboy1492025/Zen_Space.git
cd Zen_Space
```

2. **Create a virtual environment**:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the application**:
```bash
python app.py
```

5. **Open your browser**:
Navigate to `http://localhost:5000`

## 📋 Usage

### Creating a Focus Session
1. Click the **"+ New Space"** button in the top right
2. Enter a session name (e.g., "Deep Work", "Meditation")
3. Set the duration in minutes
4. Select a category: Productivity, Mindfulness, or Rest
5. Click **"Create"** to add the session

### Starting a Session
1. Click **"Start Session"** on any card
2. The timer will display a large countdown
3. Your other sessions will fade away
4. When time is up, an alarm will sound

### Ending a Session
- Click **"End Focus Session"** to return to the main view

### Managing Sessions
- Delete a session by clicking the **"✕"** button on its card
- All sessions are saved to the database

### Theme Toggle
- Click the **"🌙"** button to switch between light and dark modes

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, Tailwind CSS
- **JavaScript**: Vanilla JS for interactivity
- **Styling**: Tailwind CSS with custom glassmorphism effects
- **Fonts**: Plus Jakarta Sans (Google Fonts)

## 📁 Project Structure

```
Zen_Space/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── instance/             # Instance folder (auto-created, contains database)
│   └── zenspace.db
└── templates/
    └── index.html        # Main HTML template
```

## 🗄️ Database Schema

### Space Model
- `id` (Integer): Primary key
- `title` (String): Session name
- `duration` (Integer): Duration in minutes
- `category` (String): Category type (default: "Mindfulness")
- `created_at` (DateTime): Creation timestamp

## 🔧 Configuration

Key settings in `app.py`:
```python
app.config['SECRET_KEY'] = 'zen_secret_777'  # Change in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zenspace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

## 📦 Dependencies

- **Flask**: Web framework
- **Flask-SQLAlchemy**: ORM for database management

See `requirements.txt` for exact versions.

## 🌐 Browser Compatibility

- Chrome/Edge (Latest)
- Firefox (Latest)
- Safari (Latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🎨 Customization

### Change Theme Colors
Edit the CSS variables in `templates/index.html`:
```css
:root { 
  --bg: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
  --card: rgba(255, 255, 255, 0.4);
  --text: #1e293b;
}
```

### Modify Categories
Update the `<select>` element in the modal form in `templates/index.html`

### Change Alarm Sound
Replace the audio URL in `templates/index.html`

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| Database errors | Delete `instance/zenspace.db` and restart the app |
| Port 5000 in use | Change `app.run(port=5001)` in `app.py` |
| Styling not loading | Clear browser cache and hard refresh (Ctrl+Shift+R) |
| Timer not working | Ensure JavaScript is enabled in your browser |

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 👨‍💻 Author

**Joyboy1492025** - [GitHub Profile](https://github.com/Joyboy1492025)

---

**Remember**: The goal isn't just to work, but to work intentionally. Take your breaks. Be present. Stay Zen. 🧘‍♀️
