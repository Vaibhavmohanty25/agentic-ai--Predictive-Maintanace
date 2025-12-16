"""
Demo scenario helpers.
Used to force deterministic demo behavior.
"""

from app.core import config


def enable_normal_mode():
    config.DEMO_MODE = "normal"
    print("✅ Demo set to NORMAL mode")


def enable_failure_mode():
    config.DEMO_MODE = "failure"
    print("⚠️ Demo set to FAILURE mode")


def current_mode():
    return config.DEMO_MODE
