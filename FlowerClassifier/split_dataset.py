import os
import shutil

data_dir = 'flowers_kaggle/Original/'
path_to_validate = 'flowers_kaggle/Validate/'
path_to_test = 'flowers_kaggle/Test/'
path_to_train = 'flowers_kaggle/Train/'

for path in [path_to_validate, path_to_test, path_to_train]:
    os.makedirs(path, exist_ok=True)

def split_and_move(class_name, counts):
    source_path = os.path.join(data_dir, class_name)
    validate_count, test_count, train_count = counts
    
    images = sorted([img for img in os.listdir(source_path) if img.lower().endswith(('.jpg', '.jpeg', '.png'))])
    
    dest_paths = {
        'validate': os.path.join(path_to_validate, class_name),
        'test': os.path.join(path_to_test, class_name),
        'train': os.path.join(path_to_train, class_name)
    }
    
    for path in dest_paths.values():
        os.makedirs(path, exist_ok=True)
    
    for i, img in enumerate(images):
        src_img_path = os.path.join(source_path, img)
        
        if i < validate_count:
            shutil.move(src_img_path, os.path.join(dest_paths['validate'], img))
        elif i < validate_count + test_count:
            shutil.move(src_img_path, os.path.join(dest_paths['test'], img))
        else:
            shutil.move(src_img_path, os.path.join(dest_paths['train'], img))

split_and_move('Daisy', (535, 115, 114))
split_and_move('Rose', (549, 118, 117))
split_and_move('Tulip', (689, 148, 147))
split_and_move('Dandelion', (737, 158, 157))
split_and_move('Sunflower', (514, 110, 109))

print("success!")
