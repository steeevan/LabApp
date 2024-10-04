# views/dashboard_utils.py
from tkinter import *

def add_common_dashboard_components(frame, on_logout, on_account_settings):
    """
    Adds common components (logout button and account settings) to the given frame.

    Args:
    - frame (Frame): The frame to which components will be added.
    - on_logout (function): Callback function to handle logout.
    - on_account_settings (function): Callback function to handle account settings.
    """
    # Logout button
    logout_button = Button(frame, text="Logout", command=on_logout, font=('Arial', 12), width=15, fg="red")
    logout_button.pack(side=BOTTOM, pady=10)

    # Account Settings button
    account_settings_button = Button(frame, text="Account Settings", command=on_account_settings, font=('Arial', 12), width=15)
    account_settings_button.pack(side=BOTTOM, pady=5)
