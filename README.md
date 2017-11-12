# hackrpi2017
Our repo for the BigSister Alexa Text Game.

http://www.bigsisteriswatching.com forwards the zappa deployed https.

## Deploying with Zappa
After downloading the repo, activate the virtual environment with:

`source venv/bin/activate`

If the zappa is not deployed, deploy it with:

`zappa deploy dev`

Every change to the source files requires you to update with:

`zappa update`

Undeploy Zappa with:

`zappa undeploy`

Deactivate the virtual environment with:

`deactivate`

__NOTE:__ deactivating or undeploying the service will remove the ability to connect.

After this is completed, you should be able to use it with Alexa so long as the Skill __bigSister__ is added to the device.
The address output by Zappa must be added in the AWS Skill editor.
A walkthrough of the entire install process with zappa can be found [here](https://developer.amazon.com/blogs/post/8e8ad73a-99e9-4c0f-a7b3-60f92287b0bf/new-alexa-tutorial-deploy-flask-ask-skills-to-aws-lambda-with-zappa)
