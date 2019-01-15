from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import time 
import pymongo



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_info = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    mars_info["news_title"] = soup.find('div', class_='content_title').text
    mars_info["news_p"] = soup.find('div', class_="rollover_description_inner").text


    # JPL Mars Space Images - Featured Image

    jpl_featured_space_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_featured_space_image_url)
    time.sleep(2)

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)

    browser.click_link_by_partial_text('more info')

    html = browser.html
    soup = bs(html, "html.parser")

    featured_image_url = soup.find('img', class_="main_image")

    featured_image_url = 'https://www.jpl.nasa.gov' + featured_image_url['src']

    mars_info["mars_img"] = featured_image_url


    # Mars Weather

    mars_weather_twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_twitter_url)

    html = browser.html #doesn't work if i remove it, find out why?
    mars_twitter = bs(html, 'html.parser')
    #mars_weather = mars_twitter.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    mars_weather = mars_twitter.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()

    mars_info["mars_weather"] = mars_weather


    # Mars Facts

    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit(mars_facts_url)

    html = browser.html
    mars_facts = bs(html, 'html.parser')

    mars_facts_full_df = pd.read_html(mars_facts_url)

    mars_facts_df = pd.DataFrame(mars_facts_full_df[0])

    mars_facts_df.columns = ['Characteristic','Data']
    mars_facts_df = mars_facts_df.set_index("Characteristic")

    mars_facts_html = mars_facts_df.to_html()
    mars_facts_html = mars_facts_html.replace('\n', '')

    mars_info["mars_facts_html"] = mars_facts_html



    return mars_info
