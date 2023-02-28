# Get Started

## Introduction

This repository contains all the code used in the Get Started tutorial of the Craft AI platform.

## Architecture

- **src** : contains the source code used in the steps. Here the code for each step is written in a separate python module for readability but you could have the code of all of your steps in the same python module if you wanted.

- **Part_[1-4]_\*** : contains the notebook that use the craft sdk to create deploy and execute pipelines on the platform

- **scripts** : contains some python scripts to delete the steps, pipelines and deployments of each part

## Setup

write a `.env` file at the root of the repo with the following content


```
CRAFT_AI_ACCESS_TOKEN="*Your craft ai Token*"
CRAFT_AI_ENVIRONMENT_URL="Your craft ai environment URL"
```