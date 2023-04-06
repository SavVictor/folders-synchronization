import os
import shutil
import time
import argparse


def sync_folders(source, replica, log_file):
    """
    Synchronizes the contents of two folders specified by the `source` and `replica` arguments.

    Parameters:
    source (str): The path to the source folder.
    replica (str): The path to the replica folder.
    log_file (str): The path to the log file.
    
    """
    
    # create replica folder if it doesn't exist
    if not os.path.exists(replica):
        os.mkdir(replica)
    
    # synchronize files
    for root, dirs, files in os.walk(source):
        for file in files:
            src_path = os.path.join(root, file)
            dest_path = src_path.replace(source, replica, 1)
            if not os.path.exists(dest_path) or \
                    os.stat(src_path).st_mtime - os.stat(dest_path).st_mtime > 1:
                shutil.copy2(src_path, dest_path)
                log(log_file, f"copied {src_path} to {dest_path}")

        for dir in dirs:
            src_path = os.path.join(root, dir)
            dest_path = src_path.replace(source, replica, 1)
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
                log(log_file, f"created directory {dest_path}")

    # remove files that don't exist in source
    for root, dirs, files in os.walk(replica):
        for file in files:
            src_path = os.path.join(root, file)
            dest_path = src_path.replace(replica, source, 1)
            if not os.path.exists(dest_path):
                os.remove(src_path)
                log(log_file, f"removed {src_path}")

        for dir in dirs:
            src_path = os.path.join(root, dir)
            dest_path = src_path.replace(replica, source, 1)
            if not os.path.exists(dest_path):
                os.rmdir(src_path)
                log(log_file, f"removed directory {src_path}")


def log(log_file, message):
    with open(log_file, "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    print(message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sync two folders.')
    parser.add_argument('source', type=str, help='path to source folder')
    parser.add_argument('replica', type=str, help='path to replica folder')
    parser.add_argument('interval', type=int, help='sync interval in seconds')
    parser.add_argument('log', type=str, help='path to log file')
    args = parser.parse_args()

    while True:
        sync_folders(args.source, args.replica, args.log)
        time.sleep(args.interval)
