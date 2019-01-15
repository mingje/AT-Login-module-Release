import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from appium import webdriver
import subprocess


#cmd = 'python tt9.py'
#os.system(cmd)
# Product_list = [Qfile, Qvideo, Qget, Qphoto, Qmusic, Qsirch, Qmanager, Qcontactz, QRM, DJ2, OceanKTV]
Product_flag = "Qsirch"
loop_times = 1
Device_flag = "ASUS_ZenPone3"


class session:
    def __init__(self):
        if Device_flag == "Oppo_R7sf":
            self.dc["platformVersion"] = "5.1.1"
            self.dc["deviceName"] = "7537c434"
        elif Device_flag == "Nexus_6P":
            self.dc["platformVersion"] = "8.1.0"
            self.dc["deviceName"] = "ENU7N15B09001438"
        elif Device_flag == "ASUS_ZenPone3":
            self.dc["platformVersion"] = "8.0.0"
            self.dc["deviceName"] = "GAAZCYKOR03U439"

    def setsession_Qvideo(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        #if Device_flag == "Oppo R7sf":
        #self.dc["platformVersion"] = "5.1.1"
        #self.dc["deviceName"] = "7537c434"
        self.dc["appPackage"] = "com.qnap.qvideo"
        self.dc["appActivity"] = ".Qvideo"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        #self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_Qget(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        #if Device_flag == "Oppo R7sf":
        #self.dc["platformVersion"] = "5.1.1"
        #self.dc["deviceName"] = "7537c434"
        self.dc["appPackage"] = "com.qnap.com.qgetpro"
        self.dc["appActivity"] = ".Splash"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        #self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_Qfile(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.qfile"
        self.dc["appActivity"] = "com.qnap.qfilehd.Splash"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        #self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_Qmusic(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.qmusic"
        self.dc["appActivity"] = ".InitialSplash"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        # self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_Qmail(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.qmail"
        self.dc["appActivity"] = ".InitialSplash"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        # self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_Qphoto(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.qphoto"
        self.dc["appActivity"] = ".QPhoto"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        # self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_Qcontactz(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.mobile.mycontacts"
        self.dc["appActivity"] = "com.qnap.login.naslogin.SplashActivity"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        # self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_Qmanager(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.qmanager"
        self.dc["appActivity"] = "com.qnap.qmanagerhd.login.Splash"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        # self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_Qsirch(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.qsirch"
        self.dc["appActivity"] = "com.qnap.login.naslogin.SplashActivity"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        # self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_QRM(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.mobile.qrmplus"
        self.dc["appActivity"] = "com.qnap.mobile.login.activity.SplashActivity"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        # self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_OceanKTV(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.mobile.oceanktv"
        self.dc["appActivity"] = ".oceanktv.SplashActivity"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        # self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_DJ2(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.mobile.dj2"
        self.dc["appActivity"] = ".login.naslogin.SplashActivity"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        # self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_Qsync(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["appPackage"] = "com.qnap.Qsync"
        self.dc["appActivity"] = "com.qnap.qsync.commonModule.Splash"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        # self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)


class profile:
    def __init__(self, n, lanip1, lanip2, wanip, myDDNS, cloudlink, NASport, NASport_Se, Externalport, Externalport_Se, ac, pwd):
        self.name = n
        self.NASLANIP1 = lanip1
        self.NASLANIP2 = lanip2
        self.WANIP = wanip
        self.myDDNS = myDDNS
        self.cloudlnk = cloudlink
        self.NASport = NASport
        self.NASport_Se = NASport_Se
        self.Externalport = Externalport
        self.Externalport_Se = Externalport_Se
        self.ac = ac
        self.pwd = pwd


def getWANIP(myQNAPDDNS):
    try:
        NAS = profile("", "", "", "", myQNAPDDNS,
                       "", "", "", "", "", "", "")
        Pinghost = NAS.myDDNS
        CHECK_OUTPUT1 = subprocess.check_output('ping ' + Pinghost + ' -c 2', shell=True)
        # print(CHECK_OUTPUT1)
        # print(type(CHECK_OUTPUT1))
        pingresult = str(CHECK_OUTPUT1, 'gbk')
        resultsp = pingresult.split(")", 1)
        #resultsp.split()
        resultsp1 = resultsp[0]
        resultsp2 = resultsp1.split("(", 1)
        ipget = resultsp2[1]
        return ipget
    except:
        return "127.0.0.1"

NAS1 = profile("TVS-473", "192.168.79.200", "10.20.241.197", "", "steventvs473.myqnapcloud.com",
                   "steventvs473", "9090", "448", "9090", "443", "admin", "@dmin1234")
NAS2 = profile("TVS-473", "192.168.79.200", "10.20.241.197", "115.43.107.17", "mingjehouse.myqnapcloud.com",
                   "mingjehouse", "5000", "5001", "5000", "5001", "cindy", "cindy")
China_NonDePortNAS = profile("AT-EXT-8082", "192.168.200.9", "", getWANIP("atext8082.myqnapcloud.cn"), "atext8082.myqnapcloud.cn",
                   "atext8082", "25188", "25143", "8082","8083", "admin", "80682695")

def login1(self, **kwargs):
    IP_or_Host = kwargs.get("IP_or_Host", NAS1.NASLANIP2)
    WAN_IP = kwargs.get("WAN_IP", NAS2.WANIP)
    AC = kwargs.get("AC", "admin")
    PWD = kwargs.get("PWD", NAS1.pwd)
    SSL = kwargs.get("SSL", "disable") # SSL = "disable" or "enable"
    AutoPort = kwargs.get("AutoPort", "enable") # AutoPort = "disable" or "enable"
    Connectport = kwargs.get("Connectport", "8080")
    myDDNS = kwargs.get("myDDNS", "mingjehouse")
    testMethod = kwargs.get("testMethod", "normal") # testMethod = "normal", "QNAPDDNS" or "TUTK" or "autosearch" or "QID"
    LoginResult = kwargs.get("LoginResult", 1) # LoginResult = 0(FAIL case) or 1(PASS case)
    Region = kwargs.get("Region", ".myqnapcloud.com") # Region = "myqnapcloud.com" or "myqnapcloud.cn"

    '''這是失敗的用例'''
    try:
        self.driver.find_element_by_xpath("xpath=//*[@id='qbu_tvStart']").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@class='android.widget.ImageButton']")))
        self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.ImageButton']").click()
        if Product_flag == "Qsirch" or Product_flag == "OceanKTV" or Product_flag == "DJ2":
            self.driver.find_element_by_xpath("xpath=//*[@id='manualAddServerButton']").click()
        else:
            self.driver.find_element_by_xpath("xpath=//*[@id='IDTV_MANUAL']").click()
    except NoSuchElementException:
        try:
            self.driver.find_element_by_xpath("xpath=//*[@id='btn_right']").click
        except NoSuchElementException:
            pass
    if testMethod == "QID":
        while True:
            stopflag = 0
            if Product_flag == "Qfile":
                el = self.driver.find_elements_by_id(id_='textview_servername')
            else:
                el = self.driver.find_elements_by_id(id_='IDTV_SERVER_NAME')
            for i in el:
                if i.text == IP_or_Host:
                    i.click()
                    stopflag = 1
                    break
                else:
                    pass
            if stopflag == 1:
                break
            else:
                self.driver.swipe(669, 1100, 672, 300, 503)
        self.driver.find_element_by_xpath("xpath=//*[@id='editText_username']").send_keys(AC)
        self.driver.find_element_by_xpath("xpath=//*[@id='editText_userpassword']").send_keys(PWD)
        if Product_flag == "Qmusic":
            self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
        else:
            self.driver.find_element_by_xpath("xpath=//*[@id='btn_ok']").click()


    else:
        if Product_flag == "OceanKTV":
            try:
                self.driver.find_element_by_id(id_='img_nas_user').click()
            except:
                pass
        else:
            pass
        self.driver.find_element_by_xpath("xpath=//*[@id='addServer']").click()

        if testMethod == "autosearch":
            stopflag = 0
            j = 0
            while True:
                if j > 1:
                    flag = 1
                    assert flag == 0, "UDP Search FAIL"
                elif j <= 1:
                    if stopflag == 1:
                        break
                    else:
                        self.driver.find_element_by_id(id_='qbu_action_refresh').click()
                        time.sleep(5)
                        lastL = ""
                        while True:
                            el = self.driver.find_elements_by_id(id_='IDTV_SERVER_NAME')
                            if lastL == el[-1].text:
                                break
                            else:
                                for i in el:
                                    if i.text == IP_or_Host:
                                        i.click()
                                        stopflag = 1
                                        break
                                lastL = el[-1].text
                            if stopflag == 1:
                                break
                            else:
                                self.driver.swipe(669, 1100, 672, 300, 503)
                j = j + 1

        else:
            print("error")
            if Product_flag == "Qsirch" or Product_flag == "OceanKTV" or Product_flag == "DJ2":
                self.driver.find_element_by_xpath("xpath=//*[@id='manualAddServerButton']").click()
            else:
                self.driver.find_element_by_xpath("xpath=//*[@id='IDTV_MANUAL']").click()
        #輸入Host欄位
        if testMethod == "autosearch":
            pass
        else:
            self.driver.find_element_by_xpath("xpath=//*[@id='server_host_edit']").send_keys(IP_or_Host)
        #輸入帳號密碼
        if Product_flag == "DJ2":
            self.driver.find_element_by_id(id_='nas_login_button').click()
            self.driver.find_element_by_xpath("xpath=//*[@id='editText']").send_keys(AC)
            WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='editText_two']")))
            self.driver.find_element_by_xpath("xpath=//*[@id='editText_two']").send_keys(PWD)
            self.driver.find_element_by_id(id_='button1').click()

        else:
            self.driver.find_element_by_xpath("xpath=//*[@id='user_name_edit']").send_keys(AC)
            WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='user_password_edit']")))
            self.driver.find_element_by_xpath("xpath=//*[@id='user_password_edit']").send_keys(PWD)
        #SSL 選項
        if SSL == "disable":
            pass
        else:
            self.driver.find_element_by_xpath("//*[@id='textView_SSL']").click()
        #AutoDetectPort選項
        if AutoPort == "enable":
            pass
        else:
            self.driver.find_element_by_xpath("xpath=//*[@id='button_goto_advanced']").click()
            self.driver.swipe(669, 748, 672, 563, 503)
            self.driver.swipe(621, 603, 615, 324, 352)
            self.driver.find_element_by_xpath("xpath=//*[@id='textView_AutoPort']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("xpath=//*[@id='port_simple']").send_keys(Connectport)
        #點擊SVAE button
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@class='android.support.v7.widget.LinearLayoutCompat']")))
        self.driver.find_element_by_xpath("xpath=//*[@class='android.support.v7.widget.LinearLayoutCompat']").click()
    try:
        print("SSL confirmed")
        WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='button1']")))
        self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
        WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='button1']")))
        self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
    except:
        pass

    if LoginResult == 0:
        print("Failcase")
        WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='alertTitle']")))
        flag1 = self.driver.find_element_by_xpath("//*[@id='alertTitle']").text
        print(flag1)
        flag = 1
        assert flag == 1
    else:
        if testMethod == "TUTK":
            if Product_flag == "Qvideo":
                try:
                    WebDriverWait(self.driver, 30).until(
                        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='button1']")))
                    self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
                except:
                    WebDriverWait(self.driver, 5).until(
                        expected_conditions.presence_of_element_located((By.XPATH, "//*[@class='android.widget.ImageButton']")))
            else:
                WebDriverWait(self.driver, 30).until(
                    expected_conditions.presence_of_element_located((By.XPATH, "//*[@class='android.widget.ImageButton']")))
        else:
            print("normal enter case")
            if Product_flag == "Qmanager":
                try:
                    WebDriverWait(self.driver, 15).until(
                        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='button1']")))
                    self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
                except:
                    pass
            elif Product_flag == "OceanKTV":
                WebDriverWait(self.driver, 30).until(
                    expected_conditions.presence_of_element_located((By.ID, "img_start_singing")))
                self.driver.find_element_by_id(id_='img_start_singing').click()
                self.driver.find_element_by_id(id_='button1').click()
            elif Product_flag == "Qsync":
                WebDriverWait(self.driver, 30).until(
                    expected_conditions.presence_of_element_located((By.ID, "ItemTitle")))
                SyncFolderList = self.driver.find_elements_by_id(id_='ItemTitle')
                SyncFolderList[0].click()
                self.driver.find_element_by_id(id_='action_done').click()
        # 找到左上角主選單開啟後判斷登入方式
        WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//*[@class='android.widget.ImageButton']")))

        ImagebuttonList = self.driver.find_elements_by_xpath("xpath=//*[@class='android.widget.ImageButton']")
        ImagebuttonList[0].click()
        if Product_flag == "Qcontactz":
            self.driver.find_element_by_xpath("//*[@id='txt_header_ip']")
            flag = self.driver.find_element_by_xpath("//*[@id='txt_header_ip']").text
        elif Product_flag == "Qsirch":
            self.driver.find_element_by_xpath("//*[@id='ip']")
            flag = self.driver.find_element_by_xpath("//*[@id='ip']").text
        elif Product_flag == "QRM":
            self.driver.find_element_by_xpath("//*[@id='header_server_ip']")
            flag = self.driver.find_element_by_xpath("//*[@id='header_server_ip']").text
        elif Product_flag == "OceanKTV":
            self.driver.find_element_by_xpath("//*[@id='txt_user_nas_ip1']")
            flag = self.driver.find_element_by_xpath("//*[@id='txt_user_nas_ip1']").text
        elif Product_flag == "DJ2":
            self.driver.find_element_by_xpath("//*[@id='nas_ip']")
            flag = self.driver.find_element_by_xpath("//*[@id='nas_ip']").text
        else:
            self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']")
            flag = self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']").text
        if testMethod == "normal":
            print(flag)
            assert flag == IP_or_Host, "error"
        elif testMethod == "QNAPDDNS":
            print(flag)
            assert flag == IP_or_Host or flag == WAN_IP or flag == myDDNS + ".myqnapcloud.com" or flag == myDDNS + ".myqnapcloud.cn"
        elif testMethod == "TUTK":
            print(flag)
            assert flag == "CloudLink"
        elif testMethod == "autosearch" or testMethod == "QID":
            assert flag == NAS1.NASLANIP1 or flag == NAS1.NASLANIP2 or flag == WAN_IP or flag == myDDNS + ".myqnapcloud.com" \
                   or flag == myDDNS + ".myqnapcloud.cn"








