import lifeeasy
import filecenter

def start():
    lifeeasy.clear()
    first_confirmation()

def first_confirmation():
    print('Make sure to have uploaded your package to GitHub')
    lifeeasy.sleep(1)
    print('Make sure to make a release of this package on GitHub')
    lifeeasy.sleep(1)
    print('')
    print('')
    input('Press [enter] to coninue...')
    setup()

def confirmation():
    input('Press [enter] to coninue...')

def setup():
    if filecenter.exists(lifeeasy.working_dir() + '/setup.py'):
        print('setup.py detected')
    else:
        setup = []
        
        # NAME
        name = input("What's the name of your package? ")
        print('')

        # VERSION
        version = input("What's the version of " + name)
        print('')
        
        # DESCRIPTION
        print('Write a little summary/description of ' + name)
        desc = input('> ')
        print('')
        
        # AUTHOR
        author = input('Who is the author? ')
        print('')
        
        # EMAIL
        email = input('What is his ' + author + "'s email? ")
        print('')

        # LICENSE
        print('Warning: the license name is case-sensitive!')
        package_license = input('What is the license for ' + name + ' ? ')
        package_license_classifier = 'License :: OSI Approved :: ' + package_license + ' License'
        print('')

        # GITHUB REPO
        print("What is the GitHub repository for this package?") 
        url = input('> ')
        print('')
        
        # ARCHIVE
        if url[-1] == '/':
            download_url_try = url + 'archive/' + version + '.tar.gz'
        else:
            download_url_try = url + '/archive/' + version + '.tar.gz'
        request = lifeeasy.request(method='get', url=download_url_try)
        if request.status_code == 200:
            download_url = download_url_try
        else:
            github_release = input("What is the name of the GitHub release? ")
            print('')
        if url[-1] == '/':
            download_url_try = url + 'archive/' + github_release + '.tar.gz'
        else:
            download_url_try = url + '/archive/' + github_release + '.tar.gz'
        request = lifeeasy.request(method='get', url=download_url_try)
        if request.status_code == 200:
            download_url = download_url_try
        else:
            def ask_for_github_release():
                global download_url
                print('What is the URL of your GitHub release? (it ends with .tar.gz)')
                download_url_try = input('> ')
                print('')
                request = lifeeasy.request(method='get', url=download_url_try)
                if request.status_code == 200:
                    download_url = download_url_try
                else:
                    print("It seems that you mistyped the URL or that the repository is private...")
                    lifeeasy.sleep(2)
                    print("Please put your GitHub repository visibility in public and retry...")
                    print('')
                    lifeeasy.sleep(2)
                    ask_for_github_release()
            ask_for_github_release()

        # KEYWORDS
        print('Enter a comma-separated list of keywords for your package')
        keywords = input('> ')
        keywords = keywords.split(',')
        print('')

        # DEPENDENCIES
        print('Enter a comma-separated list of dependencies for your package')
        dependencies = input('> ')
        dependencies = dependencies.replace(' ', '')
        dependencies = dependencies.split(',')
        print('')


        # PYTHON VERSIONS
        print('Enter a comma-separated list of supported Python version numbers for this package')
        print('(i.e 3,3.4,3.5,3.6,3.7,3.8)')
        python_versions = input('> ')
        print('')
        python_versions = python_versions.replace(' ', '')
        python_versions = python_versions.split(',')

        versions_classifiers = []
        for version in python_versions:
            versions_classifiers.append('Programming Language :: Python :: ' + version)


        # README

        if filecenter.exists(lifeeasy.working_dir() + '/README.md'):
            from os import path
            this_directory = path.abspath(path.dirname(__file__))
            with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
                long_description = f.read()

            long_description_type = 'text/markdown'
        
        elif filecenter.exists(lifeeasy.working_dir() + '/readme.md'):
            from os import path
            this_directory = path.abspath(path.dirname(__file__))
            with open(path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
                long_description = f.read()
            
            long_description_type = 'text/markdown'
        
        # Need to add more readme
        
        dev_status = 'Development Status :: 4 - Beta'
        def development_status():
            global dev_status
            lifeeasy.clear()
            print('Choose a development status from the following')
            print('')
            print('Alpha')
            print('Beta')
            print('Stable')
            print('')
            print('Or press [enter] to add a custom one when adding classifiers...')
            print('')
            print('')
            dev_status_try = input('> ')

            if dev_status_try.lower() == 'alpha':
                dev_status = 'Development Status :: 3 - Alpha'
            elif dev_status_try.lower() == 'beta':
                dev_status = 'Development Status :: 4 - Beta'
            elif dev_status_try.lower() == 'stable':
                dev_status = 'Development Status :: 5 - Production/Stable'
            else:
                print("Sorry but I couldn't recognize the status.")
                lifeeasy.sleep(1)
                print('Please try again...')
                lifeeasy.sleep(1)
                development_status()
        development_status()

        custom_classifiers = []
        lifeeasy.clear()
        print("What are the custom classifiers that you want to add?")
        print('')
        print("You need to enter your classifiers one-by-one")
        print("You need to write the full classifier")
        print("When you are done press [enter] again without entering anything.")
        print('')
        print('')
        user_choice = input('> ')
        custom_classifiers.append(user_choice)
        while user_choice != '':
            lifeeasy.clear()
            print("What are the custom classifiers that you want to add?")
            print('')
            print("You need to enter your classifiers one-by-one")
            print("You need to write the full classifier")
            print("When you are done press [enter] again without entering anything.")
            print('')
            print('')
            user_choice = input('> ')
            custom_classifiers.append(user_choice)
        
        lifeeasy.clear()
        lifeeasy.display_title('Building your setup file')
        display_body = ['Initializing']
        lifeeasy.display_body(display_body)
        lifeeasy.display(wait=0.5)

        display_body.append('adding imports')
        lifeeasy.display_body(display_body)
        setup.append('from setuptools import setup')

        display_body.append('creating the setup class')
        lifeeasy.display_body(display_body)
        setup.append('setup(')

        display_body.append('adding the package name')
        lifeeasy.display_body(display_body)
        setup.append('name = ' + name + ',')

        display_body.append('adding the package version')
        lifeeasy.display_body(display_body)
        setup.append('version = ' + version + ',')
        
        display_body.append('adding the package license')
        lifeeasy.display_body(display_body)
        setup.append('license = ' + package_license + ',')
        
        display_body.append('adding the package description')
        lifeeasy.display_body(display_body)
        setup.append('description = ' + desc + ',')
        
        display_body.append('adding the package author')
        lifeeasy.display_body(display_body)
        setup.append('author = ' + author + ',')
        
        display_body.append('adding the package email')
        lifeeasy.display_body(display_body)
        setup.append('author_email = ' + email + ',')
        
        display_body.append('adding the package url')
        lifeeasy.display_body(display_body)
        setup.append('url = ' + url + ',')
        
        display_body.append('adding the package download url')
        lifeeasy.display_body(display_body)
        setup.append('download_url = ' + download_url + ',')
        
        display_body.append('adding the package keywords')
        lifeeasy.display_body(display_body)
        setup.append('keywords = ' +  str(keywords) + ',')
        
        display_body.append('adding the package dependencies')
        lifeeasy.display_body(display_body)
        setup.append('install_requires = ' + str(dependencies) + ',')

        display_body.append('creating the package classifiers')
        lifeeasy.display_body(display_body)
        classifiers = []
        classifiers.append(dev_status)
        classifiers.append(package_license_classifier)
        classifiers.extend(versions_classifiers)
        classifiers.extend(custom_classifiers)

        display_body.append('adding the package classifiers')
        lifeeasy.display_body(display_body)
        setup.append('classifiers = ' + str(classifiers) + ',')

        display_body.append('adding the package readme')
        lifeeasy.display_body(display_body)
        setup.append('long_description = ' + long_description + ',')
        
        display_body.append('adding the package readme type')
        lifeeasy.display_body(display_body)
        setup.append('long_description_content_type = ' + long_description_type)

        display_body.append('finishing...')
        lifeeasy.display_body(display_body)
        setup.append(')')

        display_body.append('creating the file...')
        lifeeasy.display_body(display_body)
        lifeeasy.write_file('setup.py', setup)