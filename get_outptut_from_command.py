    roc_auc = subprocess.check_output("grep 'roc' "+file+" -A 100 | grep 'test_blend_all'| awk -F\" \" '{print $3}'", shell=True)
