from selenium import webdriver
import os
import urllib.request
import time

path = r'D:\ML\Hackerearth Age Group Classification\chromedriver.exe'

url_prefix = "https://www.google.com.sg/search?q="
url_postfix = "&source=lnms&tbm=isch&sa=X&ei=0eZEVbj3IJG5uATalICQAQ&ved=0CAcQ_AUoAQ&biw=939&bih=591"

save_folder = 'train'

def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    n_images = 2000
    categories = ["adults", "teenagers", "toddlers"]
    download_images(topics[2])
    
def download_images(category):
    topic = input("What do you want to search for? ")
    category = input("for which category")
    # n_images = int(input('How many images do you want? '))
    n_images = 2000
    # topic = category + " hanging out"
    
    search_url = url_prefix+topic+url_postfix
    # print(search_url)
    # search_url = "https://www.google.co.in/search?q=bunch+of+toddlers&tbm=isch&chips=q:bunch+of+kids,g_1:group:4nPXelHWcNE%3D&hl=en&sa=X&ved=2ahUKEwjXk-vT47brAhXQeX0KHTS7BmcQ4lYoB3oECAEQHg&biw=1349&bih=625"
    
    path = r'C:\Program Files (x86)\chromedriver.exe'
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="C:\\Users\\Prithviraj\\Downloads\\chromedriver.exe", options=options)
    driver.get(search_url)
    
    value = 0
    for i in range(20):
        driver.execute_script("scrollBy("+ str(value) +",+1000);")
        value += 1000
        time.sleep(1)
    
    elem1 = driver.find_element_by_id('islrg')
    sub = elem1.find_elements_by_tag_name('img')
    
    count = 0
    for j,i in enumerate(sub):
        if j < n_images:
            src = i.get_attribute('src')                         
            try:
                if src != None:
                    src  = str(src)
                    count = count + 1
                    if(count%10 ==0):
                    	print(count)
                    
                    urllib.request.urlretrieve(src, os.path.join(save_folder + '\\' + category, str(count) + '.jpg'))
                else:
                    raise TypeError
            except Exception as e:            #catches type error along with other errors
                print(e)
                print('fail')
                break
    
    driver.close()
    
if __name__ == "__main__":
    main()