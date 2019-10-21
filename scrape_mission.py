from splinter import Browser
from bs4 import BeautifulSoup
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest//"
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #   ul > li:nth-child(1) > div > div > div.content_title > a
    listings["title"] = soup.find("div", class_="content_title").get_text()
    listings["paragraph"] = soup.find(
        "div", class_="article_teaser_body").get_text()
    browser.quit()


def scrape_image():
    browser = init_browser()
    browser.visit(url)

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    browser.click_link_by_partial_text('FULL IMAGE')
    #   #page > section.centered_text.clearfix.main_feature.primary_media_feature.single > div > div > article
    listings["image"] = soup.find(
        "div", class_="fancybox-inner").div.img['src']
    # listings["hood"] = soup.find("span", class_="result-hood").get_text()
    browser.quit()

    return listings
