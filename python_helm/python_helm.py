from subprocess import check_output as execute, CalledProcessError, STDOUT
from pathlib import Path
import json


class Python_helm:
    def __init__(self):
        print("> Installing dependences...")
        try:
            execute(
                "helm plugin install https://github.com/databus23/helm-diff",
                shell=True,
                stderr=STDOUT,
            )
        except CalledProcessError as e:
            err = str(e.output, "utf8")
            if err == "Error: plugin already exists\n":
                pass
            else:
                raise Exception("Failed to evaluate Helm extention dependency.")
        return

    def install(self):
        pass

    def env(self) -> dict:
        env = str(execute("helm env", shell=True), "utf8").splitlines()
        result = {}
        for line in env:
            result[line.split("=")[0]] = line.split("=")[1].replace('"', "")
        return result

    def version(self) -> dict:
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

    def list(self, namespace: str = "default") -> dict:
        result = json.loads(
            str(
                execute(f"helm list --namespace {namespace} --output json", shell=True),
                "utf8",
            )
        )
        return result

    def diff(
        self,
        release: str,
        chart: str,
        namespace: str = "default",
        output: str = "table",
    ) -> str:
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
