from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from pynput.keyboard import Key, Controller




#------------------  General Variables  ------------------#



email = "your_email@example.com"              # Replace with your email address
password = "your_password"                    # Replace with your password
title_of_ad = "Your Ad Title"                 # Replace with the title of your ad
price_of_room = "price"                       # Replace with the price (numbers only, ex. "750")
telephone_number = "number"                   # Replace with your phone number (numbers only, ex. "4164390000")
file_path = r"path_to_images_folder"          # Replace with the folder path containing your images (ex. r"C:\Users\name\ad_pics")
ad_content_path = r"path_to_ad_content_file"  # Replace with the path to the ad content file (ex. r"C:\Users\name\ad_pics\description.txt")


#====================  ALL FUNCTIONS  ====================#



#--------------------  Delete Old Ad  --------------------#


def delete_ad():
    '''If you have an existing ad, delete it first, as 
    Kijiji's algorithm detects duplicate ads and penalizes 
    repeated content'''

    # delete ad
    delete_path = '/html/body/div[3]/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/button'
    delete = driver.find_element(By.XPATH, delete_path)
    delete.click()

    time.sleep(1)

    # reason for deleting
    option_d = 'Prefer not to say'
    reason = driver.find_element(By.XPATH, f"//button[text()='{option_d}']")
    reason.click()

    time.sleep(1)

    # confirm deleting
    delete_my_ad_path = '//*[@id="modalOverlay"]/div/div/div/div[2]/div[2]/button' 
    delete_my_ad = driver.find_element(By.XPATH, delete_my_ad_path) 
    delete_my_ad.click()

    time.sleep(1.5)


#-------------   Post-Ad Button Functions   --------------#


def post_ad():
    '''This function is used if you do not have an 
    ad to delete; instead, it clicks on the "Post ad"
    button from the "My Ads" page'''
    post_ad_path = '//*[@id="MainContainer"]/div[1]/div/div/div/header/div[3]/div/div[3]/div/a'
    post_ad = driver.find_element(By.XPATH, post_ad_path)
    post_ad.click()



def post_another_ad():
    '''This function is used if you have an ad to delete.
    The button "Post another ad" is visible after you delete
    your ad.'''
    post_another_ad_path = '//*[@id="browseKijiji"]'
    post_another_ad = driver.find_element(By.XPATH, post_another_ad_path)
    post_another_ad.click()
    time.sleep(2)


#-------------------  Post Ad Process  -------------------#


