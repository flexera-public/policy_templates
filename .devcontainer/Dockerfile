FROM mcr.microsoft.com/devcontainers/base:ubuntu
# Do general apt update/upgrade
RUN apt-get update && apt-get upgrade -y
# Install misc. packages
RUN apt install wget jq git apt-transport-https curl autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm6 libgdbm-dev libdb-dev -y
# Install Ruby
RUN curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc
RUN source ~/.bashrc
RUN rbenv install 3.2.3
RUN rbenv global 3.2.3
RUN gem install bundler
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/Gemfile
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/Gemfile.lock
RUN bundle install --without documentation --path bundle
# Install Python
RUN apt install python3 pip -y
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/.pip_requirements
RUN pip install -r .pip_requirements
# Install Node
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/package.json
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/package-lock.json
RUN apt install nodejs npm -y
# Install Go
RUN apt install golang -y
# Install Cloud CLIs
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN sudo ./aws/install
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN sudo apt-get update && sudo apt-get install google-cloud-cli

