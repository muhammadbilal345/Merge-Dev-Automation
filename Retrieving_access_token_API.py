import time, uvicorn
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/get_access_token")
async def access_token(email: str, password: str):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()

    driver.maximize_window()

    try:
        driver.get("https://www.merge.dev")

        login_btn = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav-sign-in > div > svg'))
        )
        login_btn.click()

        email_txt = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.Login > div.Login-form.d-flex.align-items-center.justify-content-center > div > form > div:nth-child(3) > input'))
        )
        email_txt.send_keys(email)

        pwd_txt = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.Login > div.Login-form.d-flex.align-items-center.justify-content-center > div > form > div:nth-child(4) > input'))
        )
        pwd_txt.send_keys(password)

        login = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.Login > div.Login-form.d-flex.align-items-center.justify-content-center > div > form > div:nth-child(5) > button'))
        )
        login.click()

        linked_acc = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#sidebarCollapse > ul > li:nth-child(3) > a'))
        )
        linked_acc.click()

        acc = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.sc-dJjNIA.eEjfBG > div > div > div > div > div.row > div > div:nth-child(4) > div > div > table > tbody > tr > td.text-right > div > span:nth-child(4) > span'))
        )
        acc.click()
        
        time.sleep(2)
        acc_token = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.sc-dJjNIA.eEjfBG > div > div > div > div > div:nth-child(2) > div > div > div.sc-kgSa-dv.jQXwii.col-xl-3 > div > div > div > div:nth-child(3) > div.sc-cVEUmN.kiceSx.flex.align-items-center > div.sc-jEItEs.eONaae > svg'))
        )
        acc_token.click()
        
        time.sleep(2)
        acc_token_text = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.sc-dJjNIA.eEjfBG > div > div > div > div > div:nth-child(2) > div > div > div.sc-kgSa-dv.jQXwii.col-xl-3 > div > div > div > div:nth-child(3) > div.sc-cVEUmN.kiceSx.flex.align-items-center > div.sc-bJcRwn.dVQbxr'))
        )
        acc_token_value = acc_token_text.text

        time.sleep(2)
        setting = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.sc-dJjNIA.eEjfBG > div > div > div > div > div:nth-child(1) > div > div.sc-icMgfS.eCWyMS > div > div:nth-child(2) > ul > li:nth-child(6) > div > div > div > a'))
        )
        setting.click()
        
        time.sleep(2)
        origin_id = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.sc-dJjNIA.eEjfBG > div > div > div > div > div:nth-child(2) > div > div.d-flex.flex-column.card > div.flex.flex-column.gap-8.p-5 > div:nth-child(1) > div.flex.items-center.py-2.px-4.text-\[\#737982\].mt-2.rounded-md.bg-gray-0'))
        )
        origin_id_value = origin_id.text

        time.sleep(2)
        email = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.sc-dJjNIA.eEjfBG > div > div > div > div > div:nth-child(2) > div > div.d-flex.flex-column.card > div.flex.flex-column.gap-8.p-5 > div:nth-child(2) > div.flex.items-center.py-2.px-4.text-\[\#737982\].mt-2.rounded-md.bg-gray-0'))
        )
        email_value = email.text

    finally:
        driver.quit()

    return {"origin_id": origin_id_value, "email": email_value, "access_token": acc_token_value}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)