#!/usr/bin/env python3
"""
dznvBlox Build Script
Compiles dznvBlox into a standalone executable with all dependencies
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def clean_builds():
    """Remove old build artifacts."""
    print("[1/5] Cleaning old builds...")
    for folder in ['build', 'dist']:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    if os.path.exists('dznvBlox.spec'):
        os.remove('dznvBlox.spec')
    print("✓ Cleaned")

def install_dependencies():
    """Install required Python packages."""
    print("\n[2/5] Installing dependencies...")
    packages = ['psutil', 'requests', 'pillow', 'pyperclip', 'pyinstaller']
    for package in packages:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', package])
    print("✓ Dependencies installed")

def build_executable():
    """Build the PyInstaller executable."""
    print("\n[3/5] Building executable...")
    print("This may take a few minutes...")
    
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--windowed',
        '--icon=data/assets/mylogo.ico',
        '--name=dznvBlox',
        '--add-data', 'data:data',
        '--add-data', 'handle:handle',
        '--add-data', 'version:version',
        '--distpath=dist',
        '--workpath=build',
        'dznvBlox.pyw'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✓ Executable created: dist/dznvBlox.exe")
        return True
    else:
        print("✗ Build failed!")
        print(result.stderr)
        return False

def create_distribution():
    """Create distribution package with all required files."""
    print("\n[4/5] Creating distribution package...")
    
    release_dir = Path('dznvBlox-Release')
    if release_dir.exists():
        shutil.rmtree(release_dir)
    
    release_dir.mkdir()
    
    # Copy executable
    shutil.copy('dist/dznvBlox.exe', release_dir / 'dznvBlox.exe')
    
    # Copy data folders
    if Path('data').exists():
        shutil.copytree('data', release_dir / 'data')
    if Path('handle').exists():
        shutil.copytree('handle', release_dir / 'handle')
    if Path('version').exists():
        shutil.copytree('version', release_dir / 'version')
    
    # Copy documentation if it exists
    if Path('README.md').exists():
        shutil.copy('README.md', release_dir / 'README.md')
    if Path('LICENSE').exists():
        shutil.copy('LICENSE', release_dir / 'LICENSE')
    
    print(f"✓ Distribution package created: {release_dir}/")

def cleanup_artifacts():
    """Remove temporary build artifacts."""
    print("\n[5/5] Cleaning up build artifacts...")
    
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dznvBlox.spec'):
        os.remove('dznvBlox.spec')
    
    print("✓ Cleanup complete")

def main():
    """Main build process."""
    print("\n" + "="*50)
    print("dznvBlox Build Script")
    print("="*50)
    
    try:
        clean_builds()
        install_dependencies()
        
        if not build_executable():
            sys.exit(1)
        
        create_distribution()
        cleanup_artifacts()
        
        print("\n" + "="*50)
        print("Build Complete!")
        print("="*50)
        print("\nExecutable: dznvBlox-Release/dznvBlox.exe")
        print("Package:    dznvBlox-Release/")
        print("\nYou can now:")
        print("- Test: dznvBlox-Release/dznvBlox.exe")
        print("- Distribute: Zip the dznvBlox-Release folder")
        print()
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