def Regionset(self, Region):
    #driver.find_element_by_xpath("xpath=//*[@id='btn_right']").click()
    time.sleep(3)
    if Product_flag == "OceanKTV":
        try:
            self.driver.find_element_by_id(id_='img_nas_user').click()
        except:
            pass
    elif Product_flag == "Qsirch":
        self.driver.find_element_by_xpath("//*[@class='android.widget.ImageButton']").click()
        time.sleep(2)
    else:
        pass

    if Product_flag == "Qsirch":
        llist = self.driver.find_elements_by_xpath(
            "//android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.ExpandableListView/android.widget.RelativeLayout")
        print(llist)
        llist[2].click()
    else:
        self.driver.find_element_by_xpath("xpath=//*[@id='setting' or @id='settings']").click()

    if Product_flag == "Qvideo" or Product_flag == "Qmusic":
        while True:
            stopflag = 0
            try:
                self.driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout' and @index='8']").click()
                stopflag = 1
            except:
                self.driver.swipe(669, 800, 672, 500, 503)
            if stopflag == 1:
                break
    elif Product_flag == "Qget" or Product_flag == "Qfile" or Product_flag == "Qmanager" or Product_flag == "Qmail":
        while True:
            stopflag = 0
            try:
                self.driver.find_element_by_xpath("//*[@id='region_setting']").click()
                stopflag = 1
            except:
                self.driver.swipe(669, 800, 672, 500, 503)
            if stopflag == 1:
                break
    elif Product_flag == "Qsirch":
        self.driver.swipe(669, 800, 672, 500, 503)
        self.driver.swipe(669, 800, 672, 500, 503)

        self.driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout' and @index='9']").click()
    elif Product_flag == "Qphoto":
        self.driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout' and @index='11']").click()
    elif Product_flag == "Qcontactz" or Product_flag == "OceanKTV":
        self.driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout' and @index='3']").click()
    elif Product_flag == "QRM" or Product_flag == "DJ2":
        self.driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout' and @index='7']").click()
        
    self.driver.find_element_by_xpath("xpath=//*[@id='region_name' or @id='region_text' or @id='txt_region_subtitle']").click()
    if Region == "Globalset":
        if Product_flag == "QRM" or Product_flag == "Qsirch":
            try:
                self.driver.find_element_by_xpath("xpath=//*[@id='radio_global'][@index='0'][@checked='true']")
                self.driver.find_element_by_xpath("xpath=//*[@id='button2']").click()
            except:
                self.driver.find_element_by_xpath("xpath=//*[@id='radio_global' and @index='0']").click()
        else:
            try:
                self.driver.find_element_by_xpath("xpath=//*[@id='text1'][@index='0'][@checked='true']")
                self.driver.find_element_by_xpath("xpath=//*[@id='button2']").click()
            except:
                self.driver.find_element_by_xpath("xpath=//*[@id='text1' and @index='0']").click()
    elif Region == "Chinaset":
        if Product_flag == "QRM" or Product_flag == "Qsirch":
            try:
                self.driver.find_element_by_xpath("xpath=//*[@id='radio_china'][@index='1'][@checked='true']")
                self.driver.find_element_by_xpath("xpath=//*[@id='button2']").click()
            except:
                self.driver.find_element_by_xpath("xpath=//*[@id='radio_china' and @index='1']").click()
        else:
            try:
                self.driver.find_element_by_xpath("xpath=//*[@id='text1'][@index='1'][@checked='true']")
                self.driver.find_element_by_xpath("xpath=//*[@id='button2']").click()
            except:
                self.driver.find_element_by_xpath("xpath=//*[@id='text1' and @index='1']").click()

    try:
        self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
    except:
        pass

    self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.ImageButton']").click()
    time.sleep(2)
    self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.ImageButton']").click()

def QIDLogin(self, QIDAC, QIDPWD):
    time.sleep(3)
    self.driver.find_element_by_xpath("xpath=//*[@id='setting']").click()
    while True:
        stopflag = 0
        try:
            self.driver.find_element_by_xpath("//*[@id='img_lly']").click()
            stopflag = 1
        except:
            self.driver.swipe(669, 800, 672, 500, 503)
        if stopflag == 1:
            break
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='svg-qnap-id']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='qid']").send_keys(QIDAC)
    self.driver.find_element_by_xpath("xpath=//*[@id='password']").send_keys(QIDPWD)
    self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.Button']").click()
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='button1']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
    self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.ImageButton']").click()



def QIDLogout(self, QIDshowID):
    time.sleep(3)
    self.driver.find_element_by_xpath("xpath=//*[@id='setting']").click()
    if Product_flag == "Qget" or Product_flag == "Qfile" or Product_flag == "Qmusic" or Product_flag == "Qmanager" or \
            Product_flag == "Qsync" or Product_flag == "Qmail":
        while True:
            stopflag = 0
            try:
                el = self.driver.find_elements_by_id(id_='qid_account_info')
                print(el)
                for i in el:
                    if i.text == QIDshowID:
                        i.click()
                        stopflag = 1
                        break
                    else:
                        pass
            except:
                self.driver.swipe(669, 1100, 672, 300, 503)
            if stopflag == 1:
                break
            else:
                self.driver.swipe(669, 1100, 672, 300, 503)
    if Product_flag == "Qvideo" or Product_flag == "Qphoto":
        while True:
            stopflag = 0
            el = self.driver.find_elements_by_id(id_='title')
            print(el)
            for i in el:
                if i.text == QIDshowID:
                    i.click()
                    stopflag = 1
                    break
                else:
                    pass
            if stopflag == 1:
                break
            else:
                self.driver.swipe(669, 1100, 672, 300, 503)

    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='action_logout']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='action_logout']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='button_DeleteDevice']").click()
    self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.ImageButton']").click()






