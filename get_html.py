# PRG1:ライブラリ設定
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs

CHROMEDRIVER = '/opt/chrome/chromedriver'

def get_html(url):
    html = ''
    try:
        # ChromeでURLに接続
        options = Options()
        options.add_argument('--headless')  
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        chrome_service = fs.Service(executable_path=CHROMEDRIVER) 
        browser = webdriver.Chrome(service=chrome_service, options=options)
        browser.get(url)
        html = browser.page_source.encode('utf-8')
    # エラー発生時の例外処理
    except Exception as e:
        message = '[エラー]'+'type:{0}'.format(type(e))+'\n'+'args:{0}'.format(e.args)
        print(message)

    # Chrome終了処理
    finally:
        browser.close()
        browser.quit()

    return html