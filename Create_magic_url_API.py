import uvicorn
from fastapi import FastAPI, HTTPException
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
@app.post("/generate_url")
async def generate_url(email: str, password: str, organization_name: str, link_email: str, user_origin_id: str):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()
        driver.maximize_window()
        
        driver.get("https://www.merge.dev")
        
        login_btn = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav-sign-in > div > svg'))
        )
        login_btn.click()
        
        email_txt = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.Login > div.Login-form.d-flex.align-items-center.justify-content-center > div > form > div:nth-child(3) > input'))
        )
        email_txt.send_keys(email)
        
        password_txt = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.Login > div.Login-form.d-flex.align-items-center.justify-content-center > div > form > div:nth-child(4) > input'))
        )
        password_txt.send_keys(password)
        
        login = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.Login > div.Login-form.d-flex.align-items-center.justify-content-center > div > form > div:nth-child(5) > button'))
        )
        login.click()
        
        linked_acc = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#sidebarCollapse > ul > li:nth-child(3) > a'))
        )
        linked_acc.click()
        
        create_link_btn = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.sc-dJjNIA.eEjfBG > div > div > div > div > div.sc-cCqACh.khrydy > div > div.d-flex.flex-row.justify-content-between > div.h-100.p-2 > button'))
        )
        create_link_btn.click()
        
        org_name_txt = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#organizationName'))
        )
        org_name_txt.send_keys(organization_name)
        
        link_email_txt = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#email'))
        )
        link_email_txt.send_keys(link_email)
        
        categories_dd = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#categories'))
        )
        categories_dd.click()
        
        hris = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#hris'))
        )
        hris.click()
        
        user_origin_id_txt = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#uniqueIdentifier'))
        )
        user_origin_id_txt.send_keys(user_origin_id)
        
        gen_url_btn = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.fade.modal-shadow.fit-content.modal.show > div > div > div.modal-body > div > div > div:nth-child(2) > form > div.d-flex.justify-content-center.row > div > button'))
        )
        gen_url_btn.click()
        
        url = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.fade.modal-shadow.fit-content.modal.show > div > div > div.modal-body > div > div > div:nth-child(1) > div:nth-child(3) > div > div.sc-fmciRz.bsKOPo > div'))
        )
        
        url_text = url.text
        driver.quit()
        return {"url": url_text}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)