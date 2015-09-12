#####################################################################
# Title: selectRandomNames.py                                       #
# Author: Scott Kleinman                                            #
# Contact: scott.kleinman@csun.edu                                  #
# Date September 11, 2015                                           #
# This work is licensed under a Creative Commons Attribution-       #
# NonCommercial-ShareAlike 4.0 International License:               #
# http://creativecommons.org/licenses/by-nc-sa/4.0/                 #
#####################################################################

# Python packages
import os, random, time, yaml

# Configuration values from config.yml file
config = yaml.safe_load(open("config.yml"))
active_list = config['active_list']
num_to_select = config['num_to_select']
save_selections = config['save_selections']
filter_saved = config['filter_saved']
save_filename = config['save_filename']
save_file_folder = config['save_file_folder']

# Main function
def selectRandomNames(names, num_to_select, save_file_path=""):
    # Check if the names list has less than the required number of entries 
    done = "There are not enough names in your list for you the number you have requested."
    if len(names) < num_to_select:
        return(done)
    else:
        # Choose random names    
        random_names = random.sample(names, num_to_select)

        # Add each name to the selected_names list
        selected_names = []
        for name in random_names:
            selected_names.append(name)
    
        # Filter saved selections
        if filter_saved == True and os.path.exists(save_file_path) == True:
            f = open(save_file_path, 'r')
            lines = f.readlines()
            f.close()
            saved_selections = []
            # Merge the lines into a single list
            for line in lines:
                # Get the name list
                #print(d)
                line = eval(line)
                #print(line['selected'])
                name_list = line["selected"]
                # Merge it with the running list
                saved_selections = list(set(saved_selections + name_list))
            # Remove saved selections from selected_names
            selected_names = set(selected_names) - set(saved_selections)
            # Get list of remaining names
            remaining = set(names) - set(selected_names)
        
        # Sort the selected names
        selected_names = sorted(selected_names)

        # Save the selections            
        if save_selections == True and len(selected_names) > 0:
            with open(save_file_path, 'a') as f:
                now = time.strftime("%c")
                entry = {"selected": selected_names, "timestamp": now}
                with open(save_file_path, 'a') as f:
                    f.write(str(entry) + '\n')

        # Check if the names list has been emptied
        if len(selected_names) == 0:
            done = "There are no names remaining in your list."
            return(done)

        # Check if the names list has less than the required number of entries
        elif len(remaining) < num_to_select:
            remainingItems = ', '.join(sorted(remaining))
            done = "There are only " + str(len(remaining)) + " items left: " + remainingItems + "." 
            return(done)

        else:
            # Return the random names
            return selected_names

######################################
# Select random names and print them #
######################################
save_file_path = os.path.join(save_file_folder, save_filename)
randomNames = selectRandomNames(active_list, num_to_select, save_file_path)
print('Random Names: ' + str(randomNames))