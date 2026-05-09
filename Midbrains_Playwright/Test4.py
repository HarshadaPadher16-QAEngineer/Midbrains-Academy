from playwright.sync_api import sync_playwright


def test_contact_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Fast page load
        page.goto("https://midbrainsacademy.in/contact.html", wait_until="domcontentloaded")


        # TEST 1: Valid Form
        page.fill("input[name='name']", "Harshada")
        page.fill("input[name='phone']", "8888160236")
        page.fill("input[name='email']", "harshadapadher25@gmail.com")
        page.fill("textarea[name='message']", "Valid data")

        page.click("button[type='submit']")

        # Wait properly (no hard timeout)
        page.wait_for_load_state("networkidle")

        redirected = "contact" not in page.url
        success_msg = page.locator("#success-msg").is_visible()

        if redirected or success_msg:
            print("✅ Valid Form PASS")
        else:
            print("❌ Valid Form FAIL")

      
        # TEST 2: Invalid Form
        page.fill("input[name='name']", "xyz")
        page.fill("input[name='phone']", "88sgd13546")
        page.fill("input[name='email']", "pqr@gmail")  # invalid email
        page.fill("textarea[name='message']", "test")

        page.click("button[type='submit']")

        try:
            page.locator("#error-msg").wait_for(timeout=3000)
            print("✅ Invalid Form Validation PASS")
        except:
            print("❌ Invalid Form Validation FAIL")

        browser.close()


# Run
test_contact_form()
