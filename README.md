# clean-recycle-bin-downloads-temp-folders 
simple script that deletes everything in the users downloads and temp folder. Also cleans recycle bin.

# Windows Automation:
1. Open Task Scheduler
2. Click **Create Task..** on the right side of Task Scheduler
3. Give it a name and optionally a description. 
    - If you want to delete absolutely everything check the box next to **Run with highest privileges**
4. On the **trigger** tab you can set at what times you want the script to run.
5. Open **actions** click new
   - Under **Program/script** enter your python location, this can be found by typing: 
   `python -c "import sys; print(sys.executable)"` in the command prompt.
   - In **Add arguments** enter your script name (CleanWindows.py if not changed)
   - in **Start in** enter the location of your python script.
  

