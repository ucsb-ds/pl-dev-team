#!/usr/bin/env bash

echo "Installing software needed to run Jekyll locally... "

[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"


rvm install ruby-2.7.7
rvm use 2.7.7
gem install bundler 
#gem install pkg-config
#gem install nokogiri
# bundle config build.nokogiri --use-system-libraries

rm Gemfile.lock
bundle install
bundle lock --add-platform x86_64-linux
bundle lock --add-platform x86_64-darwin-21

echo "Done."
