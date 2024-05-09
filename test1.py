# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    self.driver.get("http://127.0.0.1/Testing/formulario.html")
    self.driver.set_window_size(795, 703)
    self.driver.find_element(By.ID, "nombre").click()
    self.driver.find_element(By.ID, "nombre").send_keys("Daniel")
    self.driver.find_element(By.ID, "apellido").send_keys("Mangialavori")
    self.driver.find_element(By.ID, "dni").send_keys("31010654")
    self.driver.find_element(By.ID, "email").send_keys("danielmangialavori@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(21)").click()
    self.driver.find_element(By.ID, "fechadenacimiento").click()
    self.driver.find_element(By.ID, "fechadenacimiento").send_keys("0001-06-12")
    self.driver.find_element(By.ID, "fechadenacimiento").send_keys("0019-06-12")
    self.driver.find_element(By.ID, "fechadenacimiento").send_keys("0198-06-12")
    self.driver.find_element(By.ID, "fechadenacimiento").send_keys("1988-06-12")
    self.driver.find_element(By.ID, "Contrasena").click()
    self.driver.find_element(By.ID, "Contrasena").send_keys("Pedro")
    self.driver.find_element(By.ID, "Repetir").send_keys("Pwsro")
    self.driver.find_element(By.ID, "bici").click()
    self.driver.find_element(By.ID, "btn_register").click()
    assert self.driver.switch_to.alert.text == "Entro a la funcion"
    assert self.driver.switch_to.alert.text == "\r\n<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <script src=\"scripts.js\"></script>\r\n    <link rel=\"stylesheet\" href=\"estilo.css\">\r\n\r\n    <script\r\n  src=\"https://code.jquery.com/jquery-3.7.1.min.js\"\r\n  integrity=\"sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=\"\r\n  crossorigin=\"anonymous\"></script>\r\n\r\n  <script src=\"JS/funciones.js\"></script>\r\n</head>\r\n\r\n\r\n<body>\r\n\r\n\r\n<h1>Ejemplo de formulario en html</h1>\r\n\r\n\r\n<h3>Formulario de Login</h3>\r\n\r\n<div>\r\n\r\n<div>\r\n<form name=\"miform\" onsubmit=\"return validacion()\" method=\"post\">\r\n<label for=\"nombre\">Nombre: </label><br>\r\n<input type=\"text\" id=\"nombre\" name=\"nombre\"><br>\r\n<label for=\"apellido\">Apellido: </label><br>\r\n<input type=\"text\" id=\"apellido\"  name=\"apellido\"><br>\r\n<label for=\"dni\">DNI: </label><br>\r\n<input type=\"number\" id=\"dni\"  name=\"dni\"><br>\r\n<label for=\"e-mail\"> E-Mail: </label><br>\r\n<input type=\"email\" id=\"email\" name=\"email\"><br>\r\n<label for=\"text\"> Fecha de Nacimiento: </label><br>\r\n<input type=\"date\" id=\"fechadenacimiento\" name=\"fechadenacimiento\"><br>\r\n<label for=\"text\"> Contrasena: </label><br>\r\n<input type=\"password\" id=\"Contrasena\"  name=\"Contrasena\"><br>\r\n<label for=\"password\"> Repetir Contrasena: </label><br>\r\n<input type=\"password\" id=\"Repetir\"  name=\"Repetir\"><br>\r\n\r\n\r\n<label for=\"genero\">Genero: </label><br>\r\n<input type=\"radio\" id=\"\" value=\"Masculino\" name=\"genero\" checked > Masculino<br>\r\n<input type=\"radio\" id=\"\" value=\"Femenino\" name=\"genero\"> Femenino<br>\r\n<input type=\"radio\" id=\"\" value=\"Otro\" name=\"genero\"> Otro<br>\r\n<br>\r\n\r\n\r\n<label for=\"vehiculo\">Tipo de vehiculo: </label><br>\r\n<input type=\"checkbox\"  id=\"coche\" name=\"vehiculo\" value=\"Coche\"> Coche<br>\r\n<input type=\"checkbox\"  id=\"bici\" name=\"vehiculo\" value=\"Bicicleta\"> Bicicleta<br>\r\n\r\n\r\n<!--<input type =\"submit\" onclick=\"validacion()\">-->      \r\n\r\n<p id=\"Mensaje\"></p>\r\n\r\n<button type=\"button\" id=\"btn_register\" > Registrate </button>\r\n\r\n</div>\r\n</form>\r\n<div6>\r\n<img src=\"computadoras-1.jpeg\" width=\"400px\" height=\"310px\">\r\n</div6>\r\n</div>\r\n</body>\r\n</html>\r\n"
    assert self.driver.switch_to.alert.text == "Hola"
  
scrap = TestUntitled()
scrap.setup_method(self)
scrap.test_untitled()

