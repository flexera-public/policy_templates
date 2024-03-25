FROM ruby:3.2.3-bookworm
# Do general apt update/upgrade
RUN apt-get update && apt-get upgrade -y
# Install misc. packages
RUN apt-get install wget jq git unzip apt-transport-https curl autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm6 libgdbm-dev libdb-dev -y
# Install Ruby gems
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/Gemfile
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/Gemfile.lock
RUN bundle install
# Install Python
RUN apt-get install python3 python3-pip -y
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/.pip_requirements
RUN pip3 install -r .pip_requirements
# Install Node
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/package.json
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/package-lock.json
RUN apt-get install nodejs npm -y
RUN npm install
# Install Go
RUN apt-get install golang -y
# Install Cloud CLIs
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN sudo ./aws/install
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN sudo apt-get update && sudo apt-get install google-cloud-cli

