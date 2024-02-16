# QGIS Landsat8 Imagery Retrieval Plugin

## Description
This plugin allows users to import Landsat 8 imagery from NASA's API directly into their QGIS project based on input latitude, longitude, dimension, and date (YYYY-MM-DD).

## Why?
This plugin expedites the process of importing Landsat 8 imagery into your QGIS project.

## How to Use:
1. **Create a New Python Plugin Directory:**
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/minimal`
   - Windows: `C:\Users\USER\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\minimal`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/minimal`

2. **Copy Plugin Files:**
   - Copy the following files to the newly created directory:
     - `mainPlugin.py`: Contains the main functionality of the plugin.
     - (Optional) `metadata.txt`: Contains metadata such as the plugin title and description.

3. **Enable the Plugin in QGIS:**
   - Start QGIS and go to the "Plugins" menu.
   - Select "Manage and Install Plugins..." to open the Plugin Manager.
   - Enable the Data Retrieval Plugin from the list of available plugins.

4. **Obtain an API Key:**
   - **Create a NASA Developer Account:**
     - Go to the [NASA API Portal](https://api.nasa.gov/).
     - Click on the "Sign Up" button to create a new account.
     - Fill in the required information to register for a developer account.
   - **Verify Your Email:**
     - After signing up, you will receive an email from NASA to verify your email address.
     - Click on the verification link provided in the email to verify your email address.
   - **Generate an API Key:**
     - Once your email is verified, log in to your NASA Developer account.
     - Navigate to the API Keys section.
     - Click on the "Generate API Key" button.
     - Provide a name for your API key (e.g., "QGIS Landsat 8 Retrieval Plugin").
     - Submit the form to generate your API key.
   - **Access Your API Key:**
     - After generating the API key, you will be provided with an API key string.
     - Copy this API key and securely store it, as you will need it to authenticate your requests to the NASA APIs.

5. **Use the Plugin:**
   - Once enabled, you should see the "Retrieve Landsat 8 Imagery" button in your QGIS toolbar.
   - If you don't see the toolbar, enable it in the QGIS settings: Settings > Toolbars > Plugins.

6. **Customize Plugin Metadata and Code:**
   - Open the `metadata.txt` file and update the plugin title and description as desired.
   - Open the `mainPlugin.py` file and start adding your own code to customize the plugin's functionality.
   - You can modify parameters, add additional features, or enhance the user interface based on your requirements.

## Enjoy!
Have fun exploring and customizing your Data Retrieval Plugin to suit your needs. Experiment with different parameters and functionalities to make the most out of your Earth Observation data integration with QGIS.
