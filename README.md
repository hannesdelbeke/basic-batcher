## Basic batch
A simple batcher for Python.

Example:
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

<img src="https://github.com/hannesdelbeke/basic-batch/assets/3758308/137cd20d-cd19-42eb-915a-4fe2eacb970c" width="350" />

## TODO
- [ ] save job script, load job from file
- [ ] same for input / iter

## Dev
ensure either PySide6 or 2 is installed

Don't edit `job_manager_ui.py`, edit `job_manager.ui` instead and build the ui with (PySide6)
```batch
cd batcher
pyside6-uic job_manager.ui -o job_manager_ui.py
```

