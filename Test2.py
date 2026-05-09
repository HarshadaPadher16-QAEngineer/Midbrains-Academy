from playwright.sync_api import sync_playwright

def run_navigation_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("Step 1: Loading Homepage...")
        page.goto("https://midbrainsacademy.in", wait_until="domcontentloaded", timeout=60000)
        
        menu_items = ["HOME", "ABOUT", "TRAINING", "PLACEMENTS", "INTERNSHIP", "GALLERY", "CAREER", "CONTACT"]

        print("\nStep 2: Starting Navigation...")

        for name in menu_items:
            try:
                print(f"--- Testing Menu: {name} ---")
                
                # Locator define
                menu_locator = page.locator(f"text={name}").first
                
                # special logic for CAREER
                if name == "CAREER":
                    # Adhi hover kara mhanje standing line/dropdown active hoil
                    menu_locator.hover()
                    page.wait_for_timeout(1000) # Hover dakhvnyasathi pause
                    
                    # Click now (force=True use because click intercept can be by dropdown)
                    menu_locator.click(force=True)
                else:
                    # All menus for normal click
                    menu_locator.click()
                
                page.wait_for_load_state("domcontentloaded")
                page.wait_for_timeout(2000)

                print(f"Success! Current URL: {page.url}")

            except Exception as e:
                print(f"Error: {name} failed → {e}")

        print("\nAll menu pages testing finished!")
        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run_navigation_test()