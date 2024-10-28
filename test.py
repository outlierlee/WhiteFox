import os

# Define the main directory containing the files
main_directory = 'Requirements-new/llvm/req'

# Walk through the directory and all its subdirectories
for dirpath, dirnames, filenames in os.walk(main_directory, topdown=False):
    # Rename directories
    for dirname in dirnames:
        old_dir = os.path.join(dirpath, dirname)
        new_dir = os.path.join(dirpath, dirname + 'Pass')
        # Rename the directory
        os.rename(old_dir, new_dir)
        print(f'Renamed directory: {old_dir} to {new_dir}')

    # Rename files
    for filename in filenames:
        if filename.endswith('_1.txt') or filename.endswith('_1.py'):  # Check for specific file types
            new_filename = filename.replace('_1', 'Pass_1')
            old_file = os.path.join(dirpath, filename)
            new_file = os.path.join(dirpath, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed file: {old_file} to {new_file}')
