from selenium import webdriver
import os
working_dir = os.getcwd()

download_dir = working_dir + "\\data"
options = webdriver.ChromeOptions()

profile = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }

options.add_experimental_option("prefs", profile)
options

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)  # Optional argument, if not specified will search path.

pdf_url = "https://www.ingentaconnect.com/contentone/imp/jcs/2019/00000026/f0020011/art00001?crawler=true&mimetype=application/pdf"
driver.get(pdf_url)

