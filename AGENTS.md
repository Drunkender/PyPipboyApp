# PyPipboyApp - AI Agent Development Guide

## Project Overview

**PyPipboyApp** is an unofficial Fallout 4 Pip-Boy companion application written in Python 3 using PyQt6. It provides a customizable second-screen interface that mirrors the in-game Pip-Boy, allowing players to monitor game data, maps, inventory, and more without alt-tabbing.

### Key Characteristics
- **Version**: 0.9.0-alpha
- **Platform**: Cross-platform (Windows, Linux, Mac)
- **License**: GPL 3.0
- **Dependencies**: PyQt6, PyPipboy library
- **Python Version**: 3.13.5+
- **Architecture**: Modular widget-based system with plugin architecture

## Core Architecture

### Application Structure

```
PyPipboyApp/
├── pypipboyapp.py          # Main application entry point
├── dialogs/                # Connection and settings dialogs
├── widgets/                # Modular widget system
│   ├── shared/             # Shared utilities and base classes
│   └── [widget_name]/      # Individual widget modules
├── styles/                 # Qt stylesheet themes
├── ui/                     # Qt Designer UI files
└── utils/                  # Utility scripts
```

### Main Components

#### 1. Main Application (`pypipboyapp.py`)
- **PipboyMainWindow**: Main Qt window with dockable widget system
- **Application**: Core application logic, network management, widget loading
- Handles connection to Fallout 4 via PyPipboy library
- Manages widget lifecycle and data distribution

#### 2. Widget System
Each widget is a self-contained module with:
- `info.py`: Widget metadata and factory function
- Widget class inheriting from `widgets.WidgetBase`
- UI files (Qt Designer .ui files)
- Optional resources and additional Python files

#### 3. Data Flow
```
Fallout 4 → PyPipboy Library → PipboyDataManager → Widgets
```

## Development Guidelines

### Widget Development Pattern

#### Creating a New Widget

1. **Create widget directory** under `widgets/`
2. **Implement `info.py`**:
```python
from widgets import widgets
from .yourwidget import YourWidget

class ModuleInfo(widgets.ModuleInfoBase):
    LABEL = 'your_widget'        # Unique identifier
    NAME = 'Your Widget'         # Display name

    @staticmethod
    def createWidgets(handle, parent):
        return YourWidget(handle, parent)
```

3. **Implement widget class**:
```python
class YourWidget(widgets.WidgetBase):
    def __init__(self, mhandle, parent):
        super().__init__('Widget Title', parent)
        # Load UI
        uic.loadUi('widgets/your_widget/ui/yourwidget.ui', self)
        # Initialize widget-specific logic

    def init(self, framework, datamanager):
        super().init(framework, datamanager)
        # Connect to data updates
        # Set up event handlers
```

#### Widget Lifecycle
- `__init__`: Basic initialization, UI loading
- `init()`: Called after framework setup, connect to data sources
- `showEvent()`/`hideEvent()`: Handle visibility changes
- Data updates via `datamanager` signals

### Data Access Patterns

## 🧠 AI-Friendly Coding Practices

You provide code snippets and explanations that are explicitly optimized for clarity, review, and AI-assisted development:

1.  **Type Hinting:** **ALWAYS** add **typing annotations** to every function and class method, including explicit return types.
2.  **Docstrings (PEP 257):** **ALWAYS** include descriptive **docstrings** for all Python functions and classes, strictly adhering to the **PEP 257 convention** (e.g., using NumPy/Google style if multiline is needed).
3.  **Comments:** Preserve all existing in-line and block comments. Add necessary comments to explain complex logic or non-obvious design choices.


#### Accessing Game Data
```python
# Subscribe to data changes
self.datamanager.subscribe('PlayerInfo', self.onPlayerInfoUpdate)

def onPlayerInfoUpdate(self, data):
    # Process updated data
    self.updateUI(data)
```

