import time
import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])
name = testdata["username"]
passwd = testdata["password"]

def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, er1):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector3)
    text = err_label.text
    assert text == er1

def test_step2(x_selector1, x_selector2, x_selector3, x_selector4, btn_selector, er2):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(name)
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(passwd)
    btn = site.find_element("css", btn_selector)
    btn.click()
    user_label = site.find_element("xpath", x_selector4)
    text = user_label.text
    assert text == er2
    
def test_step3(new_post_btn, title, description, content, save_btn, res_lbl):
    btn = site.find_element("css", new_post_btn)
    btn.click()
    time.sleep(3)
    
    input1 = site.find_element("xpath", title)
    input1.clear()
    input1.send_keys(testdata["title"])
    time.sleep(3)
    
    input2 = site.find_element("xpath", description)
    input2.clear()
    input2.send_keys(testdata["description"])
    time.sleep(3)
    
    input3 = site.find_element("xpath", content)
    input3.clear()
    input3.send_keys(testdata["content"]
    time.sleep(3)
    
    btn2 = site.find_element("xpath",save_btn)
    btn2.click()
    time.sleep(3)
    
def test_step4()
    element = site.find_element("xpath", res_lbl)
    assert element.text == "Йоркширский терьер"

site.close()