from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import configparser

# 获取配置文件所在的目录
config_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "./config/config.ini"
)

# 读取配置文件
config = configparser.ConfigParser()
config.read(config_path)

# 输出配置文件中的值 解锁钱包要用
print(config.get("argent", "argent_password"))

#sleep时间，根据自己电脑和网络修改


def main():
    password = config.get("argent", "argent_password")
    print(f"value:{password}")

    #swap 金额数量 usdc/usdt
    inNum = config.get("task", "input_number")
 
    opt = uc.ChromeOptions()
    userDataDir = config.get("chrome", "user_data_dir")
    profileDirectory = config.get("chrome", "profile_directory")
    executablePath = config.get("chrome", "executable_path")
    print(
        f"userDataDir:{userDataDir},profileDirectory:{profileDirectory},executablePath:{executablePath}"
    )
    opt.add_argument(f"--user-data-dir={userDataDir}")
    print(f"--user-data-dir={userDataDir}")


    opt.add_argument(f"--profile-directory={profileDirectory}")
    print(f"--profile-directory={profileDirectory}")


    driver = uc.Chrome(executable_path=executablePath, options=opt, use_subprocess=True)

    print(f"已打开chrome浏览器")
    url = config.get("argent", "argent_url")
    driver.get(url)
    print(f"已加载:{url}")
    time.sleep(5)
    
    search_box = driver.find_element(
        "xpath", '//*[@id="root"]/div/div/div/div/div/div/div/div[2]/form/input'
    )
    driver.implicitly_wait(5)
    time.sleep(10)
    search_box.send_keys(password)
    time.sleep(5)
    search_box.send_keys(Keys.ENTER)
    time.sleep(10)
    current_window = driver.current_window_handle
    print(
        f"passwdcurrent_window:{current_window};current_url:{driver.current_url};title:{driver.title}"
    )


    print(f"解锁skartnet agent钱包")
    current_window = driver.current_window_handle
    current_url = driver.current_url

    print(
        f"current_window:{current_window};current_url:{driver.current_url};title:{driver.title}"
    )

    driver.get(config.get("task", "jediswap"))
    driver.find_element(
        "xpath", "/html/body/reach-portal/div[2]/div/div/div/div/div/button"
    ).click()
    print(f"链接钱包")
    time.sleep(6)

    time.sleep(6)
    current_window = driver.current_window_handle
    print(
        f"current_window:{current_window};current_url:{driver.current_url};title:{driver.title}"
    )
    handles = driver.window_handles  # 返回值是一个列表
    print(f"handles:{handles}")

    print(f"handles23:{handles}")
    driver.switch_to.window(handles[0])
    time.sleep(10)
    print(
        f"connect-walletcurrent_window:{current_window};current_url:{driver.current_url};title:{driver.title}"
    )

    print(f"已选择地址")
    driver.implicitly_wait(10)
    time.sleep(6)

    # 选择币种

    driver.find_element(
        "xpath", '//*[@id="swap-currency-input"]/div/div[2]/button'
    ).click()

    driver.implicitly_wait(3)
    time.sleep(1)
    driver.find_element(
        By.CLASS_NAME,
        "token-item-0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8",
    ).click()
    # token-item-0x068f5c6a61780768455de69077e07e89787839bf8166decfbf92b645209c0fb8

    # sc-gqjmRU sc-ckVGcZ sc-jKJlTe sc-likbZx joxsSn token-item-ETHER
    # //*[@id="swap-currency-output"]/div/div[2]/button/div/svg
    time.sleep(3)
    driver.implicitly_wait(3)
    driver.find_element(
        "xpath", '//*[@id="swap-currency-output"]/div/div[2]/button'
    ).click()
    time.sleep(2)
    driver.find_element(
        By.CLASS_NAME,
        "token-item-0x068f5c6a61780768455de69077e07e89787839bf8166decfbf92b645209c0fb8",
    ).click()
    # token-item-0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8
    time.sleep(5)

    input_box = driver.find_element(By.CLASS_NAME, "token-amount-input")
    # //*[@id="swap-currency-input"]/div/div[2]/input
    input_box.send_keys(inNum)
    time.sleep(10)

    # swap-button提交
    driver.find_element("xpath", '//*[@id="swap-button"]').click()
    driver.implicitly_wait(15)
    time.sleep(4)
    # //*[@id="confirm-swap-or-send"]/div
    driver.find_element("xpath", '//*[@id="confirm-swap-or-send"]/div').click()
    driver.implicitly_wait(5)
    time.sleep(10)
    print(
        f"buttoncurrent_window:{driver.current_window_handle};current_url:{driver.current_url};title:{driver.title}"
    )
    print(f"buttonhandles:{driver.window_handles}")
    handles = driver.window_handles  # 返回值是一个列表
    print(f"handles2:{handles}")
    driver.switch_to.window(handles[1])
    print(
        f"comfirmcurrent_window:{driver.current_window_handle};current_url:{driver.current_url};title:{driver.title}"
    )
    time.sleep(6)
    driver.implicitly_wait(3)
    # 切换argent//*[@id="accordion-button-:rl:"]
    driver.find_element(By.CLASS_NAME, "css-1ih3oay").click()
    time.sleep(2)
    driver.implicitly_wait(3)
    driver.switch_to.window(handles[0])
    time.sleep(30)
    print(
        f"huicomfirmcurrent_window:{driver.current_window_handle};current_url:{driver.current_url};title:{driver.title}"
    )
    driver.find_element(
        "xpath", "html/body/reach-portal/div[2]/div/div/div/div/div/div/div[3]/button"
    ).click()

    time.sleep(50)
    driver.quit()


if __name__ == "__main__":
    main()
