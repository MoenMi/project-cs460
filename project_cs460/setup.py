from setuptools import setup

package_name = 'project_cs460'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/bruno-business-library.wbt']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/tuscaloosa.wbt']))
data_files.append(('share/' + package_name + '/textures', ['textures/bookshelf.png']))
data_files.append(('share/' + package_name + '/resource', ['resource/my_robot.urdf']))
data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Michael Moen',
    maintainer_email='mtmoen@crimson.ua.edu',
    description='Simulations for CS 460: Autonomous Robotics at the University of Alabama',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_robot_driver = project_cs460.my_robot_driver:main',
        ],
    },
)