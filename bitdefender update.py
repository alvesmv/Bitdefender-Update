import tempfile
import os
import time
import glob
import shutil
from selenium import webdriver
from tkinter import messagebox
from datetime import date


def atualizacao():
    try:
        # apaga atualizações
        ultimo_update = glob.glob(
            r"\\smc08\Home\Publico\0 Atualização do Antivírus\*.exe")
        for item in ultimo_update:
            os.remove(item)
        # define diretorio temporario para download
        diretorio_download = tempfile.mkdtemp()
        # define preferencias do navegador
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 5)
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference(
            "browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", diretorio_download)
        profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        # abre uma instancia do Firefox
        driver = webdriver.Firefox(
            firefox_profile=profile, executable_path=r'geckodriver.exe') # driver deve está no mesmo caminho do script py ou exe
        # acessa o endereço do endereço web
        driver.get(
            "https://www.bitdefender.com/support/how-to-manually-update-bitdefender-endpoint-security-tools-(best)-1875.html")
        driver.implicitly_wait(20)
        element = driver.find_element_by_xpath(
            "/html/body/section[3]/div[3]/div/div[1]/div[2]/div[1]/div/ol/li[1]/ul/li[2]/a")
        element.click()
        time.sleep(3)
        # espera o download terminar
        while glob.glob(diretorio_download + '\\*.part') != []:
            time.sleep(1)

        driver.quit()  # encerra o navegador
        # copia o arquivo para o destino
        time.sleep(3)
        origem = glob.glob(diretorio_download + "\\*.exe")[0]
        destino = r"\\smc08\Home\Publico\0 Atualização do Antivírus\Bitdefender Update " + \
            date.today().strftime('%Y.%m.%d') + ".exe"
        shutil.copy(origem, destino)
        completo = True
    except:
        completo = False
    finally:
        shutil.rmtree(diretorio_download)
    if completo:
        messagebox.showinfo("Bitdefender Update", "Download finalizado!")
    else:
        messagebox.showerror("Bitdefender Update",
                             "Não foi possivel realizar o download")


if __name__ == "__main__":
    atualizacao()
