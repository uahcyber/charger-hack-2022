#!/bin/bash

# generates a new challenge subdirectory with default file structure
# for use in the UAH Cybersecurity Club 2022 Week of Welcome CTF

SAVED_PWD=`pwd`
USED_PORTS=("22" "80") # add any ports actively used by the host server here

echo "Creating new CTF challenge"
read -p "Category: " CATEGORY
read -p "Name: " NAME

# lowercase
NAME=${NAME,,}
CATEGORY=${CATEGORY,,}

cd "$(dirname "$0")" # get into script directory to reference ../challenges

if [ -d "../challenges/$CATEGORY/$NAME" ]; then
    echo "Challenge with name $NAME already created in the $CATEGORY category"
    exit
fi

read -p "Description: " DESC
read -p "Needs Docker? [y/n]: " NEEDS_DOCKER

mkdir -p ../challenges/$CATEGORY/$NAME/solution
touch ../challenges/$CATEGORY/$NAME/flag.txt
mkdir -p ../challenges/$CATEGORY/$NAME/dist

echo -n $DESC >> ../challenges/$CATEGORY/$NAME/description.txt
if [ ${NEEDS_DOCKER^^} == "Y" ]; then
    cat <<EOT >> ../challenges/$CATEGORY/$NAME/start.sh
#!/bin/bash
# BEGIN DONT TOUCH
cd /home/user
# END DONT TOUCH
# modify me to run the challenge
EOT
    read -p "What port will need to be exposed from the container?: " PORT
    mkdir -p ../challenges/$CATEGORY/$NAME/to_copy
    chmod +x ../challenges/$CATEGORY/$NAME/start.sh
    readarray -t FOUND_PORTS < <(grep -rnw "docker run -it --rm -p" ../challenges/ | cut -d':' -f3 | awk -F'-it --rm -p ' '{ print $NF }')
    USED_PORTS+=("${FOUND_PORTS[@]}")
    while true; do
        FPORT=`shuf -i1024-65535 -n1`
        # if new port is not in array of already used host ports
        if [[ ! " ${USED_PORTS[@]} " =~ " ${FPORT} " ]]; then
            break
        fi
    done
    cat <<EOT >> ../challenges/$CATEGORY/$NAME/nsjail.cfg
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# See options available at https://github.com/google/nsjail/blob/master/config.proto

name: "default-nsjail-configuration"
description: "Default nsjail configuration for pwnable-style CTF task."

mode: ONCE
uidmap {inside_id: "1000"}
gidmap {inside_id: "1000"}
mount_proc: true
rlimit_as_type: HARD
rlimit_cpu_type: HARD
rlimit_nofile_type: HARD
rlimit_nproc_type: HARD

mount: [
  {
    src: "/chroot"
    dst: "/"
    is_bind: true
  },
  {
    src: "/etc/resolv.conf"
    dst: "/etc/resolv.conf"
    is_bind: true
  }
]
EOT
    cat <<EOT >> ../challenges/$CATEGORY/$NAME/Dockerfile
#  Copyright 2020-2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FROM ubuntu:22.04 as chroot
LABEL maintainer="uahcybersec@uah.edu"
LABEL version="0.1"
LABEL description="$CATEGORY challenge '$NAME' for the UAH Cybersecurity Club's 2022 Week of Welcome CTF."
RUN /usr/sbin/useradd --no-create-home -u 1000 user
WORKDIR /home/user
ADD to_copy /home/user/
COPY start.sh start.sh
RUN chmod -R 555 /home/user
FROM gcr.io/kctf-docker/challenge@sha256:501458c0426acc3b5a74a661791271faf0dca6555b46bfb76f944d2558bd08d5
COPY --from=chroot / /chroot
COPY nsjail.cfg /home/user/
CMD kctf_setup && kctf_drop_privs socat TCP-LISTEN:${PORT},reuseaddr,fork EXEC:"kctf_pow nsjail --config /home/user/nsjail.cfg -- /home/user/start.sh"
EOT
    cat <<EOT >> ../docker-compose.yml
  ${CATEGORY,,}-${NAME,,}:
    restart: always
    build:
      context: "./challenges/${CATEGORY,,}/${NAME,,}"
      dockerfile: "./Dockerfile"
    ports:
      - "$FPORT:$PORT"
    privileged: true
EOT
    echo "Place any final binaries/flag files in $CATEGORY/$NAME/to_copy and modify $CATEGORY/$NAME/start.sh as needed."
    echo "To test the container, run $CATEGORY/$NAME/test.sh as root."
fi

echo "Created challenge in $CATEGORY/$NAME!"
cd $SAVED_PWD
exit
