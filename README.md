# Ollama Wrapper 

Building an UI to interact with a local ollama deployment, exposed on port 11434.



## Install intructions 

Run the following command to build the containers
1. ``` cd frontend ```
2. ``` npm i ``` and after installing the node modules, ``` cd .. ```
3.  Build and run the containers: ``` docker-compose up --build```
4.  Access UI on localhost:3000

Once the containers have been built, there is no need to build them again and the system can be started with ``` docker-compose up ``` going forward

## Tech stack overview 

React - FastAPI - ollama 

## Use Case/ Function 
A custom UI for local LLM deployments that are used for security/privacy purposes where prompts contain sensitive information that cannot be shared with commercial models e.g., Protected Health Information.
