from pathlib import Path


CURRENT_PATH = Path(__file__).parent
PATH_WITH_FIXTURE = Path.joinpath(CURRENT_PATH, 'src', 'operations.json')
print('1111111111')
print(PATH_WITH_FIXTURE )