import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def iniciar_driver():
    """Inicializando o WebDriver do Chrome."""
    chrome_options = Options()

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    return driver


def executar_scraping():
    driver = iniciar_driver()
    aguardar = WebDriverWait(driver, 10)

    try:
        url = "https://www.imdb.com"
        driver.get(url)

        input_busca = aguardar.until(
            EC.element_to_be_clickable((By.ID, "suggestion-search"))
        )

        input_busca.click()
        input_busca.clear()
        input_busca.send_keys("John Travolta")
        print("Texto digitado com sucesso!")

        input_busca.send_keys(Keys.ENTER)

        container_imagem = aguardar.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-testid="nlib-img-container"]')
            )
        )

        container_imagem.click()
        print("Elemento (data-testid) clicado com sucesso!")

        url_atual = driver.current_url
        url_esperada = "https://www.imdb.com/name/nm0000237/?ref_=fn_i_1"

        if url_esperada in url_atual or "nm0000237" in url_atual:
            print(
                f"Sucesso! A página aberta corresponde ao ator. URL: {url_atual}"
            )
        else:
            print(
                f"Aviso: O robô pode estar na página errada! URL atual: {url_atual}"
            )

        print("Iniciando a busca pelo filme...")

        print("Buscando o filme pelo nome nos resultados...")

        filme = aguardar.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//a[contains(., 'Swordfish') or contains(., 'Operação Swordfish')]",
                )
            )
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            filme,
        )
        time.sleep(1)
        driver.execute_script("arguments[0].click();", filme)
        print("Filme clicado pelo nome! Entrando na página...")

        print("Buscando pelo ator 'John Travolta'...")

        try:
            xpath_container_ator = "//*[text()='John Travolta']/ancestor::*[contains(@class, 'title-cast-item') or contains(@data-testid, 'title-cast-item')][1]"

            bloco_ator = aguardar.until(
                EC.presence_of_element_located((By.XPATH, xpath_container_ator))
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                bloco_ator,
            )
            time.sleep(1)

            texto_do_bloco = bloco_ator.text
            print(
                f"\n--- Texto detectado no bloco ---\n{texto_do_bloco}\n--------------------------------"
            )

            if "Gabriel" in texto_do_bloco:
                print(
                    "Sucesso! O texto 'Gabriel' foi encontrado dentro do bloco do John Travolta."
                )
            else:
                print(
                    "O bloco do actor foi achado, mas o texto 'Gabriel' NÃO está dentro dele."
                )

        except Exception as erro:
            print(f"Erro ao tentar localizar o ator ou o container: {erro}")

        time.sleep(3)

    except Exception as e:
        print(f"Ocorreu um erro durante o scraping: {e}")

    finally:
        driver.quit()
        print("Navegador fechado corretamente.")


if __name__ == "__main__":
    executar_scraping()