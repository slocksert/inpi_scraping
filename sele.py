from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Inpi:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login"
        self.coords = [17.83, 50]
        self.map_id = "Map3"

    def open_page(self):
        self.driver.get(self.url)
  
    def click_on_map(self) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"img[usemap='#Map3']"))
        )

        script = """
        function clickOnArea(mapId, coords) {
            const mapElement = document.getElementById(mapId);
            const imgElement = document.querySelector(`img[usemap='#${mapId}']`);

            const imgRect = imgElement.getBoundingClientRect();
            const imgX = imgRect.left + window.scrollX;
            const imgY = imgRect.top + window.scrollY;

            const [x, y] = coords;
            const clickX = imgX + x;
            const clickY = imgY + y;

            const event = new MouseEvent('click', {
                clientX: clickX,
                clientY: clickY
            });

            const areaElement = document.elementFromPoint(clickX, clickY);
            areaElement.dispatchEvent(event);
        }
        
        clickOnArea(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, self.map_id, self.coords) 

    def click_on_button(self) -> None:
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "titulo"))
        )
        row_element = elements[2]
        row_element.click()


    def execute(self) -> None:
        self.open_page()
        self.click_on_map()
        self.click_on_button()
        input("")

inpi = Inpi()
inpi.execute()