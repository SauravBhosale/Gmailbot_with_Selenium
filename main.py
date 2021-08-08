#EmailBot with Selenium

from selenium import webdriver
path = 'C:\\Users\\SAURAV\\OneDrive\\Desktop\\Python\\Gmailbot\\msedgedriver.exe' #Give Your Path
driver = webdriver.Edge(path)

#Gmail login URL
url = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

#Activate the driver
driver.get(url)

#input email
email ='Your mail_id' # input your mail_id
email_account = driver.find_element_by_xpath('//*[@id="identifierId"]')
email_account.send_keys(email)

#Click next
button_next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
button_next.click()

#Enter Password
password_input = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys('Your_Password') #input your password

#Click next
button_next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
button_next.click()

#Wait load time
driver.implicitly_wait(50)

#Click the Compose Button
compose_msg = driver.find_element_by_xpath('//*[@id=":kz"]/div/div')
compose_msg.click()

#Destination email:
to = driver.find_element_by_xpath('//*[@id=":rf"]')
to.send_keys('dest_email')  #input your destination mail_id

#Subject of the Mail
subject = driver.find_element_by_xpath('//*[@id=":qx"]')
subject.send_keys('Automated_Mail')

#Content of the Mail
msg= driver.find_element_by_xpath('//*[@id=":s2"]')
msg.send_keys('Hi This is a sample mail for my web automation project')

#Click the Send Button
send = driver.find_element_by_xpath('//*[@id=":qn"]')
send.click()
