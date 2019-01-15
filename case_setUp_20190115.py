#獨立測試案例, 每個def 都是一個獨立的案例需要重新建立session
import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from BeautifulReport import BeautifulReport
from settings import session
import settings
from xmlrunner import xmlrunner


current_path = os.getcwd()
report = os.path.join(current_path, "Report")
now = time.strftime("%Y-%m-%d~%H:%M:%S", time.localtime(time.time()))

report_title = settings.Product_flag + "_" + now + ".html"
des = "獨立測試案例"

#product_list = ["Qvideo","Qget"]
#loop_times = 1
#Product_flag = "Qget"

class Login(unittest.TestCase):
    #@classmethod
    def setUp(self):
        print("start")

        if settings.Product_flag == "Qvideo":
            session.setsession_Qvideo(self)
        elif settings.Product_flag == "Qget":
            session.setsession_Qget(self)
        elif settings.Product_flag == "Qfile":
            session.setsession_Qfile(self)
        elif settings.Product_flag == "Qmusic":
            session.setsession_Qmusic(self)
        elif settings.Product_flag == "Qmail":
            session.setsession_Qmail(self)
        elif settings.Product_flag == "Qphoto":
            session.setsession_Qphoto(self)
        elif settings.Product_flag == "Qcontactz":
            session.setsession_Qcontactz(self)
        elif settings.Product_flag == "Qmanager":
            session.setsession_Qmanager(self)
        elif settings.Product_flag == "Qsirch":
            session.setsession_Qsirch(self)
        elif settings.Product_flag == "QRM":
            session.setsession_QRM(self)
        elif settings.Product_flag == "OceanKTV":
            session.setsession_OceanKTV(self)
        elif settings.Product_flag == "DJ2":
            session.setsession_DJ2(self)
        elif settings.Product_flag == "Qsync":
            session.setsession_Qsync(self)

    def test_ss(self):
        print("abcd")
    def test_dd(self):
        print("test1")
    """
    def test_QID(self):
        settings.login1(self, IP_or_Host="Steven-TVS47", AC="admin", PWD="@dmin1234", testMethod = "autosearch")

    """

    # LANIP_Client: Global, Default 8080/443 port; NAS: Global, Private/Public, SSL ON/OFF
    """
        # LANIP + 8080/443 登入 8080/443 NAS: Login success
    def test_GLLANIPdePort_GLdePortSSLOFF_login(self):
        '''LAN login -> Login PASS'''
        settings.login1(self, IP_or_Host="192.168.79.199", AC="admin", PWD="@dmin1234")

    @unittest.skipIf(settings.Product_flag == "Qcontactz" or settings.Product_flag == "Qsirch", "Not support this case")
    def test_GLLANIPdePort_GLdePortSSLON_login(self):
        '''LAN login -> Login PASS'''
        settings.login1(self, IP_or_Host = "192.168.79.199", AC="admin", PWD="@dmin1234")

    def test_GLLANIPdePortEnSSL_GLdePortSSLON_login(self):
        '''LAN login -> Login PASS'''
        settings.login1(self, IP_or_Host = "192.168.79.199", AC="admin", PWD="@dmin1234", SSL="enable")
    """
    """
        # LANIP + 8080/443 登入非8080/443 NAS: Login FAIL

    def test_GLLANIPdePort_GLNondePortSSLOFF_login(self):
        '''LAN login -> Login FAIL'''
        settings.login1(self, IP_or_Host="10.20.241.197", AC="admin", PWD="@dmin1234", LoginResult=0)

    @unittest.skipIf(settings.Product_flag == "Qcontactz", "Not support this case")
    def test_GLLANIPdePort_GLNondePortSSLON_login(self):
        '''LAN login -> Login FAIL'''
        settings.login1(self, IP_or_Host="10.20.241.197", AC="admin", PWD="@dmin1234", LoginResult=0)
    """

    """
        # LANIP + 手動輸入正確的Port 登入非8080/443 NAS: Login success
    def test_GLLANIPManualPortEnSSL_GLNondePortSSLON_login(self):
        '''LAN login -> Login PASS'''
        settings.login1(self, IP_or_Host="10.20.241.197", AC="admin", PWD="@dmin1234", SSL="enable",
                        AutoPort= "disable", Connectport="448")

    def test_GLLANIPManualPort_GLNondePortSSLOFF_login(self):
        '''LAN login -> Login PASS'''
        settings.login1(self, IP_or_Host="10.20.241.197", AC="admin", PWD="@dmin1234",
                        AutoPort="disable", Connectport="9090")
    """

    # LANIP_Client: China, Default 5000/5001 port; NAS: Global, Private/Public, SSL ON/OFF
    """
        # LANIP + 5000/5001 登入 8080/443 NAS->會自動try 5000/5001 Port: Login success
    def test_CHLANIPdePort_GLdePortSSLOFF_login(self):
        '''LAN login -> Login PASS'''
        settings.login1(self, IP_or_Host="192.168.79.199", AC="admin", PWD="@dmin1234")
    
    def test_CHLANIPdePort_GLdePortSSLON_login(self):
        '''LAN login -> Login PASS'''
        settings.login1(self, IP_or_Host="192.168.79.199", AC="admin", PWD="@dmin1234")
    
    def test_CHLANIPdePortEnSSL_GLdePortSSLON_login(self):
        '''LAN login -> Login PASS'''
        settings.login1(self, IP_or_Host="192.168.79.199", AC="admin", PWD="@dmin1234", SSL="enable")
        
        # LANIP + 5000/5001 登入非 8080/443 NAS: Login FAIL
    def test_CHLANIPdePort_GLNondePortSSLOFF_login(self):
        '''LAN login -> Login FAIL'''
        settings.login1(self, IP_or_Host="10.20.241.197", AC="admin", PWD="@dmin1234", LoginResult=0)
    
    def test_CHLANIPdePort_GLNondePortSSLON_login(self):
        '''LAN login -> Login FAIL'''
        settings.login1(self, IP_or_Host="10.20.241.197", AC="admin", PWD="@dmin1234", LoginResult=0)
        
        # LANIP + 手動輸入正確的Port 登入非8080/443 NAS: Login success
    def test_CHLANIPManualPortEnSSL_GLNondePortSSLON_login(self):
        '''LAN login -> Login PASS'''
        settings.login1(self, IP_or_Host="10.20.241.197", AC="admin", PWD="@dmin1234", SSL="enable",
                        AutoPort="disable", Connectport="448")
    
    def test_CHLANIPManualPort_GLNondePortSSLOFF_login(self):
        '''LAN login -> Login PASS'''
        settings.login1(self, IP_or_Host="10.20.241.197", AC="admin", PWD="@dmin1234",
                        AutoPort="disable", Connectport="9090")
    """
    # CloudLink_Client: Global, Default 8080/443 port; NAS: Global, Private, SSL ON/OFF
    """
        # CloudLink + 8080/443 登入NAS -> Private 拿不到Vlink Port: Login FAIL
    def test_GLcloudlinkdePort_GLPrivateSSLON_login(self):
        '''Cloudlink login -> Login FAIL'''
        settings.login1(self, IP_or_Host = settings.NAS1.cloudlnk, AC="admin", PWD="@dmin1234", testMethod = "TUTK", LoginResult=0)
    
    def test_GLcloudlinkdePort_GLPrivateSSLOFF_login(self):
        '''Cloudlink login -> Login FAIL'''
        settings.login1(self, IP_or_Host = settings.NAS1.cloudlnk, AC="admin", PWD="@dmin1234", testMethod = "TUTK", LoginResult=0)
    """
    # CloudLink_Client: Global, Default 8080/443 port; NAS: Global, Public, SSL ON/OFF
        # CloudLink + 8080/443 登入NAS -> Public 拿到Vlink Port: Login PASS
    """
    @unittest.skipIf(settings.Product_flag == "Qcontactz", "Not support this case")
    def test_GLcloudlinkdePort_GLPublicSSLON_login(self):
        '''Cloudlink login -> Login PASS'''
        settings.login1(self, IP_or_Host=settings.NAS1.cloudlnk, AC="admin", PWD="@dmin1234", testMethod="TUTK")

    def test_GLcloudlinkdePortEnSSL_GLPublicSSLON_login(self):
        '''Cloudlink login -> Login PASS'''
        settings.login1(self, IP_or_Host=settings.NAS1.cloudlnk, AC="admin", PWD="@dmin1234", SSL="enable", testMethod="TUTK")
    
    def test_GLcloudlinkdePort_GLPublicSSLOFF_login(self):
        '''Cloudlink login -> Login PASS'''
        settings.login1(self, IP_or_Host=settings.NAS1.cloudlnk, AC="admin", PWD="@dmin1234", testMethod="TUTK")
    """

    # CloudLink_Client: China, Default 5000/5001 port; NAS: Global, Private, SSL ON/OFF

        # CloudLink + 5000/5001 登入NAS -> Private 拿不到Vlink Port: Login FAIL
    """
    def test_CHcloudlinkdePort_GLPrivateSSLON_login(self):
        '''Cloudlink login -> Login FAIL'''
        settings.login1(self, IP_or_Host = settings.NAS1.cloudlnk, AC="admin", PWD="@dmin1234", testMethod = "TUTK", LoginResult=0)
    
    def test_CHcloudlinkdePort_GLPrivateSSLOFF_login(self):
        '''Cloudlink login -> Login FAIL'''
        settings.login1(self, IP_or_Host = settings.NAS1.cloudlnk, AC="admin", PWD="@dmin1234", testMethod = "TUTK", LoginResult=0)
    """
    # CloudLink_Client: China, Default 8080/443 port; NAS: Global, Public, SSL ON/OFF
        # CloudLink + 5000/5001 登入NAS -> Public 拿到Vlink Port: Login PASS
    """
    def test_CHcloudlinkdePort_GLPublicSSLON_login(self):
        '''Cloudlink login -> Login PASS'''
        settings.login1(self, IP_or_Host=settings.NAS1.cloudlnk, AC="admin", PWD="@dmin1234", testMethod="TUTK")

    def test_CHcloudlinkdePortEnSSL_GLPublicSSLON_login(self):
        '''Cloudlink login -> Login PASS'''
        settings.login1(self, IP_or_Host=settings.NAS1.cloudlnk, AC="admin", PWD="@dmin1234", SSL="enable", testMethod="TUTK")
    
    def test_CHcloudlinkdePort_GLPublicSSLOFF_login(self):
        '''Cloudlink login -> Login PASS'''
        settings.login1(self, IP_or_Host=settings.NAS1.cloudlnk, AC="admin", PWD="@dmin1234", testMethod="TUTK")

    """

    # WANIP_Client: Global, Default 8080/443 port; NAS: China, Private, SSL ON/OFF
    """
    def test_GLWANIPdePort_CHPrivateSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="115.43.107.17", AC="cindy", PWD="cindy")

    def test_GLWANIPdePort_CHPrivateSSLOFF_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="115.43.107.17", AC="cindy", PWD="cindy")
    """
    # WANIP_Client: Global, Default 8080/443 port; NAS: China, Public, SSL ON/OFF
    """
    def test_GLWANIPdePort_CHPublicSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="115.43.107.17", AC="cindy", PWD="cindy")
    
    def test_GLWANIPdePort_CHPublicSSLOFF_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="115.43.107.17", AC="cindy", PWD="cindy")
    """

    # WANIP_Client: Global, Default 8080/443 port; NAS: China, Private, NondePort, SSL ON/OFF
    """
    def test_GLWANIPdePort_CHPrivateNondePortSSLON_login(self):
        '''WANIP login -> Login FAIL'''
        settings.login1(self, IP_or_Host=settings.China_NonDePortNAS.WANIP, AC=settings.China_NonDePortNAS.ac,
                        PWD=settings.China_NonDePortNAS.pwd, LoginResult = 0)
    
    def test_GLWANIPManualPortEnSSL_CHPrivateNondePortSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host=settings.China_NonDePortNAS.WANIP, AC=settings.China_NonDePortNAS.ac,
                        PWD=settings.China_NonDePortNAS.pwd, SSL="enable", AutoPort = "disable",
                        Connectport = settings.China_NonDePortNAS.Externalport_Se)
    """
    # WANIP_Client: Global, Default 8080/443 port; NAS: China, Public, NondePort, SSL ON/OFF
    """
    def test_GLWANIPdePort_CHPublicNondePortSSLOFF_login(self):
        '''WANIP login -> Login FAIL'''
        settings.login1(self, IP_or_Host=settings.China_NonDePortNAS.WANIP, AC=settings.China_NonDePortNAS.ac,
                        PWD=settings.China_NonDePortNAS.pwd, LoginResult = 0)
    """
    """
    def test_GLWANIPManualPort_CHPublicNondePortSSLOFF_login(self):
        '''WANIP login -> Login PASS'''
        settings.Regionset(self, "Globalset")
        settings.login1(self, IP_or_Host=settings.China_NonDePortNAS.WANIP, AC=settings.China_NonDePortNAS.ac,
                        PWD=settings.China_NonDePortNAS.pwd, AutoPort = "disable",
                        Connectport = settings.China_NonDePortNAS.Externalport)
    """
    # WANIP_Client: Global, Default 8080/443 port; NAS: Global, Public, SSL ON/OFF
    """
    @unittest.skipIf(settings.Product_flag == "Qcontactz", "Not support this case")
    def test_GLWANIPdePort_GLPublicSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U")

    def test_GLWANIPdePortEnSSL_GLPublicSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U", SSL="enable")

    def test_GLWANIPdePort_GLPublicSSLOFF_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="118.169.41.6", AC="admin", PWD="NcrgU17B9U")
    """
     # WANIP_Client: Global, Default 8080/443 port; NAS: Global, Private, SSL ON/OFF
    """
    @unittest.skipIf(settings.Product_flag == "Qcontactz", "Not support this case")
    def test_GLWANIPdePort_GLPrivateSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U")

    def test_GLWANIPdePortEnSSL_GLPrivateSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U", SSL="enable")
    def test_GLWANIPdePort_GLPrivateSSLOFF_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U")
    """
    # WANIP_Client: China, Default 5000/5001 port; NAS: China, Public, SSL ON/OFF
    """
    def test_CHWANIPdePort_CHPublicSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host=settings.China_NonDePortNAS.WANIP, AC="admin", PWD="80682695")
    
    def test_CHWANIPdePort_CHPublicSSLOFF_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="115.43.107.17", AC="admin", PWD="80682695")
    """
    # WANIP_Client: China, Default 5000/5001 port; NAS: China, Private, SSL ON/OFF
    """
    def test_CHWANIPdePort_CHPrivateSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="115.43.107.17", AC="cindy", PWD="cindy")

    def test_CHWANIPdePort_CHPrivateSSLOFF_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="115.43.107.17", AC="cindy", PWD="cindy")
    """
    # WANIP_Client: China, Default 5000/5001 port; NAS: Global, Private, SSL ON/OFF
    """
    @unittest.skipIf(settings.Product_flag == "Qcontactz", "Not support this case")
    def test_CHWANIPdePort_GLPrivateSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U")

    def test_CHWANIPdePortEnSSL_GLPrivateSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U", SSL="enable")

    def test_CHWANIPdePort_GLPrivateSSLOFF_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="118.169.41.6", AC="admin", PWD="NcrgU17B9U")

    def test_CHWANIPNondePort_GLPrivateSSLOFF_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="118.169.41.6", AC="admin", PWD="NcrgU17B9U",
                        AutoPort="disable", Connectport="8080")
    """

    # WANIP_Client: China, Default 5000/5001 port; NAS: Global, Public, SSL ON/OFF
    """
    @unittest.skipIf(settings.Product_flag == "Qcontactz" or settings.Product_flag == "Qsirch", "Not support this case")
    def test_CHWANIPdePort_GLPublicSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U")
    def test_CHWANIPdePortEnSSL_GLPublicSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U", SSL = "enable")

    def test_CHWANIPNondePortEnSSL_GLPublicSSLON_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U", SSL = "enable",
                       AutoPort = "disable", Connectport = "443")

    def test_CHWANIPdePort_GLPublicSSLOFF_login(self):
        '''WANIP login -> Login PASS'''
        settings.login1(self, IP_or_Host="36.225.219.252", AC="admin", PWD="NcrgU17B9U")
    """
    # myQNAP_Client: Global, Default 8080/443 port; NAS: China, Private, SSL ON/OFF
    """
    def test_GLmyQNAPcomdePort_CHPrivateSSLON_login(self):
        '''myQNAPcloud.com login -> Login FAIL'''
        settings.login1(self, IP_or_Host = "mingjehouse.myqnapcloud.com", AC = "cindy", PWD = "cindy", LoginResult = 0)
    def test_GLmyQNAPcndePort_CHPrivateSSLON_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host = "mingjehouse.myqnapcloud.cn", AC = "cindy", PWD = "cindy")
    def test_GLmyQNAPcomdePort_CHPrivateSSLOFF_login(self):
        '''myQNAPcloud.com login -> Login FAIL'''
        settings.login1(self, IP_or_Host = "mingjehouse.myqnapcloud.com", AC = "cindy", PWD = "cindy", LoginResult = 0)
    def test_GLmyQNAPcndePort_CHPrivateSSLOFF_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host = "mingjehouse.myqnapcloud.cn", AC = "cindy", PWD = "cindy")
    
    """

    # myQNAP_Client: Global, Default 8080/443 port; NAS: China, Public, SSL ON/OFF
    """
    def test_GLmyQNAPcomdePort_CHPublicSSLON_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.com", AC="cindy", PWD="cindy")
    def test_GLmyQNAPcndePort_CHPublicSSLON_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.cn", AC="cindy", PWD="cindy")
    def test_GLmyQNAPcomdePort_CHPublicSSLOFF_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.com", AC="cindy", PWD="cindy")
    def test_GLmyQNAPcndePort_CHPublicSSLOFF_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.cn", AC="cindy", PWD="cindy")
        
    """
    # myQNAP_Client: Global, Default 8080/443 port; NAS: Global, Public, SSL ON/OFF
    """
    def test_GLmyQNAPcomdePort_GLPublicSSLON_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.com", AC="admin", PWD="NcrgU17B9U")

    def test_GLmyQNAPcndePort_GLPublicSSLON_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.cn", AC="admin", PWD="NcrgU17B9U", testMethod = "QNAPDDNS")
    
    def test_GLmyQNAPcomdePort_GLPublicSSLOFF_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.com", AC="admin", PWD="NcrgU17B9U")

    def test_GLmyQNAPcndePort_GLPublicSSLOFF_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.cn", AC="admin", PWD="NcrgU17B9U", testMethod == "QNAPDDNS")
    
    """
    # myQNAP_Client: Global, Default 8080/443 port; NAS: Global, Private, SSL ON/OFF
    """
    def test_GLmyQNAPcomdePort_GLPrivateSSLOFF_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.com", AC="admin", PWD="NcrgU17B9U")

    def test_GLmyQNAPcndePort_GLPrivateSSLOFF_login(self):
        '''myQNAPcloud.cn login -> Login FAIL'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.cn", AC="admin", PWD="NcrgU17B9U",
                        testMethod="QNAPDDNS", LoginResult = 0)
    def test_GLmyQNAPcomdePort_GLPrivateSSLON_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.com", AC="admin", PWD="NcrgU17B9U")

    def test_GLmyQNAPcndePort_GLPrivateSSLON_login(self):
        '''myQNAPcloud.cn login -> Login FAIL'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.cn", AC="admin", PWD="NcrgU17B9U",
                        testMethod="QNAPDDNS", LoginResult = 0)
    
    """

    # myQNAP_Client: China, Default 5000/5001 port; NAS: China, Public, SSL ON/OFF
    """
    def test_CHmyQNAPcomdePort_CHPublicSSLON_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.com", AC="cindy", PWD="cindy", testMethod="QNAPDDNS")

    def test_CHmyQNAPcndePort_CHPublicSSLON_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.cn", AC="cindy", PWD="cindy")
    
    def test_CHmyQNAPcomdePort_CHPublicSSLOFF_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.com", AC="cindy", PWD="cindy", testMethod="QNAPDDNS")

    def test_CHmyQNAPcndePort_CHPublicSSLOFF_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.cn", AC="cindy", PWD="cindy")
    """


    # myQNAP_Client: China, Default 5000/5001 port; NAS: China, Private, SSL ON/OFF
    """
    def test_CHmyQNAPcomdePort_CHPrivateSSLON_login(self):
        '''myQNAPcloud.com login -> Login FAIL'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.com", AC="cindy", PWD="cindy", testMethod="QNAPDDNS",
                        LoginResult = 0)

    def test_CHmyQNAPcndePort_CHPrivateSSLON_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.cn", AC="cindy", PWD="cindy")
    
    def test_CHmyQNAPcomdePort_CHPrivateSSLOFF_login(self):
        '''myQNAPcloud.com login -> Login FAIL'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.com", AC="cindy", PWD="cindy", testMethod="QNAPDDNS",
                        LoginResult = 0)

    def test_CHmyQNAPcndePort_CHPrivateSSLOFF_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host="mingjehouse.myqnapcloud.cn", AC="cindy", PWD="cindy")
    """


    # myQNAP_Client: China, Default 5000/5001 port; NAS: Global, Private, SSL ON/OFF
    """
    def test_CHmyQNAPcomdePort_GLPrivateSSLON_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.com", AC="admin", PWD="NcrgU17B9U")

    def test_CHmyQNAPcndePort_GLPrivateSSLON_login(self):
        '''myQNAPcloud.cn login -> Login FAIL'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.cn", AC="admin", PWD="NcrgU17B9U", LoginResult=0)
    
    def test_CHmyQNAPcomdePort_GLPrivateSSLOFF_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.com", AC="admin", PWD="NcrgU17B9U")

    def test_CHmyQNAPcndePort_GLPrivateSSLOFF_login(self):
        '''myQNAPcloud.cn login -> Login FAIL'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.cn", AC="admin", PWD="NcrgU17B9U", LoginResult=0)
    """


    # myQNAP_Client: China, Default 5000/5001 port; NAS: Global, Public, SSL ON/OFF
    """
    def test_CHmyQNAPcomdePort_GLPublicSSLON_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.com", AC="admin", PWD="NcrgU17B9U")

    def test_CHmyQNAPcndePort_GLPublicSSLON_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.cn", AC="admin", PWD="NcrgU17B9U", testMethod="QNAPDDNS")
    
    def test_CHmyQNAPcomdePort_GLPublicSSLOFF_login(self):
        '''myQNAPcloud.com login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.com", AC="admin", PWD="NcrgU17B9U")

    def test_CHmyQNAPcndePort_GLPublicSSLOFF_login(self):
        '''myQNAPcloud.cn login -> Login PASS'''
        settings.login1(self, IP_or_Host="chehung8080.myqnapcloud.cn", AC="admin", PWD="NcrgU17B9U", testMethod="QNAPDDNS")
    """
    # myQNAP_Client: Global, Default 8080/443 port; NAS: China, Private, NondePort, SSL ON/OFF
    """
    def test_GLmyQNAPcomdePort_CHPrivateNondePortSSLON_login(self):
        '''myQNAPcloud.com -> Login FAIL'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.com", AC="admin", PWD="80682695", LoginResult=0)
    
    def test_GLmyQNAPcomdePort_CHPrivateNondePortSSLOFF_login(self):
        '''myQNAPcloud.com -> Login FAIL'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.com", AC="admin", PWD="80682695", LoginResult=0)

    def test_GLmyQNAPcndePort_CHPrivateNondePortSSLON_login(self):
        '''myQNAPcloud.cn -> Login FAIL'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695", LoginResult=0)
    
    def test_GLmyQNAPcndePort_CHPrivateNondePortSSLOFF_login(self):
        '''myQNAPcloud.cn -> Login FAIL'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695", LoginResult=0)


    def test_GLmyQNAPcomManualPort_CHPrivateNondePortSSLOFF_login(self): # 確認一下
        '''myQNAPcloud.com -> Login FAIL'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.com", AC="admin", PWD="80682695", LoginResult=0,
                        AutoPort = "disable", Connectport = "8084")
    
    def test_GLmyQNAPcnManualPort_CHPrivateNondePortSSLOFF_login(self):
        '''myQNAPcloud.cn -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695",
                        AutoPort = "disable", Connectport = "8084")

    def test_GLmyQNAPcnManualPortEnSSL_CHPrivateNondePortSSLON_login(self):
        '''myQNAPcloud.cn -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695", SSL="enable",
                        AutoPort = "disable", Connectport = "8085")
    """
    # myQNAP_Client: Global, Default 8080/443 port; NAS: China, Public, NondePort, SSL ON/OFF
    """
    def test_GLmyQNAPcomdePort_CHPublicNondePortSSLON_login(self):
        '''myQNAPcloud.com -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.com", AC="admin", PWD="80682695",
                        WAN_IP="118.169.41.6", testMethod = "QNAPDDNS")
    
    def test_GLmyQNAPcomdePort_CHPublicNondePortSSLOFF_login(self):
        '''myQNAPcloud.com -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.com", AC="admin", PWD="80682695",
                        WAN_IP="118.169.41.6", testMethod = "QNAPDDNS")
    
    def test_GLmyQNAPcndePort_CHPublicNondePortSSLON_login(self):
        '''myQNAPcloud.cn -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695",
                        WAN_IP="118.169.41.6", testMethod="QNAPDDNS")
    def test_GLmyQNAPcndePort_CHPublicNondePortSSLOFF_login(self):
        '''myQNAPcloud.cn -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695",
                        WAN_IP="118.169.41.6", testMethod="QNAPDDNS")
    """
    # myQNAP_Client: China, Default 5000/5001 port; NAS: China, Private, NondePort, SSL ON/OFF
    """
    def test_CHmyQNAPcomdePort_CHPrivateNondePortSSLON_login(self):
        '''myQNAPcloud.com -> Login FAIL'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.com", AC="admin", PWD="80682695",
                        LoginResult=0)
    
    def test_CHmyQNAPcomdePort_CHPrivateNondePortSSLOFF_login(self):
        '''myQNAPcloud.com -> Login FAIL'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.com", AC="admin", PWD="80682695",
                        LoginResult=0)
    
    def test_CHmyQNAPcndePort_CHPrivateNondePortSSLON_login(self):
        '''myQNAPcloud.cn -> Login FAIL'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695",
                        LoginResult=0)
    
    def test_CHmyQNAPcndePort_CHPrivateNondePortSSLOFF_login(self):
        '''myQNAPcloud.cn -> Login FAIL'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695",
                        LoginResult=0)
    
    def test_CHmyQNAPcomManualPortEnSSL_CHPrivateNondePortSSLON_login(self):
        '''myQNAPcloud.com -> Login FAIL'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.com", AC="admin", PWD="80682695", LoginResult=0,
                        SSL="enable", AutoPort="disable", Connectport="8085")
    
    def test_CHmyQNAPcnManualPortEnSSL_CHPrivateNondePortSSLON_login(self):
        '''myQNAPcloud.cn -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695",
                        SSL="enable", AutoPort="disable", Connectport="8085")
    def test_CHmyQNAPcnManualPort_CHPrivateNondePortSSLON_login(self):
        '''myQNAPcloud.cn -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695",
                        AutoPort="disable", Connectport="8084", LoginResult=0)
                        
    """

    #### myQNAP_Client: China, Default 5000/5001 port; NAS: China, Public, NondePort, SSL ON/OFF
    """
    def test_CHmyQNAPcomdePort_CHPublicNondePortSSLON_login(self):
        '''myQNAPcloud.com -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.com", AC="admin", PWD="80682695",
                        WAN_IP="36.225.217.149", testMethod="QNAPDDNS", myDDNS="atext8082")
    
    def test_CHmyQNAPcomdePort_CHPublicNondePortSSLOFF_login(self):
        '''myQNAPcloud.com -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.com", AC="admin", PWD="80682695",
                        WAN_IP="36.225.217.149", testMethod="QNAPDDNS", myDDNS="atext8082")
    
    def test_CHmyQNAPcndePort_CHPublicNondePortSSLON_login(self):
        '''myQNAPcloud.cn -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695")
    
    def test_CHmyQNAPcndePort_CHPublicNondePortSSLOFF_login(self):
        '''myQNAPcloud.cn -> Login PASS'''
        settings.login1(self, IP_or_Host="atext8082.myqnapcloud.cn", AC="admin", PWD="80682695")
    """

    #@classmethod
    def tearDown(self):
        print("close")

        #self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    #tests = ["test_minus1", "test_uu", "test_add", "test_mul", "test_minus"]
    for i in range(settings.loop_times):
        suite.addTests(unittest.makeSuite(Login))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(yu))
    #suite = unittest.TestSuite(map(yu, tests))

    # suite.addTests(suite1)
    print(suite)
    xmlrunner.XMLTestRunner(verbosity=2,output="xmltest").run(suite)
    """
    result = BeautifulReport(suite)
    result.report(description=des, filename=report_title, log_path=report)
    """