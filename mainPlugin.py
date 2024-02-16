#-----------------------------------------------------------
# Copyright (C) 2024 Dylan Albrecht
#-----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#---------------------------------------------------------------------

from qgis.PyQt.QtWidgets import QAction, QMessageBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from qgis.core import QgsProject
from qgis.utils import iface

import requests

class DataRetrievalPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        # Create a new action to be added to the toolbar
        self.action = QAction('Retrieve Landsat 8 Imagery', self.iface.mainWindow())
        self.action.triggered.connect(self.open_dialog)
        
        # Add the action to the toolbar
        self.iface.addToolBarIcon(self.action)

    def open_dialog(self):
        # Create and open the parameter input dialog
        dialog = ParameterInputDialog(self.iface.mainWindow())
        dialog.exec_()

    def retrieve_imagery(self, lat, lon, dim, date, api_key):
        api_url = 'https://api.nasa.gov/planetary/earth/imagery'
        params = {
            'lat': lat,
            'lon': lon,
            'dim': dim,
            'date': date,
            'api_key': api_key
        }

        try:
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                data = response.json()
                image_url = data.get('url')
                msg_box = QMessageBox()
                msg_box.setWindowTitle('Landsat 8 Imagery')
                msg_box.setText(f'Landsat 8 image retrieved successfully.\nImage URL: {image_url}')
                msg_box.exec_()
            else:
                error_message = f'Error: {response.status_code} - {response.reason}'
                QMessageBox.critical(None, 'Data Retrieval Error', error_message)
        except Exception as e:
            QMessageBox.critical(None, 'Data Retrieval Error', str(e))

    def unload(self):
        # Remove the plugin icon from the toolbar
        self.iface.removeToolBarIcon(self.action)

class ParameterInputDialog(QDialog):
    def __init__(self, parent=None):
        super(ParameterInputDialog, self).__init__(parent)
        self.setWindowTitle('Enter Parameters')
        layout = QVBoxLayout()

        # Latitude input
        self.lat_label = QLabel('Latitude:')
        self.lat_input = QLineEdit()
        layout.addWidget(self.lat_label)
        layout.addWidget(self.lat_input)

        # Longitude input
        self.lon_label = QLabel('Longitude:')
        self.lon_input = QLineEdit()
        layout.addWidget(self.lon_label)
        layout.addWidget(self.lon_input)

        # Dimension input
        self.dim_label = QLabel('Dimension:')
        self.dim_input = QLineEdit()
        layout.addWidget(self.dim_label)
        layout.addWidget(self.dim_input)

        # Date input
        self.date_label = QLabel('Date (YYYY-MM-DD):')
        self.date_input = QLineEdit()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)

        # API key input
        self.api_key_label = QLabel('API Key:')
        self.api_key_input = QLineEdit()
        layout.addWidget(self.api_key_label)
        layout.addWidget(self.api_key_input)

        # Submit button
        submit_button = QPushButton('Retrieve Imagery')
        submit_button.clicked.connect(self.submit_parameters)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def submit_parameters(self):
        lat = self.lat_input.text()
        lon = self.lon_input.text()
        dim = self.dim_input.text()
        date = self.date_input.text()
        api_key = self.api_key_input.text()

        plugin_instance = DataRetrievalPlugin(iface)
        plugin_instance.retrieve_imagery(lat, lon, dim, date, api_key)
        self.close()

# Initialize the plugin when QGIS starts
def initPlugin(iface):
    global data_retrieval_plugin
    data_retrieval_plugin = DataRetrievalPlugin(iface)

# Clean up the plugin when QGIS exits
def unloadPlugin(iface):
    global data_retrieval_plugin
    del data_retrieval_plugin
