#!/usr/bin/env python3
"""
20-20-20 Rule Eye Care App
==========================
This app helps protect your eyes from screen strain by reminding you to:
- Every 20 minutes: Look at something 20 feet away for 20 seconds

Simple and effective eye care for computer users!
"""

# Import the tools we need
import time           # For timers and delays
import threading      # For running multiple things at once
from plyer import notification  # For showing desktop notifications
import os
from pathlib import Path

# ============================================================================
# SETTINGS - You can change these numbers!
# ============================================================================

WORK_TIME = 20 * 60    # 20 minutes in seconds (20 × 60 = 1200 seconds)
REST_TIME = 20         # 20 seconds for the notification to stay

# Optional icon (PNG). If the file doesn't exist we fall back to no icon.
ICON_PATH = str(Path(__file__).with_name("eye_icon.png"))

# Prettier title & message
NOTIFICATION_TITLE = "👁️  Time for an Eye Break!"

# Multiline message with bullet points for better readability
NOTIFICATION_MESSAGE = (
    "🕒  20-20-20 Rule\n\n"
    "•  Look at something 20 feet away\n"
    "•  Blink slowly 20 times\n"
    "•  Rest your eyes for 20 seconds\n\n"
    "Your eyes will thank you! 😊"
)

# ============================================================================
# FUNCTIONS - The building blocks of our app
# ============================================================================

def show_notification():
    """
    This function shows a desktop notification.
    It's like the popup notifications you see on your phone!
    """
    try:
        notification.notify(
            title=NOTIFICATION_TITLE,            # Big bold title
            message=NOTIFICATION_MESSAGE,        # Pretty message body
            timeout=REST_TIME,                   # Show for REST_TIME seconds
            app_name="Eye Care App",            # Name shown in popup
            app_icon=ICON_PATH if os.path.exists(ICON_PATH) else None  # Optional icon
        )
        print("✅ Notification sent! Time to rest your eyes.")
    except Exception as error:
        print(f"❌ Could not show notification: {error}")
        print("💡 Try installing: sudo apt install libnotify-bin")

def countdown_timer(minutes):
    """
    This function counts down from the given number of minutes.
    It's like a kitchen timer, but for your eyes!
    """
    total_seconds = minutes * 60
    
    while total_seconds > 0:
        # Calculate minutes and seconds remaining
        mins_left = total_seconds // 60
        secs_left = total_seconds % 60
        
        # Show the countdown (only every minute to avoid spam)
        if secs_left == 0:
            print(f"⏰ {mins_left} minute(s) until next eye break...")
        
        # Wait 1 second
        time.sleep(1)
        total_seconds -= 1

def eye_care_cycle():
    """
    This is one complete cycle of the 20-20-20 rule:
    1. Wait 20 minutes
    2. Show notification for 20 seconds  
    3. Repeat forever
    """
    cycle_count = 1
    
    while True:  # This means "repeat forever"
        print(f"\n🔄 Starting cycle #{cycle_count}")
        print(f"⏳ Working period: {WORK_TIME // 60} minutes...")
        
        # Step 1: Wait for the work period (20 minutes)
        countdown_timer(WORK_TIME // 60)
        
        # Step 2: Show the eye rest notification
        print("🔔 Time for an eye break!")
        show_notification()
        
        # Step 3: Wait while the notification is showing (20 seconds)
        print(f"😌 Resting for {REST_TIME} seconds...")
        time.sleep(REST_TIME)
        
        print("✨ Break complete! Back to work.")
        cycle_count += 1

# ============================================================================
# MAIN PROGRAM - This is where everything starts!
# ============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("👁️  20-20-20 RULE EYE CARE APP  👁️")
    print("=" * 50)
    print("🎯 Goal: Protect your eyes from screen strain")
    print(f"⏰ Timer: Every {WORK_TIME // 60} minutes")
    print(f"⏸️  Break: {REST_TIME} seconds")
    print("🛑 To stop: Press Ctrl + C")
    print("=" * 50)
    
    try:
        # Test if notifications work
        print("🧪 Testing notification system...")
        notification.notify(
            title="🎉 Eye Care App Started!",
            message="Notifications are working! First reminder in 20 minutes.",
            timeout=5
        )
        
        print("✅ App started successfully!")
        print("💡 First reminder will appear in 20 minutes.")
        print("📱 Keep this window open or minimize it.")
        
        # Start the main cycle
        eye_care_cycle()
        
    except KeyboardInterrupt:
        # This happens when user presses Ctrl + C
        print("\n\n👋 Eye Care App stopped by user.")
        print("👁️ Thanks for taking care of your eyes!")
        
    except Exception as error:
        print(f"\n❌ An error occurred: {error}")
        print("💡 Make sure you've installed the required libraries:")
        print("   pip3 install plyer")