class Antibiotics:
    PERMITTED_ANIMALS = ["bovino", "porcino", "caprino"]
    
    def __init__(self, product_name: str, dose, price: float, animals_for_dose: str):
        self.product_name = product_name
        self.dose = dose
        self.price = price
        self.animals_for_dose = animals_for_dose
        self.numberOfProducts = {}

    
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El nombre del producto debe ser una cadena no vacía.")
        self._product_name = value

   
    @property
    def dose(self):
        return self._dose

    @dose.setter
    def dose(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("La dosis debe ser un número entero.")
        
        if not (400 <= value <= 600):
            raise ValueError("La dosis debe estar entre 400 y 600 kilogramos.")
        self._dose = value

   
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("El precio debe ser un número mayor que 0.")
        self._price = value


    @property
    def animals_for_dose(self):
        return self._animals_for_dose

    @animals_for_dose.setter
    def animals_for_dose(self, value):
        if value not in self.PERMITTED_ANIMALS:
            raise ValueError(f"Animal no permitido. Los animales permitidos son: {', '.join(self.PERMITTED_ANIMALS)}.")
        self._animals_for_dose = value

