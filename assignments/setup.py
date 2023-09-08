from setuptools import setup
from glob import glob
import os
package_name = 'assignments'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*')),
        (os.path.join('share', package_name), glob('urdf/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bhoys',
    maintainer_email='bhoys@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'numpublisher = assignments.num_publisher:main',
        'numcounter = assignments.num_counter:main',
        'turtle_controller = assignments.turtle_spawner:main',
        'lidar = assignments.lidar:main',
        ],
    },
)
