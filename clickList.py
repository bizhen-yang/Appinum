from appium import webdriver

from appium import webdriver
import common
import time
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.1.2"
caps["deviceName"] = "32e784340704"
caps["noReset"] = True
caps["appPackage"] = "com.rr.hitube"
caps["appActivity"] = "com.rr.hitube.ui.main.FirstActivity"

		
def getSize(dr):
    x = dr.get_window_size()['width']
    y = dr.get_window_size()['height']
    return (x, y)
	
def swipeUp(y,dr):
    l = getSize(dr)
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.75-y)   #终点y坐标
    dr.swipe(x1, y1, x1, y2,0)
	
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
time.sleep(20)

#点击频道
driver.find_element_by_id("com.rr.hitube:id/iv_sort").click()


video = 0
i = 1
while video < 100:
    d = []
    d = driver.find_elements_by_id("com.rr.hitube:id/iv_download")
    #print(d)
    for j in range(len(d)):
        d[j].click()


    swipeUp( 1000,driver)
    video = video + len(d)
    print(str(video) + ' num')		

driver.quit()