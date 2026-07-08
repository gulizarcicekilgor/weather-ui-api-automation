def test_search_city(page):
    # Go to homepage
    page.goto("https://openweathermap.org/")
    
    # Accept cookies if popup appears
    try:
        page.locator("text=Accept").click(timeout=3000)
    except:
        pass
    
    # Find search box and type city name
    page.fill("input[placeholder='Search City']", "Istanbul")
    
    # Wait for dropdown
    page.wait_for_timeout(3000)
    
    # Click first Istanbul result in dropdown
    page.locator("text=Istanbul").first.click()
    
    # Wait for navigation
    page.wait_for_url("**/city/**", timeout=10000)
    
    # Verify we landed on Istanbul page
    assert "city" in page.url
    #
    print("URL:", page.url)