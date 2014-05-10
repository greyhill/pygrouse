from distutils.core import setup

setup(
        name = 'pygrouse',
        version = '0.0.1',
        author = 'Madison McGaffin',
        author_email = 'greyhill@gmail.com',
        packages = ['grouse'],
        url = 'http://github.com/greyhill/pygrouse',
        description = 'GROUSE subspace estimation and tracking algorithm',
        install_requires = [
            'numpy'
        ]
    )

