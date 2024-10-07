
import filecmp
import os
import shutil

import add_new_modules as add_new_modules


# test changing from modules to pipeline repo
def test_update_modules_json():
    shutil.copy('nf-microbe/test_data/modules.json.base', 'modules.json.test')
    add_new_modules.update_modules_json(module_name='b_test', modules_json='modules.json.test')
    assert filecmp.cmp('modules.json.test', 'nf-microbe/test_data/modules_test.json') == True
    os.remove('modules.json.test')

# test adding module to nf-core.yml
def test_add_module_to_nfcore_yml():
    shutil.copy('.nf-core.yml', '.nf-core.yml.test')
    add_new_modules.add_module_to_nfcore_yml(module_name='b_test', nfcore_yml='.nf-core.yml.test')
    with open('.nf-core.yml.test') as f:
        content = f.read()
    assert 'nf-core:\n      b_test: False' in content
    # os.remove('.nf-core.yml.test')

# test main function
def test_main():
    shutil.copy('.nf-core.yml', 'nf-microbe/test_data/.nf-core.yml')
    shutil.copy('nf-microbe/test_data/modules.json.base', 'nf-microbe/test_data/modules.json')
    add_new_modules.main(['-d', 'nf-microbe/test_data', '-m', 'b_test'])
    with open('nf-microbe/test_data/.nf-core.yml') as f:
        content = f.read()
    assert 'nf-core:\n      b_test: False' in content
    assert filecmp.cmp('nf-microbe/test_data/modules.json', 'nf-microbe/test_data/modules_test.json') == True
    os.remove('nf-microbe/test_data/.nf-core.yml')
    os.remove('nf-microbe/test_data/modules.json')
