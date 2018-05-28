import datetime
import schedule
import requests
import random
from bs4 import BeautifulSoup

today = datetime.datetime.now().strftime("%m/%d/%y")
shift = "0700-12"
url = "https://mytimeremote.lhs.org/APIHC/TASS/WebPortal/APIHealthcare/Login.aspx"
soup = requests.get(url)
data = BeautifulSoup(soup, 'html.parser')
print(data.prettify())
#
# def job():
#     print("I'm doing your schedule for you...")
# ##LOGIN
#     url = "https://mytimeremote.lhs.org/APIHC/TASS/WebPortal/APIHealthcare/Login.aspx"
#     name_id = "formContentPlaceholder$_userNameField"
# ##cleifer
#     pw_id = "formContentPlaceholder$_passwordField"
# ##Stewie5!
#     sign_in = "formContentPlaceholder_loginApiButton"
# ##signin click
#
# ##SECTIONPICK
#     a_translate = "sections.employee"
# ##employee tab click
#
# ##SCHEDULESELF
#     sched_id = "formContentPlaceholder_selfScheduleApiButton"
# ## schedule click
#
# ##DATEPICK
#     table_id = "formContentPlaceholder_myScheduleTable"
#     img_id = "formContentPlaceholder_activityList_3_rightImage"
# ##click
#     div_class = " dropDown dropDownBox"
#     day = div_class.select("div div:nth-of-type(2)")
# ##second child onmousedown= "setValue(this, event)"
#
#
# ##PICK SHIFT
# ##THREE SHIFTS PER WEEK
# ##THREE WEEKENDS per SIX WEEK BLOCK
# ##randomly 3 out of every 7 (excluding 3+7's), min 3 weekends (multiples 7, +=1) <= 78
#     index_list = [range(0,43)]
#     weekends = [7,14,21,28,35,42]
#
#     save_sched = "formContentPlaceholder_saveApiButton"
# ##click
#
# schedule.every().sunday.at("00:01").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)