FROM ruby:3.2.3-bookworm
# Add Google to apt list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
# Do general apt update/upgrade
RUN apt-get update && apt-get upgrade -y
# Install misc. packages
RUN apt-get install google-cloud-cli gpg nodejs npm golang python3 python3-pip pylint bash wget jq git unzip apt-transport-https curl autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm6 libgdbm-dev libdb-dev -y
# Install Ruby gems
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/Gemfile
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/Gemfile.lock
RUN bundle install
# Install Node packages
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/package.json
RUN wget https://raw.githubusercontent.com/flexera-public/policy_templates/master/package-lock.json
RUN npm install
# Install AWS/Azure Cloud CLIs
RUN wget https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip
RUN unzip awscli-exe-linux-x86_64.zip
RUN rm awscli-exe-linux-x86_64.zip
RUN bash ./aws/install
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash
# Install and update fpt
RUN wget https://binaries.rightscale.com/rsbin/fpt/v1.5.0/fpt-linux-amd64.tgz
RUN tar xvzf fpt-linux-amd64.tgz
RUN mv fpt/fpt /usr/local/bin/fpt
RUN rm fpt-linux-amd64.tgz
RUN rmdir fpt
RUN /usr/local/bin/fpt update apply
