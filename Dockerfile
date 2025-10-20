FROM fedora:42
RUN sudo dnf install mock mock-scm
RUN sudo usermod -a -G mock user
RUN newgrp mock

