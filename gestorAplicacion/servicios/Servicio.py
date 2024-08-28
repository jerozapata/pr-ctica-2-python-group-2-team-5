#Importar lo necesario...
from abc import ABC, abstractmethod

#Clase abstracta Servicio que sirve de referencia para los demás servicios en el hospital
class Servicio(ABC):
    #Atributo de clase.
    generadorID = 1000

    #Inicializador.
    def __init__(self, paciente):
        self._paciente = paciente
        self._IDSERVICIO = self.generadorID + 1 #Corregir por si acaso
        self._estadoPago = False

    #Métodos.

    #Métodos abstractos a implementar por las subclases.
    @abstractmethod
    def validarPago(self, paciente, idServicio):
        pass

    @abstractmethod
    def descripcionServicio(self):
        pass

    #Método para realizar una busqueda de los servicios sin pagar por el paciente.
    @classmethod
    def obtenerServiciosSinPagar(cls, paciente):
        historiaClinicaPaciente = paciente.getHistoriaClinica()
        listaServicios = []

        listaServicios.extend(historiaClinicaPaciente.getHistorialCitas())
        listaServicios.extend(historiaClinicaPaciente.getListaFormulas())
        if paciente.getHabitacionAsignada() != None:
            listaServicios.append(paciente.getHabitacionAsignada())
        listaServicios.extend(historiaClinicaPaciente.getHistorialVacunas())

        for servicio in listaServicios:
            if servicio.isEstadoPago():
                listaServicios.remove(servicio)

        return listaServicios

    #Setters y getters
    def getPaciente(self):
        return self._paciente

    def setPaciente(self, paciente):
        self._paciente = paciente

    def getIdServicio(self):
        return self.IDSERVICIO

    def isEstadoPago(self):
        return self._estadoPago

    def setEstadoPago(self, estadoPago):
        self._estadoPago = estadoPago