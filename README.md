# Folders Synchronization

## Description

This script provides a function to synchronize two folders on a regular interval. The script is designed to be run from the command line and takes four arguments: `source`, `replica`, `interval`, and `log`.

## Usage

The script can be run from the command line using the following format:
```
python main.py <source> <replica> <interval> <log>
```
where:
* `<source>` is the path to the source folder that you want to sync with the replica folder.
* `<replica>` is the path to the replica folder that you want to sync with the source folder.
* `<interval>` is the sync interval in seconds. The script will sync the folders at this interval.
* `<log>` is the path to the log file. The script will write logs to this file.
### Example Usage
```
python main.py /Users/user1/folder1 /Users/user2/folder2 60 /Users/user1/sync_logs.txt
```
This will synchronize the contents of `/Users/user1/folder1` with `/Users/user2/folder2` every 60 seconds, and write logs to `/Users/user1/sync_logs.txt`.

## Sync Folders GUI

This Python script provides a graphical user interface (GUI) for syncing two folders using the `sync_folders()` function from the `main.py` module.
### Dependencies
*  Python 3.6 or higher
*  `tkinter` package
*  `main.py` module
### How to Use
* Ensure all dependencies are installed.
* Run the script gui.py using the command python gui.py.
* Click on the `"Source Folder"` button to select the source folder.
* Click on the `"Replica Folder"` button to select the replica folder.
* Click on the `"Sync Folders"` button to start syncing the folders.
* Check the log file `sync.log` in the same directory as `gui.py` to view any changes made during the sync.

## License

This code is licensed under the MIT License. See the LICENSE file for more information.
