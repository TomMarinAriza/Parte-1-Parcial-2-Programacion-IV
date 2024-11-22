from models.client import Client 
from models.bill import Bill
class BillCRUD:
    def __init__(self):
        self._bills = [] 

    def create_bill(self, date, price, client):
        """
        Crea una nueva factura para un cliente específico.
        :param date: Fecha de la factura.
        :param price: Precio de la factura.
        :param client: Instancia de la clase Cliente que está asociada a la factura.
        """
        bill = Bill(date, price, client)
        self._bills.append(bill)
        return bill

    def read_bill(self, index):
        if 0 <= index < len(self._bills):
            return self._bills[index]
        else:
            raise IndexError("No existe una factura con ese índice.")

    def update_bill(self, index, date=None, price=None):
        if 0 <= index < len(self._bills):
            bill = self._bills[index]
            if date:
                bill.date = date
            if price:
                bill.price = price
            return bill
        else:
            raise IndexError("No existe una factura con ese índice.")

    def delete_bill(self, index):
        if 0 <= index < len(self._bills):
            self._bills.pop(index)
        else:
            raise IndexError("No existe una factura con ese índice.")

    def list_bills(self):
        return self._bills

    def add_product_to_bill(self, bill_index, product):
        if 0 <= bill_index < len(self._bills):
            bill = self._bills[bill_index]
            bill.addProduct(product)
        else:
            raise IndexError("No existe una factura con ese índice.")

    def remove_product_from_bill(self, bill_index, product):
        if 0 <= bill_index < len(self._bills):
            bill = self._bills[bill_index]
            bill.removeProduct(product)
        else:
            raise IndexError("No existe una factura con ese índice.")
