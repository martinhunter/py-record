from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\lh3795\Downloads\chromedriver.exe')
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
comment = driver.find_element_by_css_selector('div.reply-content')
content = comment.find_element_by_tag_name('p')
print (content.text)
