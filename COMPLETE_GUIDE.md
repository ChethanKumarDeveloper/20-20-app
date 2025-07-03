# 20-20-20 Rule Eye Care App - Complete Beginner's Guide

Welcome! This guide will help you create an app that reminds you to rest your eyes every 20 minutes using the 20-20-20 rule.

## What is the 20-20-20 Rule?
Every 20 minutes, look at something 20 feet away for 20 seconds to reduce eye strain from screens.

## Step 1: Install Python

First, let's check if Python is already installed and install it if needed:

1. **Open Terminal** (press `Ctrl + Alt + T`)
2. **Check if Python is installed** by typing:
   ```bash
   python3 --version
   ```
3. **If you see a version number** (like Python 3.8.10), great! Python is installed.
4. **If you get "command not found"**, install Python:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

## Step 2: Install VS Code (if not already installed)

1. **Download VS Code**:
   ```bash
   sudo snap install --classic code
   ```
   OR visit: https://code.visualstudio.com/download and download the .deb file

2. **Open VS Code**:
   ```bash
   code
   ```

## Step 3: Install VS Code Extensions

1. **Open VS Code**
2. **Click the Extensions icon** (squares icon on the left sidebar)
3. **Search for and install**:
   - "Python" (by Microsoft)
   - "Python Debugger" (by Microsoft)

## Step 4: Set Up Your Project

1. **Create a new folder** for your app:
   ```bash
   mkdir ~/eye-care-app
   cd ~/eye-care-app
   ```

2. **Open this folder in VS Code**:
   ```bash
   code .
   ```

## Step 5: Install Required Libraries

1. **In VS Code, open Terminal** (Terminal → New Terminal)
2. **Install the notification library**:
   ```bash
   pip3 install plyer
   ```

## Step 6: The Code (Already Created for You!)

The main app file `eye_care_app.py` is already in your project. Here's what each part does:

### Key Parts Explained:

1. **Import libraries**: We bring in tools for timers, notifications, and threading
2. **Timer function**: Counts down 20 minutes (1200 seconds)
3. **Notification function**: Shows the eye rest reminder for 20 seconds
4. **Main loop**: Repeats the cycle forever

## Step 7: Test Your App

1. **In VS Code Terminal, run**:
   ```bash
   python3 eye_care_app.py
   ```

2. **What should happen**:
   - You'll see "20-20-20 Eye Care App started!"
   - After 20 minutes, a notification will appear
   - The notification stays for 20 seconds
   - The cycle repeats

3. **To stop the app**: Press `Ctrl + C` in the terminal

## Step 8: Make it Start Automatically

### Option 1: Using Startup Applications (Easiest)

1. **Open "Startup Applications"**:
   - Press `Super` key (Windows key) and search "Startup"
   - Or run: `gnome-session-properties`

2. **Click "Add"**
3. **Fill in**:
   - **Name**: Eye Care App
   - **Command**: `/usr/bin/python3 /home/$(whoami)/eye-care-app/eye_care_app.py`
   - **Comment**: 20-20-20 rule reminder

4. **Click "Add"** and close

### Option 2: Using systemd (Advanced)

If Option 1 doesn't work, we can create a system service. Let me know if you need help with this.

## Step 9: Customize Your App

You can easily change the timing by editing these numbers in `eye_care_app.py`:

- **Change timer length**: Modify `WORK_TIME = 20 * 60` (currently 20 minutes)
- **Change notification time**: Modify `REST_TIME = 20` (currently 20 seconds)
- **Change message**: Edit the text in `show_notification()`

## Troubleshooting

### If notifications don't appear:
```bash
sudo apt install libnotify-bin
```

### If you get permission errors:
```bash
sudo chmod +x eye_care_app.py
```

### If Python3 isn't found:
Make sure Python 3 is installed and try using `python` instead of `python3`

## How to Stop the App

- **If running in terminal**: Press `Ctrl + C`
- **If running automatically**: 
  1. Open System Monitor (`gnome-system-monitor`)
  2. Find "python3" process running "eye_care_app.py"
  3. Click "End Process"

## Next Steps

Once everything is working:
1. The app will start automatically when you log in
2. You'll get reminders every 20 minutes
3. Just follow the notification's advice: look 20 feet away for 20 seconds!

## Need Help?

If something isn't working:
1. Check that Python 3 is installed
2. Make sure you're in the right folder
3. Verify the notification library is installed
4. Check that the file permissions are correct

Your eye health is important! This simple app will help protect your vision during long computer sessions.