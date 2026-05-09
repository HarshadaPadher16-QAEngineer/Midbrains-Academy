from playwright.sync_api import sync_playwright


def test_button_click_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Fast page load
        page.goto("https://midbrainsacademy.in/contact.html", wait_until="domcontentloaded")

   
        # TEST 1: Empty Form Validation
     
        page.fill("input[name='name']", "")
        page.fill("input[name='phone']", "")
        page.fill("input[name='email']", "")
        page.fill("textarea[name='message']", "")
        page.click("button[type='submit']")

        try:
            page.locator("#error-msg").wait_for(timeout=3000)
            print("✅ Empty Form Validation PASS")
        except:
            print("❌ Empty Form Validation FAIL")

    
        # TEST 2: Invalid Email
      
        page.fill("input[name='name']", "Harshada")
        page.fill("input[name='phone']", "8888160236")
        page.fill("input[name='email']", "wrongEmail")  # invalid
        page.fill("textarea[name='message']", "Testing course")
        page.click("button[type='submit']")

        try:
            page.locator("#error-msg").wait_for(timeout=3000)
            print("✅ Invalid Email Validation PASS")
        except:
            print("❌ Invalid Email Validation FAIL")

        # TEST 3: Valid Form
      
        page.fill("input[name='name']", "Harshada")
        page.fill("input[name='phone']", "8888160236")
        page.fill("input[name='email']", "harshadapadher25@gmail.com")
        page.fill("textarea[name='message']", "I want to join course")
        page.click("button[type='submit']")

        # Wait for submit result (fast + stable)
        page.wait_for_load_state("networkidle")

        if ("contact" not in page.url) or page.locator("#success-msg").is_visible():
            print("✅ Valid Form Submission PASS")
        else:
            print("❌ Valid Form Submission FAIL")

        browser.close()


# Run test
test_button_click_flow()