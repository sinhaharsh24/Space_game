from cx_Freeze import setup, Executable

# Dependencies (Optional: Add if needed)
build_options = {
    'packages': [],
    'excludes': [],
}

setup(
    name="SpaceGame",
    version="1.0",
    description="Space Game",
    options={"build_exe": build_options},
    executables=[Executable("SPACEGAME.py")]  # Replace with your main Python file name
)
