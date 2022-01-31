from selenium import webdriver
import selenium
url = "https://www.youtube.com/c/JomaOppa/videos"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('chromedriver', options=options)
driver.get(url)
button = driver.find_elements_by_xpath('.//button[@class = "VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc IIdkle"]')
print(button)
button[1].click()

videos = driver.find_elements_by_xpath('.//a[@class="yt-simple-endpoint style-scope ytd-grid-video-renderer"]')

for video in videos:
    link = video.get_attribute("href")
    title = video.get_attribute("title")
    
    #print(dir(link))
    label = video.get_attribute("aria-label").replace(title, "").replace("by Joma Tech", "").replace(" ", "")

    time = label[0]
    length = label[1]
    if int(time) <= 5 and length == "d":
        print(f"Link: {link} Title: {title}")
        