#### Common Data Paths
- `PlayerInfo`: Player stats, location, etc.
- `Inventory`: Player inventory data
- `Map`: World map data
- `Quests`: Active quest information
- `Radio`: Radio station data

### UI/UX Guidelines

#### Qt Designer Usage
- Use Qt Designer for UI layouts
- Store .ui files in `widgets/[name]/ui/` directories
- Load UI files in widget `__init__` method

#### Styling
- Application supports Qt stylesheets
- Style directories in `styles/` with `style.qss` files
- Two example styles: `akPip-Green` and `qdarkstyle`

#### Responsive Design
- Widgets are dockable and resizable
- Support multiple screen configurations
- Consider both fullscreen and windowed modes

## Common Development Tasks

### Adding a New Widget

1. Analyze data requirements from PyPipboy documentation
2. Design UI mockup
3. Create widget directory structure
4. Implement widget class with data binding
5. Add to main widget registry (usually automatic)
6. Test with live game data

### Modifying Existing Widgets

1. Locate widget in `widgets/[name]/`
2. Examine `info.py` for entry point
3. Read existing widget implementation
4. Modify UI file or Python code as needed
5. Test changes with game connection

### Adding New Features

1. Identify which widget/component should handle the feature
2. Check available data from PyPipboy
3. Implement feature incrementally
4. Update UI to reflect new functionality
5. Test edge cases and error conditions

### Debugging Data Issues

1. Use Data Browser widget to inspect available data
2. Check PyPipboy library documentation
3. Add debug logging to widget data handlers
4. Verify data subscription patterns

## Testing Strategy

### Manual Testing
- Connect to running Fallout 4 instance
- Test widget functionality across different game states
- Verify UI responsiveness and data accuracy
- Test dockable widget behavior

### Development Testing
- Use mock data for UI development when game not available
- Test widget loading and initialization
- Verify error handling for disconnected states

## Code Quality Standards

### Python Best Practices
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Document complex logic with comments
- Handle exceptions gracefully

### Qt/PyQt6 Patterns
- Use signals/slots for event handling
- Avoid blocking operations on UI thread
- Clean up resources in widget destructors
- Follow Qt naming conventions

### Error Handling
- Gracefully handle disconnection from game
- Provide user feedback for error states
- Log errors for debugging
- Don't crash on malformed data

## Project Conventions

### File Organization
- One widget per directory under `widgets/`
- UI files in `ui/` subdirectory within widget
- Resources in `res/` subdirectory
- Follow existing naming patterns

### Import Style
```python
from PyQt6 import QtGui, QtWidgets, QtCore, uic
from widgets import widgets
from dialogs.connecthostdialog import ConnectHostDialog
```

### Naming Conventions
- Widget classes: `WidgetNameWidget`
- Dialog classes: `DialogNameDialog`
- Use descriptive, PascalCase class names
- Use snake_case for methods and variables

## Useful Resources

### External Documentation
- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Qt Stylesheets](https://doc.qt.io/qt-5/stylesheet.html)
- [PyPipboy Library](https://github.com/matzman666/PyPipboy)

### Internal Resources
- Widget examples in `widgets/` directory
- Style examples in `styles/` directory
- UI files provide layout examples

## Getting Started

1. **Setup Development Environment**
    - Install Python 3.13.5+, PyQt6, PyPipboy
    - Clone repository
    - Run `pypipboyapp.py` to verify setup

2. **Understand Data Flow**
   - Examine existing widgets for data access patterns
   - Use Data Browser widget to explore available data
   - Study PyPipboy documentation for data structures

3. **Start Small**
   - Begin with simple widget modifications
   - Add logging and debug output
   - Test incrementally with game connection

4. **Contribute Back**
   - Follow existing code patterns
   - Document new functionality
   - Test thoroughly before committing

This guide provides the foundation for AI agents to effectively contribute to PyPipboyApp development. The modular architecture and clear separation of concerns make it an excellent project for collaborative development.
