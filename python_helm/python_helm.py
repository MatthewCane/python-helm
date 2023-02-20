from subprocess import check_output as execute
from pathlib import Path
import json


class Python_helm:
    def __init__(self):
        print("> Installing dependences...")
        execute("helm plugin install https://github.com/databus23/helm-diff")
        pass

    def install():
        pass

    def env() -> dict:
        env = str(execute("helm env", shell=True), "utf8").splitlines()
        result = {}
        for line in env:
            result[line.split("=")[0]] = line.split("=")[1].replace('"', "")
        return result

    def version() -> dict:
        version = (
            str(execute("helm version", shell=True), "utf8")
            .strip()
            .replace("version.BuildInfo", "")
            .replace("{", "")
            .replace("}", "")
            .split(",")
        )
        result = {}
        for item in version:
            result[item.split(":")[0]] = item.split(":")[1].replace('"', "")

        return result

    def list(namespace: str = "default") -> dict:
        result = json.loads(
            str(
                execute(f"helm list --namespace {namespace} --output json", shell=True),
                "utf8",
            )
        )
        return result

    def diff(
        release: str, chart: str, namespace: str = "default", output: str = "table"
    ):
        result = json.loads(
            str(
                execute(
                    f"helm diff upgrade --namespace {namespace} --output {output} {release} {chart}",
                    shell=True,
                ),
                "utf8",
            )
        )
        return result
