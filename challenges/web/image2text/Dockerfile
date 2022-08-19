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
FROM python:latest
LABEL maintainer="uahcybersec@uah.edu"
LABEL version="0.1"
LABEL description="web challenge 'image2text' for the UAH Cybersecurity Club's 2022 Week of Welcome CTF."
RUN /usr/sbin/useradd --no-create-home -u 1000 user
WORKDIR /home/user
ADD to_copy /home/user/
RUN pip3 install flask Pillow pytesseract
RUN apt-get update && apt-get install tesseract-ocr -y
COPY start.sh start.sh
RUN chmod -R 555 /home/user
RUN chmod -R 666 /home/user/uploads
CMD bash -c "/home/user/start.sh"
