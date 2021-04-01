#!/usr/bin/env python3
# coding: utf-8

# 参考: https://www.jianshu.com/p/25fd8a5dddc9
# 参考: https://www.cnblogs.com/98WDJ/p/11050559.html

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
import time
from random import random, randint
from PIL import Image
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

shimo_url = "https://shimo.im/"
shimo_user = ""
shimo_password = ""


def get_snap(web_driver):
    """获取网页的快照图"""
    file_name = "snap.png"
    web_driver.save_screenshot(file_name)
    snap_obj = Image.open(file_name)
    return snap_obj


def get_captcha_position(web_driver):
    """获取验证码图片在网页中的位置"""
    img_element = web_driver.find_element_by_xpath(
        '//div[@class="geetest_panel_next"]//canvas[@class="geetest_canvas_slice geetest_absolute"]'
    )
    size = img_element.size
    location = img_element.location
    left = location['x']
    top = location['y']
    right = left+size['width']
    bottom = top+size['height']
    captcha_position = (left, top, right, bottom,)
    return captcha_position


def get_captcha_image(web_driver, captcha_position, image_file_name):
    """截取出验证码图片"""
    snap_obj = get_snap(web_driver)
    img_obj = snap_obj.crop(captcha_position)
    img_obj.save(image_file_name)
    return img_obj


def get_distance(img1, img2):
    """获取滑块到缺口的距离"""
    # 初始X
    start_x = 60
    # 阈值
    threshold = 60
    for x in range(start_x, img1.size[0]):
        for y in range(img1.size[1]):
            rgb1 = img1.load()[x, y]
            rgb2 = img2.load()[x, y]
            res1 = abs(rgb1[0] - rgb2[0])
            res2 = abs(rgb1[1] - rgb2[1])
            res3 = abs(rgb1[2] - rgb2[2])
            if not (res1 < threshold and res2 < threshold and res3 < threshold):
                return x-7


def get_track(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 3 / 5
    # 计算间隔
    t = 0.4
    # 初速度
    v = 0
    while current < distance:  # 所以 track是不会大于总长度的
        if current < mid:
            # 加速度为正
            a = randint(3, 5)
        else:
            # 加速度为负
            a = - randint(1, 4)
        # 初速度v0
        v0 = v
        # 移动距离x = v0t + 1/2 * a * t^2，现做了加速运动
        move = v0 * t + 1 / 2 * a * t * t
        # 当前速度v = v0 + at  速度已经达到v，该速度作为下次的初速度
        v = v0 + a * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))  # track 就是最终鼠标在 X 轴移动的轨迹

    while current > distance:
        track.append(distance - current)
        break

    logger.debug(f"移动轨迹: {track}")
    return track


def login(web_browser):
    web_browser.get(shimo_url)
    time.sleep(random() * 3)
    # 点击登录按钮
    web_browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[2]/a[2]/button').click()
    time.sleep(random() * 3)
    # 填写用户名
    web_browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/div/input').send_keys(shimo_user)
    time.sleep(random() * 2)
    # 填写密码
    web_browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/input').send_keys(shimo_password)
    time.sleep(random() * 5)
    # 点击立即登录
    web_browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div/div/div[1]/button').click()
    time.sleep(random() * 5)
    return web_browser


def main():
    web_browser = Chrome()
    # 石墨文档输入账号密码登录
    login(web_browser)
    # 验证码图片(保留两张图, 用于测试或debug)
    captcha_image = "captcha.png"
    # 验证码背景图
    captcha_image_bg = "captcha_bg.png"
    captcha_position = get_captcha_position(web_browser)
    captcha_image_obj = get_captcha_image(web_browser, captcha_position, captcha_image)
    time.sleep(0.5)
    # 修改网页代码, 使显示验证码背景图
    web_browser.execute_script(
        '''
        var x=document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0];
        x.removeAttribute("style");
        '''
    )
    captcha_image_bg_obj = get_captcha_image(web_browser, captcha_position, captcha_image_bg)
    # 还原网页代码
    web_browser.execute_script(
        '''
        var x=document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0];
        x.setAttribute("style", "opacity: 1; display: none;");
        '''
    )
    distance = get_distance(captcha_image_obj, captcha_image_bg_obj)
    logger.info(f"滑块到缺口的距离: {distance}")

    # 滑块按钮的位置
    slider = web_browser.find_element_by_class_name('geetest_slider_button')
    track = get_track(distance)
    # 拖住滑块
    ActionChains(web_browser).click_and_hold(slider).perform()
    # 按轨迹拖动滑块到缺口
    for x in track:
        ActionChains(web_browser).move_by_offset(xoffset=x, yoffset=0).perform()

    time.sleep(0.2)
    # 抬起鼠标左键
    ActionChains(web_browser).release().perform()
    time.sleep(3)
    if "/dashboard/" in web_browser.current_url:
        logger.info("登录成功")
    else:
        logger.info("登录失败, 请再试一次.")

    time.sleep(120)
    web_browser.close()


if __name__ == '__main__':
    main()
