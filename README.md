## Basic batcher
A batcher for Python.

<img src="https://github.com/hannesdelbeke/basic-batch/assets/3758308/137cd20d-cd19-42eb-915a-4fe2eacb970c" width="350" />

## Example
- You want to rename all meshes in Blender with a script. (Currently easier with Blender's native script editor)
- For each file in a folder, you want to open this scene, and check naming conventions.  

iter input:
```python
import pathlib;pathlib.Path("C:/my_folder").glob('**/*.blend')
```

script input: (pseudo code)
```python
import bpy

bpy.load_scene(str(item))
for obj in bpy.objects:
  print(obj) # TODO check if obj is named correctly
```

## TODO
- [ ] save job script, load job from file
- [ ] same for input / iter
- sample scenarios
  - validate scenes in a folder
  - validate scenes from a text file with scene paths
  - easily select different input configs
  - run from inside blender, validate multiple scenes. reuse existing blender for speed. if it crashes we lose progress.
  - run from outside blender, validate multiple scenes. open new blender for each
  - save progress to log
  
## Dev
ensure either PySide6 or 2 is installed

Don't edit `job_manager_ui.py`, edit `job_manager.ui` instead and build the ui with (PySide6)
```batch
cd batcher
pyside6-uic job_manager.ui -o job_manager_ui.py
```

