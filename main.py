
import os
from tqdm import tqdm
from utils import save_image_multiple_times, run_image_harmonization, transfer_and_rename_images


base_dir = "test_images"
ad_dir = "product_ad"
mask_dir = "mask/mask.png"
out_harmonized_dir = "faster_harmonizer"
dirs = os.listdir(base_dir)

for dir in tqdm(dirs):
    # move images to demo folder
    input_folder = os.path.join(base_dir, dir ,ad_dir)
    output_folder = "demo/image_harmonization/example/composite"
    new_names = ["1.png","2.png","3.png","4.png"]
    transfer_and_rename_images(input_folder, output_folder, new_names)

    # move masks to demo folder
    mask_point_dir = os.path.join(base_dir, dir, mask_dir)
    mask_out_folder = "demo/image_harmonization/example/mask"
    save_image_multiple_times(mask_point_dir,mask_out_folder,new_names)
    run_image_harmonization()

    # move results back
    output_folder = os.path.join(base_dir, dir ,out_harmonized_dir)
    input_folder = "demo/image_harmonization/example/harmonized"
    new_names = ["1.png","2.png","3.png","4.png"]
    transfer_and_rename_images(input_folder, output_folder, new_names)
