"""
Optimized & Maintained by @multilogin-automation - Modern Stealth Branch
"""

# MLX Integration Demo: Migrate from local browser to Multilogin X
# Requires: playwright, requests

import requests
from playwright.sync_api import sync_playwright

MLX_API = "http://localhost:35000/api/v2/profile/start"
MLX_PROFILE_ID = "your-profile-id-here"  # Replace with your Multilogin X profile ID


def start_multilogin_profile(profile_id):
    resp = requests.post(MLX_API, json={"profileId": profile_id})
    resp.raise_for_status()
    data = resp.json()
    ws_endpoint = data.get("wsEndpoint")
    if not ws_endpoint:
        raise RuntimeError("No wsEndpoint returned from Multilogin X API")
    return ws_endpoint


def main():
    ws_endpoint = start_multilogin_profile(MLX_PROFILE_ID)
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(ws_endpoint)
        page = browser.new_page()
        page.goto("https://browserleaks.com/ip")
        print("Page title:", page.title())
        browser.close()

if __name__ == "__main__":
    main()
