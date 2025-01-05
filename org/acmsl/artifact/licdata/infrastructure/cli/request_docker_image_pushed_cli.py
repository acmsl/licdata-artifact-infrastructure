# vim: set fileencoding=utf-8
"""
org/acmsl/artifact/licdata/infrastructure/cli/request_docker_image_pushed_cli.py

This file defines the RequestDockerImagePushedCli class.

Copyright (C) 2024-today acmsl's Licdata Artifact Infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from argparse import ArgumentParser
from pythoneda.shared import PrimaryPort, PythonedaApplication
from pythoneda.shared.infrastructure.cli import CliHandler


class RequestDockerImagePushedCli(CliHandler, PrimaryPort):
    """
    A PrimaryPort used to request pushing the Docker image.

    Class name: RequestDockerImagePushedCli

    Responsibilities:
        - Parse the command-line to retrieve the push request.

    Collaborators:
        - org.acmsl.artifact.licdata.application.LicdataIacApp: It's notified back with the information retrieved from the command line.
    """

    def __init__(self):
        """
        Creates a new RequestDockerImagePushedCli instance.
        """
        super().__init__("Provide the Docker image options")

    @classmethod
    def priority(cls) -> int:
        """
        Retrieves the priority of this port.
        :return: The priority.
        :rtype: int
        """
        return 90

    @classmethod
    @property
    def is_one_shot_compatible(cls) -> bool:
        """
        Retrieves whether this primary port should be instantiated when
        "one-shot" behavior is active.
        It should return False unless the port listens to future messages
        from outside.
        :return: True in such case.
        :rtype: bool
        """
        return True

    def add_arguments(self, parser: ArgumentParser):
        """
        Defines the specific CLI arguments.
        :param parser: The parser.
        :type parser: argparse.ArgumentParser
        """
        parser.add_argument(
            "-s",
            "--stack",
            required=False,
            help="The name of the stack",
        )
        parser.add_argument(
            "-p",
            "--project",
            required=False,
            help="The name of the project",
        )
        parser.add_argument(
            "-l",
            "--location",
            required=False,
            help="The location of the project",
        )
        parser.add_argument(
            "-c",
            "--credential-name",
            required=True,
            help="Specify the credential name for Docker login",
        )
        parser.add_argument(
            "-p",
            "--credential-password",
            required=False,
            help="Specify the credential password for Docker login",
        )

    async def handle(self, app: PythonedaApplication, args):
        """
        Processes the command specified from the command line.
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.PythonedaApplication
        :param args: The CLI args.
        :type args: argparse.args
        """
        await app.accept_docker_image_push_requested(
            {
                "stack_name": args.stack,
                "project_name": args.project,
                "location": args.location,
                "credential_name": args.credential_name,
                "credential_value": args.credential_password,
            }
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
