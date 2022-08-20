# Charger Hack 2022 Challenges

Scripts, resources, and challenges for the UAH Cybersecurity Club's 2022 Charger Hack CTF. 

Usage
-----

Have a `.env` file in the root directory of this project with values for the following:

```bash
CTF_EMAIL=ctfchallemail@gmail.com
CTF_EMAIL_PASSWORD=supersecretpassword
```

To create a new challenge, run:

```bash
./general_scripts/new_challenge.sh
```

To start all challenges, run:

```bash
sudo docker-compose up --build [-d]
```

To stop all challenge instances, run:

```bash
sudo docker-compose down
```