def post_ad_continued():
    '''Process for posting the entire ad'''

    # write the title
    ad_title = driver.find_element(By.ID, "AdTitleForm")
    ad_title.send_keys(title_of_ad)

    time.sleep(1)

    # click on next
    next_button_path = '//*[@id="mainPageContent"]/div/div/div/div[2]/div/div/div[2]/div[1]/div/button'
    next_button = driver.find_element(By.XPATH, next_button_path)
    next_button.click()

    time.sleep(2)

    # click on real estate
    real_estate_button_path = '//*[@id="CategorySuggestion"]/div/ul/li[3]/button'
    real_estate = driver.find_element(By.XPATH, real_estate_button_path)
    real_estate.click()

    time.sleep(1)

    # click on for rent
    for_rent_path = '//*[@id="CategorySuggestion"]/div/ul[2]/li[1]/button'
    for_rent = driver.find_element(By.XPATH, for_rent_path)
    for_rent.click()

    time.sleep(1)

    # click on room rentals & roommates
    room_rentals_roommates_path = '//*[@id="CategorySuggestion"]/div/ul[2]/li[3]/button'
    room_rentals_roommates = driver.find_element(By.XPATH, room_rentals_roommates_path)
    room_rentals_roommates.click()

    time.sleep(2.5)

    # 'offering' button
    i_am_offering_path = '/html/body/div[3]/div[3]/main/form/div/div[3]/ul/li[2]/div/label[1]/label'
    i_am_offering = driver.find_element(By.XPATH, i_am_offering_path)
    i_am_offering.click()

    # 'furnished' button
    furnished_path = '//*[@id="MainForm"]/div[3]/ul/li[3]/div/div[1]/label[1]/label'
    furnished = driver.find_element(By.XPATH, furnished_path)
    furnished.click()

    # 'pet friendly' button
    pet_friendly_path = '//*[@id="MainForm"]/div[3]/ul/li[4]/div/div[1]/label[2]/label'
    pet_friendly = driver.find_element(By.XPATH, pet_friendly_path)
    pet_friendly.click()

    # write the description
    description_path = '//*[@id="pstad-descrptn"]'
    description = driver.find_element(By.XPATH, description_path)


    with open(ad_content_path, "r") as Room_ad:
        for line in Room_ad:
            description.send_keys(line)


    # upload images

    time.sleep(1)

    select_images_path = '//*[@id="ImageUploadButton"]'
    select_images = driver.find_element(By.XPATH, select_images_path)
    select_images.click()
    keyboard = Controller()

    time.sleep(3)

    keyboard.type(file_path)

    time.sleep(0.5)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter) 

    time.sleep(1)

    keyboard.type("")

    time.sleep(1)

    # I labelled my pictures 'a', 'b', ..., 'i' for simplicity
    string = '"a" "b" "c" "d" "e" "f" "g" "h" "i" "j"'
    keyboard.type(string)

    time.sleep(3)

    keyboard.press(Key.enter)

    time.sleep(0.5)

    keyboard.release(Key.enter) 

    time.sleep(10)

    # price of room
    price_path = '//*[@id="PriceAmount"]'
    price = driver.find_element(By.XPATH, price_path)
    price.send_keys(price_of_room)

    time.sleep(0.5)

    # telephone number
    telephone_path = '//*[@id="PhoneNumber"]'
    telephone = driver.find_element(By.XPATH, telephone_path)
    telephone.send_keys(telephone_number)

    time.sleep(0.5)

    # $0.00 cost
    free_cost_path = '//*[@id="MainForm"]/div[10]/div/div/div/div[1]/div[1]/div[2]/div[2]/button'
    free_cost = driver.find_element(By.XPATH, free_cost_path)
    free_cost.click()

    time.sleep(1)

    # checkout and post ad
    checkout_and_post_ad_path = '//*[@id="MainForm"]/div[14]/div/div/button[1]'
    checkout_and_post_ad = driver.find_element(By.XPATH, checkout_and_post_ad_path)
    checkout_and_post_ad.click()

    time.sleep(5)



#====================  END OF SECTION  ===================#



#-------------------- Login to Kijiji --------------------#


options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# go to kijji
url = "https://www.kijiji.ca"
driver.get(url)
sign_in = driver.find_element(By.XPATH, '//*[@data-testid="header-sign-in"]')
sign_in.click()

time.sleep(3.5)

# login information
username = driver.find_element(By.ID, "username")
username.send_keys(email)

password = driver.find_element(By.ID, "password")
password.send_keys(password)

sign_in = driver.find_element(By.ID, "login-submit")
driver.execute_script("arguments[0].click();", sign_in)

time.sleep(1)

# click on dropdown
dropdown = driver.find_element(By.CSS_SELECTOR, '[aria-label="My Account"]')
dropdown.click()

# click on account
my_ads_path = '/html/body/div[1]/div/div/div[1]/header/div/div[1]/div[3]/div[2]/div/ul/li[1]/a'
my_ads = driver.find_element(By.XPATH, my_ads_path)
my_ads.click()

time.sleep(2)

# find row of ad  
ad_table = driver.find_element(By.XPATH, '//table[contains(@class, "myAdsTable-3260305338 hideActionColumn-2062048758")]')
rows = ad_table.find_elements(By.TAG_NAME, "tr")

# this is the column on the kijiji ad page which houses the titles of ads
title = 2
title_list = []


def func(rows):
    for row in rows:
        columns = row.find_elements(by=By.TAG_NAME, value='td')
        for index, col in enumerate(columns):

            if index == title:
                title_list.append(col.text)

            if title_of_ad == col.text:
                return row
    
row = func(rows)


if title_of_ad in title_list:
    link_element = row.find_element(By.TAG_NAME, 'a')
    link_element.click()
    delete_ad()
    post_another_ad()

else:
    time.sleep(1)
    post_ad()



post_ad_continued()



driver.quit()