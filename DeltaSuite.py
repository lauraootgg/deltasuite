import os
import shutil
import tempfile
import logging

def clear_temp_files():
    """
    Clears temporary files from the system's temporary directory.
    """
    temp_dir = tempfile.gettempdir()
    logging.info(f"Clearing temporary files from {temp_dir}")
    
    try:
        for root, dirs, files in os.walk(temp_dir):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    os.remove(file_path)
                    logging.info(f"Removed file: {file_path}")
                except Exception as e:
                    logging.error(f"Failed to remove file: {file_path} - {e}")

            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    shutil.rmtree(dir_path)
                    logging.info(f"Removed directory: {dir_path}")
                except Exception as e:
                    logging.error(f"Failed to remove directory: {dir_path} - {e}")
    except Exception as e:
        logging.error(f"Error while clearing temporary files: {e}")

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("DeltaSuite: Starting temporary files cleanup")
    clear_temp_files()
    logging.info("DeltaSuite: Temporary files cleanup completed")

if __name__ == "__main__":
    main()