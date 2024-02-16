# QGIS Landsat8 Retrieval Plugin

This is a plugin for QGIS that enables the user to input latitude, longitude, dimension, and date to retrieve landsat8 imagery from NASA's API.

## Why?

This plugin expedites the process of importing landsat8 imagery directly to your QGIS project.

## How to use it?

1. Create a New Python Plugin Directory:

    Navigate to your QGIS plugin directory:
   
    Linux: ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
    Windows: C:\Users\USER\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\
    macOS: ~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/

    Create a new directory for your plugin (e.g., dataRetrieval).

3. Copy Plugin Files:

    Copy the following files to the newly created directory:
    mainPlugin.py: Contains the main functionality of the plugin.
    (Optional) metadata.txt: Contains metadata such as the plugin title and description.

4. Enable the Plugin in QGIS:

    Start QGIS and go to the "Plugins" menu.
    Select "Manage and Install Plugins..." to open the Plugin Manager.
    Enable the Data Retrieval Plugin from the list of available plugins.

5. Obtaining an API Key:

    Visit the NASA API Portal website.
    Sign up for an account or log in if you already have one.
    Once logged in, navigate to the API Key Management section.
    Generate a new API key by clicking on the "Generate API Key" button.
    Copy the generated API key to use it in the plugin.

6. Use the Plugin:

    Once enabled, you should see the "Retrieve Landsat 8 Imagery" button in your QGIS toolbar.
    If you don't see the toolbar, enable it in the QGIS settings: Settings > Toolbars > Plugins.

    Click on the "Retrieve Landsat 8 Imagery" button.

    Input latitude, longitude, dimension, date (YYYY-MM-DD), and the API key obtained in step 4.

    Customize Plugin Metadata and Code:

    Open the metadata.txt file and update the plugin title and description as desired.
    Open the mainPlugin.py file and start adding your own code to customize the plugin's functionality.
    You can modify parameters, add additional features, or enhance the user interface based on your requirements.

Enjoy!:

Have fun exploring and customizing your Data Retrieval Plugin to suit your needs. Experiment with different parameters and functionalities to make the most out of your Earth Observation data integration with QGIS.
