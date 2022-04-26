#!/usr/bin/python

import json
import os
import sys

config = sys.argv[-1]

# load json content from config file
def load_json():
    with open(config) as components:
        return json.load(components)

json = load_json()

# helper function for creating folders
def create_folder(folder_name,prev = None):
    if prev is None:
        new_folder_path = os.path.join(os.getcwd(),folder_name)
        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)
        return new_folder_path

    new_folder_pathh = os.path.join(prev,folder_name)
    if not os.path.exists(new_folder_pathh):
        os.mkdir(new_folder_pathh)

# create all the respective subfolders folders specified for each component
def create_directories():
    parent = create_folder(json['path'])
    for component in json['components']:
        create_folder(component,parent)


path = create_directories()


# react code template
code_template = """// libraries
import React from "react"

// other components

// style

// utils

const {} = () => {{
    return (
        <div>This is the {} component</div>
    );
}};

export default {};"""


# create javascript files in respective folders
# fill each file with code template
def create_js():
    for component in json['components']:
        filename = component.capitalize() + ".js"
        full_file_path = os.path.join("components",component,filename)
        with open(full_file_path,"w") as file:
            file.write(code_template.format(component.capitalize(),component,component.capitalize()))

create_js()

