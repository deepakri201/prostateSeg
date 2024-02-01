#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to generate test datalist for prostate158 dataset
Data should be organized in the following format:
    folder_to_parse/
        001/
            001_T2_axial.nii.gz
            001_ADC_resampled_to_T2_itk.nii.gz
            001_DWI_resampled_to_T2_itk.nii.gz
        002/
            002_T2_axial.nii.gz
            002_ADC_resampled_to_T2_itk.nii.gz
            002_DWI_resampled_to_T2_itk.nii.gz

Created on 02/01/2024

@author: bburton
"""
import os
import json

folder_to_parse = "/opt/prostate158/data/nii/"
# Write folder is desired name in output for datalist
write_folder_to_parse = "/prostate158/data/nii/"
output_path_datalist = "/opt/prostate158/monai_pcdetection_bundle/configs/datalist_ProstateX.json"

dirs = os.listdir(folder_to_parse)

list_of_images = []
for patient in dirs:
    # Parse dir
    if os.path.isdir(folder_to_parse + patient):
        print("Parsing folder: " + patient)
        # Parse files
        files = os.listdir(folder_to_parse + patient)
        files.sort()
        # Init list of 3 entries
        for file in files:
            if file.endswith(".nii.gz"):
                # Init json dict
                # {"image": ["dataset/024/024_t2.nii.gz", "dataset/024/024_adc.nii.gz", "dataset/024/024_dwi.nii.gz"]}
                # Ensure order is T2, ADC, DWI
                if "T2_axial" in file:
                    t2_path = write_folder_to_parse + patient + "/" + file
                elif "ADC_resampled_to_T2_itk" in file:
                    adc_path = write_folder_to_parse + patient + "/" + file
                elif "DWI_resampled_to_T2_itk" in file:
                    dwi_path = write_folder_to_parse + patient + "/" + file
        # When done parsing files, create entry
        json_entry = {"image": [t2_path, adc_path, dwi_path]}
        list_of_images.append(json_entry)

# When done parsing dirs, create json
json_data = {"testing": list_of_images}
print(json_data)
# Write output to file
with open(output_path_datalist, 'w') as outfile:
    json.dump(json_data, outfile)