#!/bin/bash

if [ $(git remote | grep upstream) != "upstream" ]; then
  gum style --foreground "#F00" ":exclamation: No upstream remote found"  | gum format -t emoji
  git remote add upstream https://github.com/tataraba/simplesite
fi

echo "Choose a branch to speed up to :car: :dash:" | gum format -t emoji
branch=$(gum choose "main" "01_templates" "02_tailwind" "03_tinydb" "04_htmx")

gum confirm "Are you sure you want to speed up to \"$branch?\"" 
echo "Cool :sunglasses:. Adding $branch to your local repo" | gum format -t emoji

git merge "origin/$branch"