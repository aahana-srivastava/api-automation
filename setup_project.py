import os

def create_file(path):
    with open(path, 'w') as f:
        pass  # Create an empty file

def setup_project():
    # Create directories
    os.makedirs('tests', exist_ok=True)
    os.makedirs('utils', exist_ok=True)

    # Create files
    create_file('tests/__init__.py')
    create_file('tests/test_posts.py')
    create_file('tests/test_users.py')
    create_file('utils/__init__.py')
    create_file('utils/api_helper.py')
    create_file('config.py')
    create_file('requirements.txt')
    create_file('README.md')

    print("Project structure created successfully!")

if __name__ == "__main__":
    setup_project()