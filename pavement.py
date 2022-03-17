from paver.easy import *
from paver.setuputils import setup
import threading

feature_name = "demoqa"

setup(
    name="behave-browserstack",
    version="0.1.0",
    author="BrowserStack",
    author_email="support@browserstack.com",
    description="Behave Integration with BrowserStack",
    license="MIT",
    keywords="example selenium browserstack",
    url="https://github.com/browserstack/lettuce-browserstack",
    packages=['features']
)

# export variables to know what to execute
def run_behave_test(config, feature, task_id=0):
    sh(f'export CONFIG_FILE=config/{config}.json && export TASK_ID={task_id} && behave features/{feature}.feature')

# set up the task to run single or parallel
@task
@consume_nargs(1)
def run(args):
    if args[0] == 'single':
        run_behave_test(args[0], feature_name)
    else:
        jobs = []
        for i in range(4):
            thread = threading.Thread(target=run_behave_test, args=(args[0], feature_name, i))
            jobs.append(thread)
            thread.start()

        for th in jobs:
            th.join()

# set up the commands to run the tests by commandline
@task
def test():
    """Run all tests"""
    sh("paver run single")
    sh("paver run parallel")
