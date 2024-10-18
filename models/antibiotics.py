class antibiotics:
    PERMITED_ANIMALS = ["bovino", "porcino", "caprino"]  
    
    def __init__(self, productName: str, dose, price: float, animalsForDose: str):
        
        try:
            dose = int(dose)  
        except ValueError:
            raise ValueError("La dosis debe ser un número entero.")
        
        if not (400 <= dose <= 600):
            raise ValueError("La dosis debe estar entre 400 y 600 kilogramos.")
        self.dose = dose

       
        if animalsForDose not in self.PERMITED_ANIMALS:
            raise ValueError(f"Animal no permitido. Los animales permitidos son: {', '.join(self.PERMITED_ANIMALS)}.")
        self.animalsForDose = animalsForDose

       
        if not isinstance(productName, str) or not productName:
            raise ValueError("El nombre del producto debe ser una cadena no vacía.")
        self.productName = productName

        
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("El precio debe ser un número mayor que 0.")
        self.price = price
