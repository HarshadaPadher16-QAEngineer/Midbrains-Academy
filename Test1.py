#Homepage Validation

#Verify page loads successfully
#Validate title URL 
#Check main sections visibility


from playwright.sync_api import sync_playwright

def run_homepage_test():
    with sync_playwright() as p:
        # Use the 'args' for maximize the screen while the launch browser.  
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        
        # 'no_viewport=True' use for full window size by set throught screen.
        page = browser.new_page(no_viewport=True)

        # 1. CASE: Verify page loads successfully
        print("Scenario 1: Opening the website...")

        # 'networkidle' use 'load' this is stable.
        page.goto("https://midbrainsacademy.in", wait_until="domcontentloaded", timeout=60000)
        print("Page loaded successfully!")

        # 2. CASE: Validate Title and URL
        print("Scenario 2: Validating Title and URL...")
        
        actual_title = page.title()
        print(f"Actual Title: {actual_title}")
        assert "Midbrain" in actual_title, f"Title mismatch! Got: {actual_title}"

        actual_url = page.url
        print(f"Actual URL: {actual_url}")
        assert "midbrainsacademy.in" in actual_url, f"URL mismatch! Got: {actual_url}"

        # 3. CASE: Check main sections visibility
        print("Scenario 3: Checking main section visibility...")
        
        main_section = page.locator("body")
        if main_section.is_visible():
            print("Success: Main section is visible on the screen.")
        else:
            print("Error: Main section is not visible.")

        # Wait for some time
        print("Waiting for 3 seconds before closing...")
        page.wait_for_timeout(3000)

        # Close the Browser 
        # browser.close()
        print("Test Completed Successfully!")

if __name__ == "__main__":
    run_homepage_test()