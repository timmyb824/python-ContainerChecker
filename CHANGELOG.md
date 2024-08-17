# CHANGELOG



## v0.8.0 (2024-08-17)

### Feature

* feat: add timout to ssh connect and remove unused import ([`3295744`](https://github.com/timmyb824/python-ContainerChecker/commit/32957446bd72575efbaadf76f9f6e1b0fede9d46))

### Refactor

* refactor(test_ssh): Add timeout parameter to ssh client connection calls ([`9b7f222`](https://github.com/timmyb824/python-ContainerChecker/commit/9b7f2221c860a6103472f40f3ebb46d697ec9747))

### Unknown

* Merge pull request #10 from timmyb824/feat/add-ssh-timeout

feat/add ssh timeout ([`d1dba1b`](https://github.com/timmyb824/python-ContainerChecker/commit/d1dba1b7eda711bd36b7152400e976ae0e57730b))


## v0.7.0 (2024-08-08)

### Feature

* feat: Add version printing functionality and update dependencies to latest versions ([`8f5a7af`](https://github.com/timmyb824/python-ContainerChecker/commit/8f5a7af8a9a13a038f67553fe26867f3a19423d4))

### Unknown

* Merge pull request #9 from timmyb824/feat/add-version-command

feat: Add version printing functionality and update dependencies to latest versions ([`5f3e459`](https://github.com/timmyb824/python-ContainerChecker/commit/5f3e4598a8aedfc92e629aef07a859dd18183019))


## v0.6.0 (2024-08-08)

### Feature

* feat: Add default path for servers.yaml in argparse options ([`b8c232a`](https://github.com/timmyb824/python-ContainerChecker/commit/b8c232a64b1d11d727a8797c899597311251f7b7))

* feat: Add USER_HOME constant to store user&#39;s home directory ([`f1bd245`](https://github.com/timmyb824/python-ContainerChecker/commit/f1bd2452db2ba51a84103a6d25cae70381f10d23))

### Fix

* fix: add handling for key file not found and store the key file location ([`fd2f724`](https://github.com/timmyb824/python-ContainerChecker/commit/fd2f7247ff7778de67d90cae621f160be7307b62))

### Style

* style: update logging in config.py ([`176c92f`](https://github.com/timmyb824/python-ContainerChecker/commit/176c92f16de17ee9cc1a123de706b8808fe53e75))

### Unknown

* Merge pull request #8 from timmyb824/feat/improve-file-handling

improve handling of config and key file ([`ace12e9`](https://github.com/timmyb824/python-ContainerChecker/commit/ace12e9b1315c8088c4e1d90cca4c2d3a3f59a6c))


## v0.5.0 (2024-08-08)

### Feature

* feat: Fix incorrect decoding of SSH client response in container tests ([`82a2959`](https://github.com/timmyb824/python-ContainerChecker/commit/82a2959a529d7c57ccf70f88b29291022b0a3402))

* feat: Improve error handling and logging for container checking functions; add workaround for checking containers on a synologynas ([`16378ce`](https://github.com/timmyb824/python-ContainerChecker/commit/16378ceba4063de29d638115e45000ed0818c63f))

* feat: Add debug logging for container status on remote servers ([`c200dda`](https://github.com/timmyb824/python-ContainerChecker/commit/c200ddacffac1839b9d7551ff5ac7eaa200f6aea))

### Unknown

* Merge pull request #7 from timmyb824/feat/improve-logging-add-workaround

feat: improve logging for debugging and add workaround for containers on synology nas ([`f4ce706`](https://github.com/timmyb824/python-ContainerChecker/commit/f4ce706370bc4a0e3b72ffdeaac1028f9dd61789))


## v0.4.0 (2024-08-06)

### Feature

* feat: Introduce concurrent processing for server connections ([`fe3ca8e`](https://github.com/timmyb824/python-ContainerChecker/commit/fe3ca8e94b9b42bff74221ddeda3470e7d58910a))

### Unknown

* Merge pull request #6 from timmyb824/feat/speed-up-processing

feat: Introduce concurrent processing for server connections ([`17c79ea`](https://github.com/timmyb824/python-ContainerChecker/commit/17c79ea3adfedb1925581077e87b0582ee863c88))


## v0.3.0 (2024-08-06)

### Feature

* feat: add number of containers running to output ([`670e59f`](https://github.com/timmyb824/python-ContainerChecker/commit/670e59f8038fe58ac200bc32a0d5497a320f08d6))

### Unknown

* Merge pull request #5 from timmyb824/feat/add-ct-count

feat: add number of containers running to output ([`6ea3361`](https://github.com/timmyb824/python-ContainerChecker/commit/6ea33611df25b11e947f52ca08f4f8f1c3de517c))


## v0.2.3 (2024-08-06)

### Refactor

* refactor: Update import paths to containerchecker namespace ([`16ac1d9`](https://github.com/timmyb824/python-ContainerChecker/commit/16ac1d9beab9ca1338b1ebaae5fa0e4d02a90165))

### Unknown

* Merge pull request #4 from timmyb824/refactor/stop-using-src

refactor: Update import paths to containerchecker namespace ([`470087d`](https://github.com/timmyb824/python-ContainerChecker/commit/470087d145854be25d7392801b2b82a330e3525d))


## v0.2.2 (2024-08-06)

### Refactor

* refactor: Update imports in multiple files to include the correct path from src folder ([`82e9379`](https://github.com/timmyb824/python-ContainerChecker/commit/82e93797740df29cba2dde32a446b9b93310417c))

### Unknown

* Merge pull request #3 from timmyb824/fix/import-issue-again

refactor: Update imports in multiple files to include the correct path from src folder ([`2368ab2`](https://github.com/timmyb824/python-ContainerChecker/commit/2368ab2534d3e2b49efb395fd693dfd177880d4a))


## v0.2.1 (2024-08-06)

### Refactor

* refactor: Update imports to use relative import paths in containers, main, and ssh modules ([`20870b1`](https://github.com/timmyb824/python-ContainerChecker/commit/20870b1db6a5132cb7b9b0dbee7037c03a5c46ad))

* refactor: Rename function to improve clarity and consistency in naming conventions ([`a6abfce`](https://github.com/timmyb824/python-ContainerChecker/commit/a6abfce8f9c3ef56e2c4f3b08dd0b4a52a582ba2))

### Style

* style: Remove tabulate from dependencies and update rich version to &#34;^13.7.1&#34; ([`8eff971`](https://github.com/timmyb824/python-ContainerChecker/commit/8eff971f9a7d9619051ac82408a65135a89175ab))

### Unknown

* Merge pull request #2 from timmyb824/fix/import-issue

fix/import issue ([`d6d6c38`](https://github.com/timmyb824/python-ContainerChecker/commit/d6d6c3802ede83d7f4cfb7371147462eaad6f719))


## v0.2.0 (2024-08-06)

### Documentation

* docs: Add Pylint configuration file with rules and settings ([`0e1313e`](https://github.com/timmyb824/python-ContainerChecker/commit/0e1313e6a978dd6f66abe5d9c5791292be84117c))

### Feature

* feat: Add pcc script to run main function ([`565f905`](https://github.com/timmyb824/python-ContainerChecker/commit/565f905fb6449386541e7421722e20f370899817))

* feat: Add logging to SSH module for better error handling ([`3f5e5e5`](https://github.com/timmyb824/python-ContainerChecker/commit/3f5e5e5f3c2030343d41b64b36b3279b6d1dc12e))

* feat: Add constants module with rich console import ([`2e354c5`](https://github.com/timmyb824/python-ContainerChecker/commit/2e354c58acbcdf750416f1d16ef5dda5a24c192d))

* feat: Improve error handling and logging in read_yaml function ([`04bbe51`](https://github.com/timmyb824/python-ContainerChecker/commit/04bbe515bfbbbdc3ab630a8c6596564c8a9fe491))

* feat: Add argument parser for command line arguments ([`d15a661`](https://github.com/timmyb824/python-ContainerChecker/commit/d15a661a5c886076ce1167bae93a954578b03489))

* feat: Add function to set up logging configuration ([`61ad194`](https://github.com/timmyb824/python-ContainerChecker/commit/61ad1940034d20bd344ec702f2b9c4d0e9683aec))

* feat: Add rich library to project dependencies ([`75cde06`](https://github.com/timmyb824/python-ContainerChecker/commit/75cde065803d8b96a28226fe223051b0e145e6aa))

### Refactor

* refactor(containers): Improve logging and display functionality for running containers ([`9187007`](https://github.com/timmyb824/python-ContainerChecker/commit/91870075cb296775f9c08374ec81bd26ffe0aad7))

### Style

* style: Import library &#39;rich&#39; for pretty printing ([`2011045`](https://github.com/timmyb824/python-ContainerChecker/commit/2011045ed7c7f3ebe6d0bdd6fa17a7d70829d726))

### Unknown

* Merge pull request #1 from timmyb824/feat/add-new-features

docs: Add Pylint configuration file with rules and settings ([`1a187d2`](https://github.com/timmyb824/python-ContainerChecker/commit/1a187d25989da864b828704241fda2227629259d))


## v0.1.0 (2024-08-05)

### Chore

* chore: Update code formatting and remove unnecessary code duplication ([`d9c9ee8`](https://github.com/timmyb824/python-ContainerChecker/commit/d9c9ee83dd81c41a22f22acb7299ffa53d9617d6))

### Documentation

* docs: Add GNU General Public License v3 to the project ([`daa6469`](https://github.com/timmyb824/python-ContainerChecker/commit/daa6469b9c18841b8117c33a1728713ad80d6940))

### Feature

* feat: Add pre-commit configuration and Sourcery settings files ([`3987863`](https://github.com/timmyb824/python-ContainerChecker/commit/3987863acf2f528ef1271310d8f9754a3bee8083))


## v0.0.0 (2024-08-05)

### Chore

* chore: Remove unused test run step in CI workflow ([`141b31c`](https://github.com/timmyb824/python-ContainerChecker/commit/141b31c26bbdc46fd6b580d8ae4e4d2ee9a7ae09))

### Refactor

* refactor: Restructure main function into process_server for better readability and maintenance ([`66a6386`](https://github.com/timmyb824/python-ContainerChecker/commit/66a63862ec2e472393068200dd803910e9ff8138))

### Test

* test: Add unit tests for containers and ssh modules ([`01222d3`](https://github.com/timmyb824/python-ContainerChecker/commit/01222d3ce5824a849838b5c9be40e19added8e5c))

### Unknown

* init commit ([`0e50db8`](https://github.com/timmyb824/python-ContainerChecker/commit/0e50db8e05fb1e366eaca6e209d8f63c601683d8))
