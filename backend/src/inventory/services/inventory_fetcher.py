from src.inventory.utils import InventoryDAO
from src.inventory.model import Inventory
from src.exceptions import UnregisteredBarcode
from src.common.helpers import BarcodeManager


class InventoryFetcher:
    def __init__(self, db_session):
        self.session = db_session
        self.barcode_manager = BarcodeManager(db_session)

    def find_by_barcode(self, barcode):
        """
          Finds a inventory by barcode and return InventoryDAO,
          if the barcode is unregistered raise UnregisteredBarcode exception

          :args
            :barcode(str): The invetory barcode
          returns: InventoryDAO
        """
        inventory = self.barcode_manager(barcode)

        return InventoryDAO(inventory)
