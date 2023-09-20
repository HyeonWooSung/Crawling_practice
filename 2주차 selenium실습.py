#!/usr/bin/env python
# coding: utf-8

# In[35]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome('C:/Users/User/chromedriver.exe',options=options)
driver.implicitly_wait(2)
driver.get('https://www.daum.net/')
# driver.find_element_by_xpath('//*[@id="daumHead"]/div[2]/div/div[1]/ul/li[4]/a').click()
# //*[@id="q"]
# driver.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[3]').send_keys(Keys.ENTER)

element = driver.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[3]') #검색창 html의 name이 'q'여서 q다
element.send_keys('구글')            #검색 단어를 입력한다
# element.submit()
# driver.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[3]').click()
element.send_keys(Keys.ENTER)


# In[10]:


# driver.find_element_by_xpath('//*[@id="main-area"]/div[7]/a[2]') #xpath 로 접근
# driver.find_element_by_class_name('ico_search_submit')	#class 속성으로 접근
# driver.find_element_by_id('k_btn')	#id 속성으로 접근
# driver.find_element_by_link_text('회원가입')	#링크가 달려 있는 텍스트로 접근
# driver.find_element_by_css_selector('#account > div > a')	#css 셀렉터로 접근
# driver.find_element_by_name('join')	#name 속성으로 접근
# driver.find_element_by_partial_link_text('가입')	#링크가 달려 있는 엘레먼트에 텍스트 일부만 적어서 해당 엘레먼트에 접근
# driver.find_element_by_tag_name('input')	#태그 이름으로 접근


# In[9]:


#4. 클릭 .click()
# driver.find_element_by_xpath('//*[@id="main-area"]/div[7]/a[2]').click()

#5. 텍스트 입력/엔터 .send_keys('텍스트') / .send_keys(Keys.ENTER)
# driver.find_element_by_name('query').send_keys('보라매역')
# driver.find_element_by_name("query").send_keys(Keys.ENTER)

#6. 텍스트 삭제 .clear()
# driver.find_element_by_name("query").clear()

# #7. iframe 지정 switch_to.frame
#   #iframe 지정
# element = driver.find_element_by_tag_name('iframe')

#   #프레임 이동
# driver.switch_to.frame(element)

#   #프레임에서 빠져나오기
# driver.switch_to.default_content()

#8. 팝업창 이동 / 수락 / 거절
#경고창으로 이동
# driver.switch_to.alert

# from selenium.webdriver.common.alert import Alert

# Alert(driver).accept()    #경고창 수락 누름
# Alert(driver).dismiss()   #경고창 거절 누름
# print(Alert(driver).text  # 경고창 텍스트 얻음

#9. 스크롤 내리기
#브라우저 스크롤 최하단으로 이동
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

#10. 스크린샷
#캡쳐할 엘레먼트 지정
# element = driver.driver.find_element_by_class_name('ico.target')

# #캡쳐 (name에는 파일명)
# element.save_screenshot('name.jpg')



# In[ ]:





# In[ ]:





# In[ ]:




