import unittest
from unittest.mock import MagicMock
import sys
import os

# Add the project root to sys.path so we can import widgets
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock PyQt5
mock_qt = MagicMock()
mock_qt.QtWidgets = MagicMock()
mock_qt.QtCore = MagicMock()
mock_qt.QtGui = MagicMock()

# Mock QAbstractTableModel so inheritance works
class MockQAbstractTableModel:
    def __init__(self, parent=None):
        pass

    _signalItemUpdate = MagicMock()
    _signalSortedIdsUpdate = MagicMock()

    # We need to mock the signal connect methods
    def __getattr__(self, name):
         return MagicMock()

mock_qt.QtCore.QAbstractTableModel = MockQAbstractTableModel
mock_qt.QtCore.pyqtSignal = lambda *args: MagicMock()
# Mock pyqtSlot decorator
def mock_slot(*args):
    def decorator(func):
        return func
    return decorator
mock_qt.QtCore.pyqtSlot = mock_slot

# Mock enums
mock_qt.QtCore.Qt.DisplayRole = 0
mock_qt.QtCore.Qt.Horizontal = 1
mock_qt.QtCore.Qt.TextAlignmentRole = 2
mock_qt.QtCore.Qt.FontRole = 3
mock_qt.QtCore.Qt.AlignVCenter = 0
mock_qt.QtCore.Qt.AlignLeft = 0
mock_qt.QtCore.Qt.AlignRight = 0
mock_qt.QtCore.Qt.AlignCenter = 0

sys.modules['PyQt5'] = mock_qt
sys.modules['PyQt5.QtWidgets'] = mock_qt.QtWidgets
sys.modules['PyQt5.QtCore'] = mock_qt.QtCore
sys.modules['PyQt5.QtGui'] = mock_qt.QtGui

# Mock pypipboy
mock_pypipboy = MagicMock()
sys.modules['pypipboy'] = mock_pypipboy
sys.modules['pypipboy.inventoryutils'] = MagicMock()


from widgets.inventorybrowser.inventorymodel import CatAmmoModel, InventoryTableModel, CatAllModel

class TestInventoryDoubleClick(unittest.TestCase):
    def test_ammo_model_double_click_DOES_NOT_trigger_use(self):
        """
        Test that double-clicking on an item in a category where "Use" is disabled
        (like Ammo) does NOT trigger the rpcUseItem call.
        """
        # Setup
        model = CatAmmoModel()
        datamanager = MagicMock()
        item = MagicMock()
        view = MagicMock()

        # Pre-check: Verify that Use action is indeed disabled for CatAmmoModel
        is_enabled = model._cmIsUseActionEnabled(item, [item])
        self.assertFalse(is_enabled, "Use action should be disabled for Ammo")

        # Action: Double click
        model.itemDoubleClicked(datamanager, item, view)

        # Assertion: datamanager.rpcUseItem should NOT be called
        datamanager.rpcUseItem.assert_not_called()

    def test_all_model_double_click_DOES_trigger_use(self):
        """
        Test that double-clicking on an item in a category where "Use" is enabled
        (like All items) DOES trigger the rpcUseItem call.
        """
        # Setup
        model = CatAllModel()
        datamanager = MagicMock()
        item = MagicMock()
        view = MagicMock()

        # Pre-check: Verify that Use action is enabled for CatAllModel (default)
        is_enabled = model._cmIsUseActionEnabled(item, [item])
        self.assertTrue(is_enabled, "Use action should be enabled for AllModel by default")

        # Action: Double click
        model.itemDoubleClicked(datamanager, item, view)

        # Assertion: datamanager.rpcUseItem SHOULD be called
        datamanager.rpcUseItem.assert_called_with(item)

if __name__ == '__main__':
    unittest.main()
