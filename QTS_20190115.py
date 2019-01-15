import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

from appium import webdriver


from selenium import webdriver
driver = webdriver.Chrome("/Users/stevenhsu/PycharmProjects/untitled/chromedriver")

driver.get("https://192.168.79.200:448")
driver.refresh()
time.sleep(5)
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "button")))
driver.find_element_by_tag_name("button").click()
time.sleep(2)

WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "username")))
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("pwd").send_keys("@dmin1234")
driver.find_element_by_id("submit").click()
time.sleep(2)
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='lostPhone']")))
#driver.find_element_by_xpath("/html/body/div[4]/div[7]/div[1]/div[1]/form/div[2]/span").click
driver.find_element_by_xpath("//*[@id='lostPhone']").click()
driver.find_element_by_id("scyAns").send_keys("admin")
driver.find_element_by_id("scyAnsSubmit").click()
x = 0
while True:
    if x == 3:
        break
    else:
        try:
            print("1")
            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                ((By.XPATH,
                "//body[div/@class='x-window app-dlg q-msg-win q-window show-header-line x-window-noborder x-window-plain q-modal-window']")))
            bu = driver.find_elements_by_css_selector("table>tbody>tr>td>em>button.x-btn-text")
            bu[-1].click()
            break
        except:
            pass
        try:
            print("2")
            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.id, "ext-gen124")))
            break
        except:
            pass

    x = x + 1


driver.find_element_by_id("ext-gen124").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='ext-comp-1100']/li[2]/img").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='cp_dv_block_0']/div[1]/div[1]/div[1]/img").click()
time.sleep(5)
lis1 = driver.find_elements_by_css_selector("li.qts-tab")

lis1[4].click()
time.sleep(2)

driver.find_element_by_xpath("//input[@name='region']").click()
time.sleep(2)
list1 = driver.find_elements_by_css_selector("div.x-combo-list-item")
print(list1)
list1[1].click()
driver.find_element_by_id("bb-apply-general").click()
clo1 = driver.find_elements_by_css_selector("span.close-icon")
clo1[0].click()
time.sleep(3)

time.sleep(2)
driver.find_element_by_id("ext-gen124").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='ext-comp-1100']/li[2]/img").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='cp_dv_block_0']/div[1]/div[1]/div[1]/img").click()
time.sleep(2)
checkList = driver.find_elements_by_css_selector("input.x-form-checkbox.x-form-field")
che = checkList[2].is_selected()
checkbox = driver.find_elements_by_css_selector("span.checkbox-img")
checlick = checkbox[2]
if che == True:
    print("selected")
else:
    time.sleep(2)
    checlick.click()
    driver.find_element_by_id("bb-apply-general").click()
    WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.ID, "bb-msg-general")))

clo = driver.find_elements_by_css_selector("div.x-tool.x-tool-icon.x-tool-close")
clo[0].click()
time.sleep(3)


time.sleep(2)
driver.find_element_by_id("ext-gen124").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='ext-comp-1100']/li[6]/img").click()
y = 0
while True:
    if y == 18:
        break
    else:
        try:
            print("find1")
            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                ((By.XPATH,
                "//body[div/@class='x-window utility-window win-form q-window show-header-line x-window-noborder x-window-plain q-modal-window']")))
            print("ok")
            clo2 = driver.find_elements_by_css_selector("div.x-tool.x-tool-icon.x-tool-close")
            clo2[2].click()
            time.sleep(3)
            break
        except:
            pass

        try:
            print("find2")
            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                        ((By.XPATH, "//*[@id='mcn_center_region_logo']/img")))
            break
        except:
            pass
    y = y + 1
lis = driver.find_elements_by_css_selector("div.x-tree-node-el.x-tree-node-leaf.x-unselectable")
print(lis)
lis[5].click()
z = 0
while True:
    if z == 18:
        break
    else:
        try:
            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                ((By.XPATH, "//div[img/@src='/cgi-bin/apps/myCloudNas/images/ac/logo_access_control_top.jpg']")))
            time.sleep(3)
            break
        except:
            pass
    z = z + 1

driver.find_element_by_css_selector("div.x-form-field-wrap.x-form-field-trigger-wrap.x-box-item").click()
time.sleep(2)
list = driver.find_elements_by_css_selector("div.x-combo-list-item")
print(list)
list[1].click()
driver.find_element_by_id("access_control_apply_button").click()
time.sleep(5)

clo3 = driver.find_elements_by_css_selector("span.close-icon")
print(clo3)
clo3[0].click()



