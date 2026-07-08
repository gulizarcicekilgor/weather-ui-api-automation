def test_homepage_loads(page):
    page.goto("https://openweathermap.org/")
    assert page.title() !=""    #→ Sayfanın başlığı boş değilse test geçer. assert = "bu doğru olmalı" demek.
    print("Page title: ", page.title())

    