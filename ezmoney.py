from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Set up the Chrome driver
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headlessly, without opening a browser window
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=service, options=options)

    # URL of McDonald's Investor Relations News Releases page
    url = "https://corporate.mcdonalds.com/corpmcd/our-stories/business/financial-news.html"

    # Navigate to the URL
    driver.get(url)

    # Wait for the news section to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'newsroom-card-view'))
    )

    # Wait for the content to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'cmp-news-listing__item'))
    )

    # Find the section containing news releases
    try:
        news_section = driver.find_element(By.ID, 'newsroom-card-view')
    except:
        print("Error: Could not find the news section with id 'newsroom-card-view'. Please check the website structure.")
        driver.quit()
        return

    # Extract news releases
    news_releases = news_section.find_elements(By.CLASS_NAME, 'cmp-news-listing__item')

    # Check if news releases were found
    if not news_releases:
        print("Error: Could not find any news releases in the news section.")
        driver.quit()
        return

    # Iterate over the news releases and extract the necessary information
    for release in news_releases:
        title = release.find_element(By.TAG_NAME, 'h3').text.strip()
        date = release.find_element(By.CLASS_NAME, 'cmp-newsroom__cards-tile--list-content-date').text.strip()
        try:
            read_more_link = release.find_element(By.LINK_TEXT, 'Read more')
            link = read_more_link.get_attribute('href')
        except:
            link = "No link found"

        # Print the extracted information
        print(f"Title: {title}")
        print(f"Date: {date}")
        print(f"Link: {link}")
        print('-' * 80)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
