import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fungsi untuk mencoba login dengan email yang diberikan
def test_login(email, password):
    driver = webdriver.Firefox()
    driver.maximize_window()
    try:
        # Buka halaman login coursera
        driver.get("https://www.coursera.org/?authMode=login")

        # Cari elemen input email
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        username_input.clear()
        username_input.send_keys(email)

        # Cari elemen input password
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password")))
        password_input.clear()
        password_input.send_keys(password)

        # Submit form login
        password_input.send_keys(Keys.RETURN)

        # Mengisi captcha
        print("selesaikan captca dalam 20 detik")
        time.sleep(20) #jeda 20 detik

        try:
            # Cari pesan error jika login gagal
            error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='_p2k6y2 css-1dg8j96']"))
            )
            # Jika error message ditemukan, maka login gagal
            print("Failed")
        except:
            # Jika tidak ada error message, maka login berhasil
            # Memastikan kita benar-benar berada di halaman utama setelah login
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='rc-MetatagsWrapper']"))
            )
            print("Passed")

    finally:
        # Tutup browser
        driver.quit()

# Test case untuk login dengan email yang salah
test_login("kiramaze@gmail.com", "Putra002")

# Test case untuk login dengan username dan password yang benar
test_login("kyramaze@gmail.com", "Putra002")
