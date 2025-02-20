from flask import Flask
import os
import datetime
import subprocess
import pytz

app = Flask(_name_)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"

    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get top command output (first 10 lines)
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -10", shell=True, text=True)
    except Exception as e:
        top_output = f"Error retrieving top output: {str(e)}"

    # HTML output
    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> Yashas</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
