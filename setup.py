import os
from setuptools import setup, find_packages
from setuptools.command.install import install

# Custom install class
class CustomInstallCommand(install):
    def run(self):
        # Stylish message
        print("\n" + "="*50)
        print("🔥 MediaMagic 🔥")
        print("Created by: Codetech")
        print("GitHub: https://github.com/ShUBHaMJHA9/mediamagic")
        print("="*50 + "\n")
        
        # Proceed with the standard installation
        super().run()

# Read README.md
current_dir = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(current_dir, "README.md")

# Ensure README file exists before trying to read
if os.path.exists(readme_path):
    with open(readme_path, encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = "A powerful and extensible all-media downloader for videos, audio, and more."

# Setup configuration
setup(
    name="MediaMagic",
    version="0.1.0",
    author="Codetech",
    author_email="admin@codetech",
    description="A powerful and extensible all-media downloader for videos, audio, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShUBHaMJHA9/mediamagic",
    packages=find_packages(),
    install_requires=[
        "yt-dlp>=2023.3.3",
        "requests>=2.26.0",
        "ffmpeg-python>=0.2.0",
        "beautifulsoup4>=4.10.0",
        "spotipy>=2.20.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Sound/Audio",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    keywords="media downloader audio video youtube tiktok terabox instagram dailymotion spotify",
    license="MIT",
    entry_points={
        "console_scripts": [
            "mediamagic=mediamagic.cli:main",  # If you have a cli main function
        ]
    },
    project_urls={
        "Documentation": "https://github.com/ShUBHaMJHA9/mediamagic/wiki",
        "Source": "https://github.com/ShUBHaMJHA9/mediamagic",
        "Tracker": "https://github.com/ShUBHaMJHA9/mediamagic/issues",
    },
    cmdclass={
        'install': CustomInstallCommand,  # Use the custom install command
    }
)
