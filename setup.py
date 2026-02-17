import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version = '0.0.0'

REPO_NAME = "KidneyTumorSegmentation"
AUTHOR_USER_NAME = "harithsya24"
SRC_REPO = "src"
AUTHOR_EMAIL = "amruthakravishankar@outlook.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version, 
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,  
    description="A Python package for Kidney Tumor Segmentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": SRC_REPO},
    packages=setuptools.find_packages(where=SRC_REPO)
)