
## Looping over env variables
import os
for k, v in os.environ.items():
    print("%s = %s" %(k,v))


## Problems with speed using Internet Explorer    
from selenium.webdriver import IeOptions
ieo = IeOptions()
ieo.require_window_focus = True
driver = webdriver.Ie("G:\z-BPA\IEDriver\IEDriverServer.exe", options=ieo)

