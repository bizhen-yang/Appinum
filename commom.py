from appium import webdriver

#基础函数

#获得机器屏幕大小x,y
def getSize(dr):
    x = dr.get_window_size()['width']
    y = dr.get_window_size()['height']
    return (x, y)
 
#屏幕向上滑动
def swipeUp(t,dr):
    l = getSize(dr)
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    dr.swipe(x1, y1, x1, y2,t)

#屏幕向下滑动
def swipeDown(t,dr):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    dr.swipe(x1, y1, x1, y2,t)
#屏幕向左滑动
def swipLeft(t,dr):
    l=getSize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    dr.swipe(x1,y1,x2,y1,t)
#屏幕向右滑动
def swipRight(t,dr):
    l=getSize()
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    dr.swipe(x1,y1,x2,y1,t)

def is_element_exist(css):
    s = driver.find_element_by_xpath(css_selector=css)
    if len(s) == 0:
        return False
    elif len(s) == 1:
        return True