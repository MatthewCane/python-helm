from python_helm.python_helm import Python_helm


def test_env():
    helm = Python_helm()
    helm.env()


def test_version():
    helm = Python_helm()
    helm.version()
