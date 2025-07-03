#!/usr/bin/env python3
"""
TEST VERSION of 20-20-20 Rule Eye Care App
==========================================
This is a FAST version for testing - runs every 30 seconds instead of 20 minutes!
Use this to make sure everything works before using the real app.
"""

# Import the tools we need
import time           # For timers and delays
import threading      # For running multiple things at once
from plyer import notification  # For showing desktop notifications

# ============================================================================
# TEST SETTINGS - Much faster for testing!
# ============================================================================

WORK_TIME = 30         # 30 seconds (instead of 20 minutes)
REST_TIME = 5          # 5 seconds for notification (instead of 20)
NOTIFICATION_TITLE = "🧪 TEST: Time to Rest Your Eyes!"
NOTIFICATION_MESSAGE = """This is a TEST notification!

In the real app, this appears every 20 minutes.
This test runs every 30 seconds.

Look around for 5 seconds! 👁️"""

# ============================================================================
# FUNCTIONS - Same as the real app, just faster
# ============================================================================

def show_notification():
    """Shows a test notification"""
    try:
        notification.notify(
            title=NOTIFICATION_TITLE,
            message=NOTIFICATION_MESSAGE,
            timeout=REST_TIME,
            app_name="Eye Care Test"
        )
        print("✅ TEST notification sent!")
    except Exception as error:
        print(f"❌ Could not show notification: {error}")
        print("💡 Try installing: sudo apt install libnotify-bin")

def countdown_timer(seconds):
    """Counts down in seconds (for testing)"""
    while seconds > 0:
        if seconds <= 10:  # Show countdown for last 10 seconds
            print(f"⏰ {seconds} seconds until test notification...")
        time.sleep(1)
        seconds -= 1

def test_cycle():
    """Fast test cycle"""
    cycle_count = 1
    
    while cycle_count <= 3:  # Only run 3 cycles for testing
        print(f"\n🧪 TEST CYCLE #{cycle_count} of 3")
        print(f"⏳ Waiting {WORK_TIME} seconds...")
        
        countdown_timer(WORK_TIME)
        
        print("🔔 TEST: Time for an eye break!")
        show_notification()
        
        print(f"😌 Resting for {REST_TIME} seconds...")
        time.sleep(REST_TIME)
        
        print("✨ Test break complete!")
        cycle_count += 1
    
    print("\n🎉 Test completed successfully!")
    print("✅ Your app is working! Now you can use the real version.")

# ============================================================================
# MAIN TEST PROGRAM
# ============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("🧪  TESTING YOUR EYE CARE APP  🧪")
    print("=" * 50)
    print("⚡ This is a FAST test version")
    print(f"⏰ Test timer: Every {WORK_TIME} seconds (not 20 minutes)")
    print(f"⏸️  Test break: {REST_TIME} seconds (not 20 seconds)")
    print("🔢 Will run 3 cycles then stop")
    print("🛑 To stop early: Press Ctrl + C")
    print("=" * 50)
    
    try:
        print("🧪 Testing notification system...")
        notification.notify(
            title="🎉 Eye Care Test Started!",
            message="Testing if notifications work on your system!",
            timeout=3
        )
        
        print("✅ Test started! Watch for notifications...")
        test_cycle()
        
    except KeyboardInterrupt:
        print("\n\n👋 Test stopped by user.")
        
    except Exception as error:
        print(f"\n❌ Test error: {error}")
        print("💡 Make sure you've installed: pip3 install plyer")