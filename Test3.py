from playwright.sync_api import sync_playwright


class TrainingPage:
    def __init__(self, page):
        self.page = page
        self.training_menu = page.locator("text=TRAINING").first
        self.software_testing_link = page.locator("a:has-text('Software Testing')").first

    def open_software_testing_page(self):
        print("Step 1: Waiting for Training Menu...")
        self.training_menu.wait_for(state="visible", timeout=15000)

        print("Step 2: Clicking Training Menu...")
        try:
            self.training_menu.click()
        except:
            self.training_menu.click(force=True)

        print("Step 3: Waiting for Software Testing link...")
        self.software_testing_link.wait_for(state="visible", timeout=15000)

        print("Step 4: Clicking Software Testing...")
        try:
            self.software_testing_link.click()
        except:
            self.software_testing_link.click(force=True)

        print("Step 5: Waiting for navigation...")
        self.page.wait_for_load_state("domcontentloaded")


def run_scenario3_test():
    with sync_playwright() as p:
        print("\nStarting Test Scenario 3...")

        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Stable navigation (handles slow site)
        try:
            page.goto(
                "https://midbrainsacademy.in/",
                wait_until="load",
                timeout=60000
            )
        except:
            print("⚠️ Slow load, retrying...")
            page.goto(
                "https://midbrainsacademy.in/",
                wait_until="commit"
            )

        tp = TrainingPage(page)
        tp.open_software_testing_page()

   
        # VALIDATION (URL + HEADING)
      
        current_url = page.url
        print("Current URL:", current_url)

        url_check = "software-testing" in current_url.lower()

        try:
            heading = page.locator("h1").text_content()
        except:
            heading = ""

        heading_check = "software testing" in heading.lower()

        if url_check or heading_check:
            print("✅ SUCCESS: Correct page opened")
        else:
            print("❌ FAILED: Wrong page")
            assert False

        browser.close()


if __name__ == "__main__":
    run_scenario3_test()