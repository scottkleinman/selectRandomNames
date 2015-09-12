#selectRandomNames.py
Author: Scott Kleinman

Date: September 12, 2015

## Introduction
`selectRandomNames.py` is a short Python script I wrote to choose random names of students in my classes. It works with any list of items. For instance, I sometimes feed it the days of the week in order to select random days for quizzes. In principle, it's not really all that more effective than closing my eyes and pointing to items on a list, but it seems to be more fun and motivating. It definitely feels like less work.

## Usage
Start by setting the configuration in the `config.yml` file, which must be in the same folder as `selectRandomNames.py` (unless you change the path in the main script). There are six settings:

###`active_list`###
This is the list of names or other items you are submitting to the script. The format must be a Python list, that is, comma-separated values in quotation marks (unless the items are numbers) between square brackets. The sample `config.yml` file shows the format. The sample configuration file also has some other short lists. This shows that you can keep multiple lists in the file and activate whichever one you want to use by giving it the `active_list` key.

###`num_to_select`###
This is the number of items you wish to select from the list. The default is 1 item, which will choose one random item from the active list.

###`save_selections`###
If you change the default setting `False` to `True`, the list of selected items will be saved to a text file with the name you supply in the `save_filename` setting. The list is saved in a JSON string containing a timestamp. If you run the script multiple times, a new JSON string will be created on a new line.

###`filter_saved`###
If you change the default setting `False` to `True`, the lists of selected items saved to your text file will be merged into a single list. Any names in this list are filtered from the random name selections. If merging all the names stored in the text file is not what you want, edit the text file in advance or use multiple text files for different purposes.

###`save_filename`###
This is the name of the text file you wish to create for saving and filtering selected names.

###`save_file_folder`###
This is the path to the folder that will contain the text file with the selections you save. It does not need to be in the same location as the main script.

## Note:
Saving and filtering previous selections may reduce your name list to below the number you have set as the number of random choices. If this is the case, the script will warn you and return smaller numbers on repeated runs until all names in your list are exhausted.

Last Update: September 12, 2015

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License: http://creativecommons.org/licenses/by-nc-sa/4.0/.